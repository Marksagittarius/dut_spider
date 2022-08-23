from multiprocessing import cpu_count, Process, JoinableQueue
from store import store_actress_as_json
from config.spider import base_url_of_actress
from bs4 import BeautifulSoup
from model import Actress
from . import reg
import logging
import urllib
import time
import re

actress_list = []
url_list = []
cpu_num = cpu_count()


def query_html(url):
    """ Return the html context of the given url.
    
    Args:
        url (string): The url of the given website.
    
    Returns:
        html_result(string): The html context of the given website.
    """

    header_config = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
    request = urllib.request.Request(url, headers=header_config)
    html_result = ""
    try:
        html_result = urllib.request.urlopen(request).read().decode("utf-8")
    except urllib.error.URLError as url_error:
        if hasattr(url_error, "reason"):
            logging.error(url_error.reason)
    return html_result


def consumer(queue, name, ans):
    """ The handler of the consumer thread. Get the base information of the actress from the given url, transform
    the separate information into the model (Actress) which will be stored
    in the "JoinableQueue" from the input data.
        
    Args:
        @queue (JoinableQueue<string>): A special inheritance of the data-structure
        Queue which implements the feature of sharing memory as well as the consistence
        in multiple threads, carrying the list of the url strings.
        @name (string): The id of the consumer thread.
        @ans (JoinableQueue<Actress>): Collecting the list of Actress which is the result of
            the function "parse_actress_html(base_html: string)".
            
    Returns:
        (void)
    """
    
    while True:
        url = queue.get()
        print("%s is working" % (name))
        if url is None:
            break
        actress = parse_actress_html(query_html(base_url_of_actress + url))
        if actress is not None:
            ans.put(actress)
        queue.task_done()
    

def producer(queue, name, url_list):
    """ The handler of the producer thread.
    Store the list of url in the task queue which will be distributed
    to the consumer threads.
    
    Args:
        @queue (JoinableQueue<string>): The task queue which will be sent
        to the consumer thread.
        @name (string): The id of the thread.
        @url_list ([]string): The list of the url.
        
    Returns:
        (void)
    """
    
    for url in url_list:
        print("%s is working" % (name))
        queue.put(url)
    queue.join()


def parse_actress_category_html(base_html):
    """ Parse the html file of the given category page. Get the list of the hyperlink url
    from the given html element. Make the preparation of the dispatch of the multiple thread
    tasks about web-spider and collect the whole result of the spider tasks which will be sent
    to the layer of storage.
    
    Args:
        @base_html (string): The url of the category web-page.
        
    Returns:
        (void)
    """
    
    soup = BeautifulSoup(base_html, "html.parser")
    for item in soup.find_all("td", width="507", height="30"):
        hyper_link = re.findall(reg.is_hyper_link, str(item))
        if hyper_link != "":
            url_list.append(hyper_link[0])
            print("Get Hyper Link " + hyper_link[0])

    start = time.time()
    ans = JoinableQueue()
    queue = JoinableQueue()
    producer_instance = Process(target=producer, args=(queue, "Producer", url_list))
    consumers = []
    
    for i in range(cpu_num):
        consumers.append(Process(target=consumer, args=(queue, "Consumer[" + str(i) + "]", ans)))
    
    for con in consumers:
        con.daemon = True
    
    producer_instance.start()
    for con in consumers:
        con.start()
            
    producer_instance.join()
    
    end = time.time()
    
    print("Spider Time :" + str(end - start) + "s")
    actress_list = []
    while not ans.empty():
        actress_list.append(ans.get())
    store_actress_as_json(actress_list)
    
    
def parse_actress_html(base_html):
    """ Parse the given html file and get the base information of the actress, which
    will be stored in the form of structure Actress.
    
    Args:
        @base_html (string): The html file of the Wiki page of the Actress.
    
    Returns:
        @actress (Actress): The structure describing the base information of the Actress.
    """
    
    soup = BeautifulSoup(base_html, "html.parser")
    left_element = soup.find("dl", class_="basicInfo-block basicInfo-left")
    right_element = soup.find("dl", class_="basicInfo-block basicInfo-right")
    item = str(left_element) + str(right_element)
    name_value = ""
    name_list = re.findall(reg.is_name, str(item))
    if len(name_list) > 0:
        name_value = re.sub(r'<dt class="basicInfo-item name" id="basic-name">中文名</dt>\n<dd class="basicInfo-item value">\n', "", str(name_list[0]))
        name_value = re.sub(r'\n</dd>', "", str(name_value))
    
    nation_value = ""
    nation_list = re.findall(reg.is_nation, str(item))
    if len(nation_list) > 0:
        nation_value = re.sub(r'<dt class="basicInfo-item name" id="basic-name">民\s*族</dt>\n<dd class="basicInfo-item value">\n', "", str(nation_list[0]))
        nation_value = re.sub(r'\n</dd>', "", str(nation_value))
        nation_value = re.sub(r'</?a.*?>', "", nation_value)
        
    birthday_value = ""
    birthday_list = re.findall(reg.is_birthday, str(item))
    if len(birthday_list) > 0:
        birthday_value = re.sub(r'<dt class="basicInfo-item name" id="basic-name">出生日期</dt>\n<dd class="basicInfo-item value">\n', "", str(birthday_list[0]))

    blood_type_value = ""
    blood_type_list = re.findall(reg.is_blood_type, str(item))
    if len(blood_type_list) > 0:
        blood_type_value = re.sub(r'<dt class="basicInfo-item name" id="basic-name">血\s*型</dt>\n<dd class="basicInfo-item value">\n', "", str(blood_type_list[0]))
        
    constellation_value = ""
    constellation_list = re.findall(reg.is_constellation, str(item))
    if len(constellation_list) > 0:
        constellation_value = re.sub(r'<dt class="basicInfo-item name" id="basic-name">星\s*座</dt>\n<dd class="basicInfo-item value">\n', "", str(constellation_list[0]))
        constellation_value = re.sub(r'</?a.*?>', "", constellation_value)
                
    height_value = ""
    height_list = re.findall(reg.is_height, str(item))
    if len(height_list) > 0:
        height_value = re.sub(r'<dt class="basicInfo-item name" id="basic-name">身\s*高</dt>\n<dd class="basicInfo-item value">\n', "", str(height_list[0]))
        height_value = re.sub(r'\scm', "", height_value)
    
    weight_value = ""
    weight_list = re.findall(reg.is_weight, str(item))
    if len(weight_list) > 0:
        weight_value = re.sub(r'<dt class="basicInfo-item name" id="basic-name">体\s*重</dt>\n<dd class="basicInfo-item value">\n', "", str(weight_list[0]))
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
        actress = Actress(name=name_value, nation=nation_value, birthday=birthday_value, blood_type=blood_type_value, constellation=constellation_value, height=height_value, weight=weight_value)
    return actress
    
        
        
        
        


        
    
