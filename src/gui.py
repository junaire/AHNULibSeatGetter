import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

from helper import Helper

window = tk.Tk()
window.title("Fuck AHNU Library Seat Reservation")
window.geometry("500x500")


message = tk.Label(window,text="please enter your student id:",font=("Arial",12))
message.pack()
student_id = tk.Entry(window)
student_id.pack()

message = tk.Label(window,text="please choose date",font=("Arial",12))
message.pack()
date = ttk.Combobox(window)
date.pack()
date["value"] = ('Today','Tomorrow','The day after tomorrow')

message = tk.Label(window,text="please choose the room:",font=("Arial",12))
message.pack()
room = ttk.Combobox(window)
room.pack()
room["value"] = (
        "花津2楼南",
        "花津3楼南",
        "花津3楼北",
        "花津4楼南",
        "花津4楼北",
        "3楼公共E",
        "3楼公共W",
        "4楼公共E",
        "4楼公共W")


message = tk.Label(window,text="please choose start time",font=("Arial",12))
message.pack()
start_time = ttk.Combobox(window)
start_time.pack()
start_time["value"] = ('8:00','8:30','9:00','9:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30','20:00','20:30','21:00')


message = tk.Label(window,text="please choose end time",font=("Arial",12))
message.pack()
end_time = ttk.Combobox(window)
end_time.pack()
end_time["value"] = ('8:00','8:30','9:00','9:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30','20:00','20:30','21:00','21:30','22:00')


def print_error(message):
    tk.messagebox.showerror(title='Error', message=message)
def print_info(message):
    tk.messagebox.showinfo(title='Info', message=message)
def parse_room_code(room):
    rooms = {
        "花津2楼南": "2s",
        "花津3楼南": "3s",
        "花津3楼北": "3n",
        "花津4楼南": "4s",
        "花津4楼北": "4n",
        "3楼公共E": "3g1",
        "3楼公共W": "3g2",
        "4楼公共E": "4g1",
        "4楼公共W":"4g2"
    }
    return rooms[room]

def check_input(raw_student_id, raw_date, raw_room_code, raw_start_time, raw_end_time):
    if raw_student_id and raw_date and raw_room_code and raw_start_time and raw_end_time:
        if raw_date == 'Today':
                date_code = 0
        elif raw_date == 'Tomorrow':
            date_code = 1
        elif raw_date == 'The day after tomorrow':
            date_code =  2
        else:
            date_code = 0

        return True, raw_student_id, date_code, raw_room_code, raw_start_time, raw_end_time
    return False, None, None, None, None, None

def run():
    input_status, s_id, date_offset, room_code, s_time, e_time = check_input(student_id.get(),date.get(),room.get(),start_time.get(),end_time.get())
    if not input_status:
        print_error("Input in incomplete!")
        return

    helper = Helper(s_id)

    res = helper.run(parse_room_code(room_code),date_offset,s_time,e_time)

    if res:
        print_info("Congradulations! :)")
    else:
        print_error("Shit! I failed :(")
    
b = tk.Button(window, text='Reserve', font=('Arial', 12), width=10, height=1, command=run)
b.pack()

window.mainloop()
