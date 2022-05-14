import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

from helper import Helper

window = tk.Tk()
window.title("Fuck AHNU Library Seat Reservation")
window.geometry("300x400")


def place_label(text):
    message = tk.Label(window, text=text, font=("Arial", 12))
    message.pack()


def print_error(message):
    tk.messagebox.showerror(title="Error", message=message)


def print_info(message):
    tk.messagebox.showinfo(title="Info", message=message)


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
        "4楼公共W": "4g2",
    }
    return rooms[room]


def parse_date(date_str):
    if date_str == "Today":
        return 0
    elif date_str == "Tomorrow":
        return 1
    elif date_str == "The day after tomorrow":
        return 2


place_label("please enter your student id:")
student_id = tk.Entry(window)
student_id.pack()

place_label("please enter your password:")
password = tk.Entry(window)
password.pack()

place_label("please choose date")
date = ttk.Combobox(window)
date.pack()
date["value"] = ("Today", "Tomorrow", "The day after tomorrow")

place_label("please choose the room:")
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
    "4楼公共W",
)


place_label("please choose start time")
start_time = ttk.Combobox(window)
start_time.pack()
start_time["value"] = (
    "8:00",
    "8:30",
    "9:00",
    "9:30",
    "10:00",
    "10:30",
    "11:00",
    "11:30",
    "12:00",
    "12:30",
    "13:00",
    "13:30",
    "14:00",
    "14:30",
    "15:00",
    "15:30",
    "16:00",
    "16:30",
    "17:00",
    "17:30",
    "18:00",
    "18:30",
    "19:00",
    "19:30",
    "20:00",
    "20:30",
    "21:00",
)


place_label("please choose end time")
end_time = ttk.Combobox(window)
end_time.pack()
end_time["value"] = (
    "8:00",
    "8:30",
    "9:00",
    "9:30",
    "10:00",
    "10:30",
    "11:00",
    "11:30",
    "12:00",
    "12:30",
    "13:00",
    "13:30",
    "14:00",
    "14:30",
    "15:00",
    "15:30",
    "16:00",
    "16:30",
    "17:00",
    "17:30",
    "18:00",
    "18:30",
    "19:00",
    "19:30",
    "20:00",
    "20:30",
    "21:00",
    "21:30",
    "22:00",
)


def run():
    helper = Helper(student_id.get(), password.get())

    res = helper.run(
        parse_room_code(room.get()),
        parse_date(date.get()),
        start_time.get(),
        end_time.get(),
    )

    if res:
        print_info("Congradulations! :)")
    else:
        print_error("Shit! I failed :(")


b = tk.Button(window, text="Go", font=("Arial", 12), width=10, height=1, command=run)
b.pack()

window.mainloop()
