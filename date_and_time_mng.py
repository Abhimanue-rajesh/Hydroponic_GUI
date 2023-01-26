import customtkinter
import time 
import pickle

from customtkinter import *
from tkinter import *
from datetime import date


#Theme and apperance of main window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#Main_window_Feature_managment
root = customtkinter.CTk()
root.title('Hydrophonics')
root.minsize(1330,690)
window_width = 1330
window_height = 690
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
center_y_n = center_y - 35
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y_n}')

#Functions
def Time():
    current_time = ''
    new_time = time.strftime('%H:%M:%S')
    if current_time != new_time:
        current_time=new_time
        time_label.configure(text=new_time)
    time_label.after(200,Time)    

def Date():
    current_date = date.today()
    current_date = current_date.strftime("%B %d, %Y")
    date_label.configure(text=current_date)

def storeing_data():
    t_and_d=time.localtime()
    current_year  = t_and_d.tm_year
    current_month = t_and_d.tm_mon
    current_day   = t_and_d.tm_mday
    current_min   = t_and_d.tm_min
    data_base = {}
    data_base[0]=current_year
    data_base[1]=current_month
    data_base[2]=current_day
    data_base[3]=current_min
    data_base_file=open('d_&_t','ab')
    pickle.dump(data_base,data_base_file)
    data_base_file.close

def loading_data():
    data_base_file=open('d_&_t','rb')
    data_base=pickle.load(data_base_file)
    print(data_base)
    for keys in data_base:
        print(keys, '=>', data_base[keys])
    data_base_file.close


#Clock 
date_time_frame=customtkinter.CTkFrame(master=root,width=480,height=50,corner_radius=20,border_color='Green',border_width=2)
date_time_frame.place(relx=0.5,rely=0.05,anchor=CENTER)
time_label = customtkinter.CTkLabel(master=date_time_frame, font=('Centuray Gothic', 30,))
time_label.place(relx=0.8,rely=0.5, anchor=CENTER)
date_label = customtkinter.CTkLabel(master=date_time_frame, font=('Centuray Gothic', 30,))
date_label.place(relx=0.3,rely=0.5, anchor=CENTER)
Time()
Date()

#Exit Button 
exit_button = customtkinter.CTkButton(master=root, text= "Exit", command=root.destroy,width=200,height=40,corner_radius=20,
                                      font=('Century Gothic',20),hover_color='Red4')
exit_button.place(relx=0.9,rely=0.95,anchor=CENTER)

#Storeing Button
str_btn = customtkinter.CTkButton(master=root,text='store',command=storeing_data,width=200,height=40,corner_radius=20,
                                      font=('Century Gothic',20))
str_btn.place(relx=0.5,rely=0.5,anchor=CENTER)

#Loading Data
ld_btn = customtkinter.CTkButton(master=root,text='Load',command=loading_data,width=200,height=40,corner_radius=20,
                                      font=('Century Gothic',20))
ld_btn.place(relx=0.5,rely=0.6,anchor=CENTER)

#looping root
root.mainloop()