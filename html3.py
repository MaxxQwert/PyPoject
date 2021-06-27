import requests
import re
from urllib.parse import urlparse

def ref_ex(url):
    hosts = []
    refs = re.findall(r'<a.*href\s*?=\s*?[\"\'](.*?)[\"\']', requests.get(url).text)
    for ref in refs:
        host = urlparse(ref).hostname
        if host != None:
            hosts.append(host)
    return hosts

refs = {}
url = input()
refs = sorted(list(set(ref_ex(url))))
for i in refs:
    print(i)

# https://stepic.org/media/attachments/lesson/24472/sample0.html
#https://pastebin.com/raw/hfMThaGb
#[/:\?]