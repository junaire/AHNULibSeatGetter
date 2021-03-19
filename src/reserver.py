import requests
import datetime

class Reserver:
    def __init__(self):
        self.reserve_url = "http://libzwxt.ahnu.edu.cn/SeatWx/ajaxpro/SeatManage.Seat,SeatManage.ashx"
        self.headers = {
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

    def choose_time(self, date_offset, start_time, end_time):
        today = datetime.date.today()
        date = today + datetime.timedelta(days=date_offset)

        start = str(date) + " " + str(start_time)
        end   = str(date) + " " + str(end_time)
        return str(date), start, end

    def _reserve_seat(self,seat_code, date, start_time, end_time):

        data = '{"sid":"%d","atDate":"%s","st":"%s","et":"%s"}' % (int(seat_code),str(date), str(start_time), str(end_time))
        try:
            response = self.session.post(url=self.reserve_url,headers=headers,data=data,verify=False)
            if "预约成功" in response.text:
                return True
            else:
                return False
        except:
            return False


    def reserve(self,seat_code, date_offset, start_time, end_time):
        date, start, end = self.choose_time(date_offset, start_time, end_time)
        self._reserve_seat(seat_code, date, start, end)
