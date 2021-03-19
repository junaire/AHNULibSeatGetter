import requests
from lxml import etree
class Checker:
    def check(seat_url):
        response = requests.get(seat_url)
        html = etree.HTML(respsonse.content)
        times = html.xpath("//ul[@class='ulTimes']/li")
