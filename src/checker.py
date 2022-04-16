import requests
from lxml import etree
class Checker:
    def check(self, seat_url):
        response = requests.get(seat_url)
        html = etree.HTML(response.content)
        times = html.xpath("//ul[@class='ulTimes']/li")
