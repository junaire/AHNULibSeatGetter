from reserver import Reserver
from seatgetter import SeatGetter
from loginer import Loginer


class Helper:
    def __init__(self,student_id):
        
        self.loginer = Loginer(student_id,student_id)
        session = self.loginer.login()
        self.reserver = Reserver(session)
        self.seat_getter = SeatGetter(student_id,session)

    def _reserve_all(self,room_code,date_number,start_time,end_time):
        url, seats = self.seat_getter.choose_seat(room_code)
        for seat in seats:
            reserve_status = self.reserver.reserve(seat,date_number,start_time,end_time)
            if reserve_status:
                return True
        return False
            

    def run(self,room_code,date_number,start_time,end_time):
        flag = self._reserve_all(room_code,date_number,start_time,end_time)
        return flag
