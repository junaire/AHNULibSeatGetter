import requests
from lxml import etree
class Loginer:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session  = requests.Session();
        self.session.trust_env = False
        self.login_url = "http://libzwxt.ahnu.edu.cn/SeatWx/login.aspx"
        self.headers = {
            'Proxy-Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7',
            }

    def _get_view_code(self):
        data = {
            'tbUserName': self.username,
            'tbPassWord': self.password,
            'Button1': '\u767B \u5F55  ',
            'hfurl': ''
        }
        response = self.session.post(url=self.login_url,headers=self.headers,data=data)

        if response.status_code == 200:
            html = etree.HTML(response.text)
            view_code = html.xpath("//input/@value")
            return view_code
        return None


    def login(self):
        view_code = self._get_view_code()
        if not view_code:
            print("Can't get view code")
            exit(-1)

        data = {
            '__VIEWSTATE':view_code[0],
            '__VIEWSTATEGENERATOR': view_code[1],
             '__EVENTVALIDATION': view_code[2],
            'tbUserName': self.username,
            'tbPassWord': self.password,
            'Button1': '\u767B \u5F55  ',
            'hfurl': ''
        }
        response = self.session.post(url=self.login_url,headers=self.headers,data=data)
        if response.status_code == 200:
            return self.session
        else:
            return None
