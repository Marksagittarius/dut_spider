from config.spider import start_url_of_actress, start_url_of_television
from .actress import parse_actress_category_html
from .television import parse_television_category_html
import urllib.request
import urllib.error
import logging


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


def start_all_tasks():
    """ Start all the tasks of spider.
    
    """
    
    print("Task: Actress")
    parse_actress_category_html(query_html(start_url_of_actress))
    
    print("Task: Television")
    parse_television_category_html(query_html(start_url_of_television))