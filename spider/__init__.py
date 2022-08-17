import urllib.request
import urllib.error
import logging


def query_html(url):
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
