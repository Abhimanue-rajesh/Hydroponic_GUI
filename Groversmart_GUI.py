import customtkinter
import time 
import pickle

from customtkinter import *
from tkinter import *
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta


#Theme and apperance of main window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#Main_window_Feature_managment
root = customtkinter.CTk()
root.title('Hydroponics')
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

def check_box():
    var_a = check_box_nutrition_a.get()
    var_b = check_box_nutrition_b.get()
    if var_a == 'nutrition_a_on':
        check_box_nutrition_a.configure(text='Added Nutriant A')
    else:
        check_box_nutrition_a.configure(text=' ')
    if var_b == 'nutrition_b_on':
        check_box_nutrition_b.configure(text='Added Nutriant B') 
    else:
        check_box_nutrition_b.configure(text=' ') 
    if var_a == 'nutrition_a_on' and var_b == 'nutrition_b_on':
        save_button_nutrition.configure(state='normal')
    else:
        save_button_nutrition.configure(state='disabled')

#Clock 
date_time_frame=customtkinter.CTkFrame(master=root,width=480,height=50,corner_radius=20,border_color='Green',border_width=2)
date_time_frame.place(relx=0.5,rely=0.05,anchor=CENTER)
time_label = customtkinter.CTkLabel(master=date_time_frame, font=('Century Gothic', 30,))
time_label.place(relx=0.8,rely=0.5, anchor=CENTER)
date_label = customtkinter.CTkLabel(master=date_time_frame, font=('Century Gothic', 30,))
date_label.place(relx=0.3,rely=0.5, anchor=CENTER)
Time()
Date()

#Exit Button 
exit_button = customtkinter.CTkButton(master=root, text= "Exit", command=root.destroy,width=200,height=40,corner_radius=20,
                                      font=('Century Gothic',20),hover_color='Red4')
exit_button.place(relx=0.9,rely=0.95,anchor=CENTER)

#Nutrition Frame
nutrition_frame=customtkinter.CTkFrame(master=root,width=500,height=250,corner_radius=20,border_color='Green',border_width=2)
nutrition_frame.place(relx=0.22,rely=0.3,anchor=CENTER)
top_label_nutrition=customtkinter.CTkLabel(master=nutrition_frame,text='Nutritional Information',font=('Century Gothic',30,UNDERLINE),
                                            text_color='Yellow')
top_label_nutrition.place(relx=0.5,rely=0.1,anchor=CENTER)
nutrient_a_label=customtkinter.CTkLabel(master=nutrition_frame,text='Nutrient A (20ml)',font=('Century Gothic', 30,),text_color='white')
nutrient_a_label.place(relx=0.26,rely=0.3,anchor=CENTER)
nutrient_b_label=customtkinter.CTkLabel(master=nutrition_frame,text='Nutrient B (20ml)',font=('Century Gothic', 30,),text_color='white')
nutrient_b_label.place(relx=0.26,rely=0.5,anchor=CENTER)
check_box_nutrition_a=customtkinter.CTkCheckBox(master=nutrition_frame,text=' ',onvalue='nutrition_a_on',offvalue='nutrition_a_off',
                                                command=check_box,font=('Century Gothic', 20,))
check_box_nutrition_a.place(relx=0.72,rely=0.32,anchor=CENTER)
check_box_nutrition_b=customtkinter.CTkCheckBox(master=nutrition_frame,text=' ',onvalue='nutrition_b_on',offvalue='nutrition_b_off',
                                                command=check_box,font=('Century Gothic', 20,))
check_box_nutrition_b.place(relx=0.72,rely=0.51,anchor=CENTER)
save_button_nutrition=customtkinter.CTkButton(master=nutrition_frame,text='Save',width=150,height=30,corner_radius=20,font=('Century Gothic',20),
                                                    state='disabled')
save_button_nutrition.place(relx=0.83,rely=0.9,anchor=CENTER)


#Water Frame
water_frame=customtkinter.CTkFrame(master=root,width=500,height=250,corner_radius=20,border_color='Green',border_width=2)
water_frame.place(relx=0.22,rely=0.7,anchor=CENTER)
save_button_water=customtkinter.CTkButton(master=water_frame,text='Save',width=150,height=30,corner_radius=20,font=('Century Gothic',20))
save_button_water.place(relx=0.83,rely=0.9,anchor=CENTER)
date_label_water=customtkinter.CTkLabel(master=water_frame)

#looping root
root.mainloop()