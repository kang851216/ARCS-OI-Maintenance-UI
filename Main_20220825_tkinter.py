from tkinter import *

Main = Tk()
Main.geometry('600x600')
title = Label(Main, 
                text="ARCS 户外投放口 运行模式", 
                font = ("Arial", 25)
                )
title.place(x=80, y=20, width=600, height=60)

frame_button = LabelFrame(Main, text="操作按钮", relief="solid", bd=2, font = ("Arial", 14))
frame_button.place(x=30, y=100, width=180, height=180)

button_start = Button(frame_button, width=14, height= 1, text="程序运行", font = ("Arial", 14))
button_start.grid(row=1, column=1)
button_end = Button(frame_button, width=14, height= 1, text="程序结束", font = ("Arial", 14))
button_end.grid(row=5, column=1)


frame_doorstatus = LabelFrame(Main, text="盖门状态", relief="solid", bd=2,  font = ("Arial", 14))
frame_doorstatus.place(x=30, y=290, width=180, height=240)

frame_log = LabelFrame(Main, text="动作记录", relief="solid", bd=2,  font = ("Arial", 14))
frame_log.place(x=220, y=100, width=240, height=430)

frame_info = LabelFrame(Main, relief="solid", bd=2)
frame_info.place(x=480, y=440, width=100, height=90)

Main.mainloop()
