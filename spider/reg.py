import re

is_hyper_link = re.compile(r'<a data-lemmaid=".*?" href="(.*?)" target="_blank">')

is_name = re.compile(r'<dt class="basicInfo-item name" id="basic-name">中文名</dt>\n<dd class="basicInfo-item value">\n.*?\n</dd>')

is_nation = re.compile(r'<dt class="basicInfo-item name" id="basic-name">民\s*族</dt>\n<dd class="basicInfo-item value">\n.*?\n</dd>')

is_birthday = re.compile(r'<dt class="basicInfo-item name" id="basic-name">出生日期</dt>\n<dd class="basicInfo-item value">\n.*?日')

is_blood_type = re.compile(r'<dt class="basicInfo-item name" id="basic-name">血\s*型</dt>\n<dd class="basicInfo-item value">\n.*?型')

is_constellation = re.compile(r'<dt class="basicInfo-item name" id="basic-name">星\s*座</dt>\n<dd class="basicInfo-item value">\n.*?座')

is_height = re.compile(r'<dt class="basicInfo-item name" id="basic-name">身\s*高</dt>\n<dd class="basicInfo-item value">\n.*?cm')

is_weight = re.compile(r'<dt class="basicInfo-item name" id="basic-name">体\s*重</dt>\n<dd class="basicInfo-item value">\n.*?kg')

is_actor_hyper_link = re.compile(r'<dt><a data-lemmaid=".*?" href=".*?" target="_blank">')

is_epidemic_data = re.compile(r'window.getAreaStat = ([\s\S]*?)</script>')
