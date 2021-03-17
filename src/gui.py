from SeatReserve import Reserver
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk


window = tk.Tk()
window.title("Fuck AHNU Library Seat Reservation")
window.geometry("500x300")

"""
photo = tk.PhotoImage(file=r"D:\\python-projects\\LibraryReservation\\bg.gif")
l = tk.Label(window, image=photo)
l.pack()
"""

message = tk.Label(window,text="please enter your student id:",font=("Arial",12))
message.pack()
student_id = tk.Entry(window)
student_id.pack()




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
end_time["value"] = ('8:00','8:30','9:00','9:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30','20:00','20:30','21:00')

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

def run():
    reserver = Reserver(student_id.get())
    login_staus = reserver.login()
    if not login_staus:
        print_error("Shit! Login failed!")
         
    seats = reserver.choose_seat(parse_room_code(room.get()))
    reserve_status = reserver.reserve_seat(seats,start_time.get(),end_time.get())
    if not reserve_status:
        print_error("Shit! Seat reserve failed! They may all be token!")
    else:
        print_info("Congratulations! Seat was reserved successfully!")


b = tk.Button(window, text='Reserve', font=('Arial', 12), width=10, height=1, command=run)
b.pack()

window.mainloop()
