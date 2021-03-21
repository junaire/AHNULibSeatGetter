from helper import Helper
s_id = input("Please input your student id: ")
print("Today ==================== 0")
print("Tomorrow ================= 1")
print("The day after tomorrow === 2")
date_offset = input("Please choose the date: ")
s_time = input("Please input start time: ")
e_time = input("Please input end time: ")

helper = Helper(s_id)

res = helper.run(room_code,date_offset,s_time,e_time)

if res:
    print("Congradulations! :)")
else:
    print("Shit! I failed :(")

