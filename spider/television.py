from store import store_actor_as_json, store_audience_form_as_json
from multiprocessing import cpu_count, Process, JoinableQueue
from config.spider import base_url_of_television
from model import Actor, AudienceFormUint
from bs4 import BeautifulSoup
from . import query_html
from . import reg
import time
import re

television_list = []
url_list = []
cpu_num = cpu_count()
audience_form_list = []


def consumer(queue, name, ans):
    while True:
        url = queue.get()
        print("%s is working" % (name))
        if url is None:
            break
        actress = parse_actor_html(query_html(base_url_of_television + url))
        if actress is not None:
            ans.put(actress)
        queue.task_done()


def producer(queue, name, url_list):
    for url in url_list:
        print("%s is working" % (name))
        queue.put(url)
    queue.join()


def parse_category_html(base_html):
    soup = BeautifulSoup(base_html, "html.parser")
    for item in soup.find_all("ul", {"class": "actorList"}):
        hyper_link = re.findall(reg.is_actor_hyper_link, str(item))
        if len(hyper_link) > 0:
            for link in hyper_link:
                link = re.sub(r'<dt><a data-lemmaid=".*?" href="', "", str(link))
                link = re.sub(r'" target="_blank">', "", str(link))
                url_list.append(link)
                print("Get Hyper Link " + link)

    start = time.time()
    ans = JoinableQueue()
    queue = JoinableQueue()
    producer_instance = Process(
        target=producer, args=(queue, "Producer", url_list))
    consumers = []

    for i in range(cpu_num):
        consumers.append(Process(target=consumer, args=(
            queue, "Consumer[" + str(i) + "]", ans)))

    for con in consumers:
        con.daemon = True

    producer_instance.start()
    for con in consumers:
        con.start()

    producer_instance.join()

    end = time.time()

    print("Spider Time :" + str(end - start) + "s")
    actor_list = []
    while not ans.empty():
        actor_list.append(ans.get())
    store_actor_as_json(actor_list)


def parse_actor_html(base_html):
    soup = BeautifulSoup(base_html, "html.parser")
    left_element = soup.find("dl", class_="basicInfo-block basicInfo-left")
    right_element = soup.find("dl", class_="basicInfo-block basicInfo-right")
    item = str(left_element) + str(right_element)
    name_value = ""
    name_list = re.findall(reg.is_name, str(item))
    if len(name_list) > 0:
        name_value = re.sub(
            r'<dt class="basicInfo-item name" id="basic-name">中文名</dt>\n<dd class="basicInfo-item value">\n', "", str(name_list[0]))
        name_value = re.sub(r'\n</dd>', "", str(name_value))

    nation_value = ""
    nation_list = re.findall(reg.is_nation, str(item))
    if len(nation_list) > 0:
        nation_value = re.sub(
            r'<dt class="basicInfo-item name" id="basic-name">民\s*族</dt>\n<dd class="basicInfo-item value">\n', "", str(nation_list[0]))
        nation_value = re.sub(r'\n</dd>', "", str(nation_value))
        nation_value = re.sub(r'</?a.*?>', "", nation_value)

    birthday_value = ""
    birthday_list = re.findall(reg.is_birthday, str(item))
    if len(birthday_list) > 0:
        birthday_value = re.sub(
            r'<dt class="basicInfo-item name" id="basic-name">出生日期</dt>\n<dd class="basicInfo-item value">\n', "", str(birthday_list[0]))

    blood_type_value = ""
    blood_type_list = re.findall(reg.is_blood_type, str(item))
    if len(blood_type_list) > 0:
        blood_type_value = re.sub(
            r'<dt class="basicInfo-item name" id="basic-name">血\s*型</dt>\n<dd class="basicInfo-item value">\n', "", str(blood_type_list[0]))

    constellation_value = ""
    constellation_list = re.findall(reg.is_constellation, str(item))
    if len(constellation_list) > 0:
        constellation_value = re.sub(
            r'<dt class="basicInfo-item name" id="basic-name">星\s*座</dt>\n<dd class="basicInfo-item value">\n', "", str(constellation_list[0]))
        constellation_value = re.sub(r'</?a.*?>', "", constellation_value)

    height_value = ""
    height_list = re.findall(reg.is_height, str(item))
    if len(height_list) > 0:
        height_value = re.sub(
            r'<dt class="basicInfo-item name" id="basic-name">身\s*高</dt>\n<dd class="basicInfo-item value">\n', "", str(height_list[0]))
        height_value = re.sub(r'\scm', "", height_value)

    weight_value = ""
    weight_list = re.findall(reg.is_weight, str(item))
    if len(weight_list) > 0:
        weight_value = re.sub(
            r'<dt class="basicInfo-item name" id="basic-name">体\s*重</dt>\n<dd class="basicInfo-item value">\n', "", str(weight_list[0]))
        weight_value = re.sub(r'\skg', "", weight_value)

    if len(blood_type_value) == 0:
        blood_type_value = "未知"

    if len(height_value) == 0:
        height_value = "未知"

    if len(weight_value) == 0:
        weight_value = "未知"

    if len(nation_value) == 0:
        nation_value = "未知"

    if len(name_value) > 0 and len(birthday_value) > 0 and len(constellation_value) > 0:
        actor = Actor(name=name_value, nation=nation_value, birthday=birthday_value, blood_type=blood_type_value, constellation=constellation_value, height=height_value, weight=weight_value)
        return actor


def parse_television_data_form(base_html):
    soup = BeautifulSoup(base_html, "html.parser")
    forms = soup.find_all("table", {"log-set-param": "table_view", "data-sort": "sortDisabled"})
    items = forms[3].find_all("tr")
    items = items[2:]
    for item in items:
        data_units = item.find_all("div", {"class": "para"})
        audience_form_unit = AudienceFormUint(date=data_units[0].text, rate1=data_units[1].text, share1=data_units[2].text,
                                              rank1=data_units[3].text, rate2=data_units[4].text, share2=data_units[5].text, rank2=data_units[6].text)
        audience_form_list.append(audience_form_unit)
        store_audience_form_as_json(audience_form_list)
        