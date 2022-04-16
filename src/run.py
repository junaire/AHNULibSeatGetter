from helper import Helper
s_id = input("Please input your student id: ")
s_passwd = input("Please input your passwd: ")
print("Today ==================== 0")
print("Tomorrow ================= 1")
print("The day after tomorrow === 2")
date_offset = input("Please choose the date: ")
s_time = input("Please input start time: ")
e_time = input("Please input end time: ")
print("花津2楼南: 2s")
print("花津3楼南: 3s")
print("花津3楼北: 3n")
print("花津4楼南: 4s")
print("花津4楼北: 4n")
print("3楼公共E: 3g1")
print("3楼公共W: 3g2")
print("4楼公共E: 4g1")
print("4楼公共W:4g2")
room_code = input("Please choose room: ")

helper = Helper(s_id, s_passwd)
res = helper.run(room_code,date_offset,s_time,e_time)

if res:
    print("Congradulations! :)")
else:
    print("Shit! I failed :(")

