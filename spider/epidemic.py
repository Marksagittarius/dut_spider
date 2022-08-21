from store import store_epidemic_data
from . import reg
import time
import re


global false, null, true
false = null = true = ""


def parse_epidemic_summary_stat(base_html):
    """ Get the data of COVID-9 epidemic of each province in CHINA.

    Args:
        @base_html (string): The html file of given website.
        
    Returns:
        (void)
    """
    
    start = time.time()
    province_info_list = re.findall(reg.is_epidemic_data, base_html)
    province_stat = eval(province_info_list[0].replace('}catch(e){}', ''))
    end = time.time()
    print("Spider Time :" + str(end - start) + "s")
    store_epidemic_data(province_stat)
    