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

#Fonts
fcg15=customtkinter.CTkFont('Century Gothic',15,)
fcg20=customtkinter.CTkFont('Century Gothic',20,)
fcg25=customtkinter.CTkFont('Century Gothic',25,)
fcg30=customtkinter.CTkFont('Century Gothic',30,)

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
    if var_a == 'nutrition_a_on' and var_b == 'nutrition_b_on':
        save_button_nutrition.configure(state='normal')
    else:
        save_button_nutrition.configure(state='disabled')

#Clock 
date_time_frame=customtkinter.CTkFrame(master=root,width=480,height=50,corner_radius=20,border_color='Green',border_width=2)
date_time_frame.place(relx=0.5,rely=0.05,anchor=CENTER)
time_label = customtkinter.CTkLabel(master=date_time_frame, font=fcg30)
time_label.place(relx=0.8,rely=0.5, anchor=CENTER)
date_label = customtkinter.CTkLabel(master=date_time_frame, font=fcg30)
date_label.place(relx=0.3,rely=0.5, anchor=CENTER)
Time()
Date()

#Exit Button 
exit_button = customtkinter.CTkButton(master=root, text= "Exit", command=root.destroy,width=200,height=40,corner_radius=20,font=fcg20,
                                        hover_color='Red4')
exit_button.place(relx=0.9,rely=0.95,anchor=CENTER)

#Nutrition Frame
nutrition_frame=customtkinter.CTkFrame(master=root,width=500,height=250,corner_radius=20,border_color='Green',border_width=2)
nutrition_frame.place(relx=0.22,rely=0.3,anchor=CENTER)
top_label_nutrition=customtkinter.CTkLabel(master=nutrition_frame,text='Nutritional Information',font=('Century Gothic',30,UNDERLINE),
                                            text_color='Yellow')
top_label_nutrition.place(relx=0.5,rely=0.1,anchor=CENTER)
nutrient_a_label=customtkinter.CTkLabel(master=nutrition_frame,text='Nutrient A (20ml)',font=fcg30,text_color='white')
nutrient_a_label.place(relx=0.29,rely=0.3,anchor=CENTER)
nutrient_b_label=customtkinter.CTkLabel(master=nutrition_frame,text='Nutrient B (20ml)',font=fcg30,text_color='white')
nutrient_b_label.place(relx=0.29,rely=0.5,anchor=CENTER)
info_display_text=customtkinter.CTkTextbox(master=nutrition_frame,width=300,height=80,state='disabled',corner_radius=10,border_width=2,font=fcg15)
info_display_text.place(relx=0.35,rely=0.77,anchor=CENTER)
check_box_nutrition_a=customtkinter.CTkCheckBox(master=nutrition_frame,text=' ',onvalue='nutrition_a_on',offvalue='nutrition_a_off',
                                                command=check_box,font=fcg20)
check_box_nutrition_a.place(relx=0.7,rely=0.32,anchor=CENTER)
check_box_nutrition_b=customtkinter.CTkCheckBox(master=nutrition_frame,text=' ',onvalue='nutrition_b_on',offvalue='nutrition_b_off',
                                                command=check_box,font=fcg20)
check_box_nutrition_b.place(relx=0.7,rely=0.51,anchor=CENTER)
save_button_nutrition=customtkinter.CTkButton(master=nutrition_frame,text='Save',width=150,height=30,corner_radius=20,font=fcg20,state='disabled')
save_button_nutrition.place(relx=0.83,rely=0.88,anchor=CENTER)
week_one_rdbtn=customtkinter.CTkRadioButton(master=nutrition_frame,text='Week One',value=1,command=check_box,font=fcg15)
week_one_rdbtn.place(relx=0.7,rely=0.25)
week_two_rdbtn=customtkinter.CTkRadioButton(master=nutrition_frame,text='Week Two',value=1,command=check_box,font=fcg15)
week_two_rdbtn.place(relx=0.7,rely=0.39)
week_three_rdbtn=customtkinter.CTkRadioButton(master=nutrition_frame,text='Week Three',value=1,command=check_box,font=fcg15)
week_three_rdbtn.place(relx=0.7,rely=0.53)
week_four_rdbtn=customtkinter.CTkRadioButton(master=nutrition_frame,text='Week Four',value=1,command=check_box,font=fcg15)
week_four_rdbtn.place(relx=0.7,rely=0.66)


#Water Frame
water_frame=customtkinter.CTkFrame(master=root,width=500,height=250,corner_radius=20,border_color='Green',border_width=2)
water_frame.place(relx=0.22,rely=0.7,anchor=CENTER)
save_button_water=customtkinter.CTkButton(master=water_frame,text='Save',width=150,height=30,corner_radius=20,font=fcg20)
save_button_water.place(relx=0.83,rely=0.9,anchor=CENTER)
top_label_water=customtkinter.CTkLabel(master=water_frame,text='Water Replenishment',font=('Century Gothic',30,UNDERLINE),
                                            text_color='Yellow')
top_label_water.place(relx=0.5,rely=0.1,anchor=CENTER)
date_label_water=customtkinter.CTkLabel(master=water_frame,font=fcg30,text_color='white')
date_label_water.place(relx=0.5,rely=0.5,anchor=CENTER)

#looping root
root.mainloop()