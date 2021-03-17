import requests
import re
import time
import random
from lxml import etree

class Reserver:
    def __init__(self,student_id):
        self.username = student_id
        self.password = student_id
        self.login_url = "http://libzwxt.ahnu.edu.cn/SeatWx/login.aspx?url=http%3a%2f%2flibzwxt.ahnu.edu.cn%2fSeatWx%2findex.aspx"
        self.reserve_url = "http://libzwxt.ahnu.edu.cn/SeatWx/ajaxpro/SeatManage.Seat,SeatManage.ashx"
        self.session = requests.Session()
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
        self.room_urls = {
            '2s': 'http://libzwxt.ahnu.edu.cn/SeatWx/Room.aspx?rid=1&fid=1',
            '2n': '',
            '3s': 'http://libzwxt.ahnu.edu.cn/SeatWx/Room.aspx?rid=6&fid=3',
            '3n': 'http://libzwxt.ahnu.edu.cn/SeatWx/Room.aspx?rid=5&fid=4',
            '4s': 'http://libzwxt.ahnu.edu.cn/SeatWx/Room.aspx?rid=3&fid=5',
            '4n': 'http://libzwxt.ahnu.edu.cn/SeatWx/Room.aspx?rid=4&fid=6',
            '3g1': 'http://libzwxt.ahnu.edu.cn/SeatWx/Room.aspx?rid=13&fid=9',
            '3g2': 'http://libzwxt.ahnu.edu.cn/SeatWx/Room.aspx?rid=14&fid=9',
            '4g1': 'http://libzwxt.ahnu.edu.cn/SeatWx/Room.aspx?rid=15&fid=10',
            '4g2':'http://libzwxt.ahnu.edu.cn/SeatWx/Room.aspx?rid=16&fid=10',
            }



    def _get_view_code(self):
        data = {
            'tbUserName': self.username,
            'tbPassWord': self.password,
            'Button1': '\u767B \u5F55  ',
            'hfurl': 'http%3a%2f%2flibzwxt.ahnu.edu.cn%2fSeatWx%2findex.aspx'
        }
        response = self.session.post(url=self.login_url,headers=self.headers,data=data)
        if response.status_code == 200:
            html = etree.HTML(response.text)
            view_code = html.xpath("//input/@value")
            return view_code


    def login(self):
        view_code = self._get_view_code()
        data = {
            '__VIEWSTATE':view_code[0],
            '__VIEWSTATEGENERATOR': view_code[1],
             '__EVENTVALIDATION': view_code[2],
            'tbUserName': self.username,
            'tbPassWord': self.password,
            'Button1': '\u767B \u5F55  ',
            'hfurl': 'http%3a%2f%2flibzwxt.ahnu.edu.cn%2fSeatWx%2findex.aspx'
        }
        response = self.session.post(url=self.login_url,headers=self.headers,data=data)
        if response.status_code == 200:
            return True
        else:
            return False

   
    def choose_seat(self,room_code):
        try:
            room_url = self.room_urls[room_code]
            response = self.session.get(url=room_url, headers=self.headers)
            html = etree.HTML(response.text)
            lxml_pattern = "//div[@class='seat']//li"
            seats_list = []
            seats = html.xpath(lxml_pattern)
            for seat in seats:
                seat_state = ''.join(seat.xpath("@data-state"))
                if seat_state == '0':
                    seat_url = ''.join(seat.xpath("./a/@href"))
                    seat_code = re.search(r'sid=(\d*)\b', seat_url).group(1)
                    seats_list.append(seat_code)

        except:
            return False
        return seats_list


    def reserve_seat(self,seats_list,start_time,end_time):
        flag = False
        today = time.strftime("%Y-%m-%d", time.localtime())
        headers = {
        'Proxy-Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'X-AjaxPro-Method': 'AddOrder',
        'DNT': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Accept': '*/*',
        'Origin': 'http://libzwxt.ahnu.edu.cn',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7',
    }

        while seats_list:
            seat_code = random.choice(seats_list)
            seats_list.remove(seat_code)
            start = today+" "+start_time
            end   = today+" "+end_time
            data = '{"sid":"%d","atDate":"%s","st":"%s","et":"%s"}'%(int(seat_code),today,start,end)
            try:
                response = self.session.post(url=self.reserve_url,headers=headers,data=data,verify=False)
                time.sleep(1)
                if "有重复部分" in response.text:
                    print(response.text)
                    continue
                elif "预约成功" in response.text:
                    flag = True
                    break
                else:
                    continue
            except:
                continue
        return flag
