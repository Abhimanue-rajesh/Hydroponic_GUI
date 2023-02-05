import pickle
import time
from datetime import date, datetime
from tkinter import *

import customtkinter
from customtkinter import *
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from tkcalendar import DateEntry
from os import path


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

def save_dates_alert():
   save_file= open('dates.pickle','wb')
   pickle.dump(date_data_list,save_file)
   print('saved')
   save_file.close


def week_one():
    global date_data_list
    file_presence = str(path.exists('dates.pickle'))
    print(file_presence)
    if file_presence == 'True':
       read_file=open('dates.pickle','rb')
       date_data_list = pickle.load(read_file)
       info_display_text.configure(state='normal')
       info_display_text.insert("0.0", date_data_list)
       info_display_text.configure(state='disabled')
    else:
       week = relativedelta(days=+7)
       datetime_now = datetime.now()
       first_week =datetime_now+week
       second_week=first_week+week
       third_week=second_week+week
       fourth_week=third_week+week
       first_day=str(datetime_now.date())
       first_week_date=str(first_week.date())
       second_week_date=str(second_week.date())
       third_week_date=str(third_week.date())
       fourth_week_date=str(fourth_week.date())
       date_data_list={'Initaial Date':first_day,'First Week':first_week_date,
                    'Second Week':second_week_date,'Third Week':third_week_date,
                    'Fourth Week':fourth_week_date}
       info_display_text.insert("0.0", date_data_list)
       save_dates_alert()
    
def refresh():
   if isinstance(check_box_nutrition_a,customtkinter.CTkCheckBox):
    check_box_nutrition_a.deselect()
   if isinstance(check_box_nutrition_b,customtkinter.CTkCheckBox):
    check_box_nutrition_b.deselect()
   if isinstance(week_one_rdbtn,customtkinter.CTkRadioButton):
    week_one_rdbtn.deselect()
   if isinstance(week_two_rdbtn,customtkinter.CTkRadioButton):
    week_two_rdbtn.deselect()
   if isinstance(week_three_rdbtn,customtkinter.CTkRadioButton):
    week_three_rdbtn.deselect()
   if isinstance(week_four_rdbtn,customtkinter.CTkRadioButton):
    week_four_rdbtn.deselect()

#to get the date in loop--whenever the user changes the date input  
def date_update(*args):
    global date_data
    date_data=date_selector.get()
    if len(date_data)==0:
        save_button_water.configure(state='disabled')
    else:
        save_button_water.configure(state='normal')

def next_refil_water():
    print(date_data)
    date_data=parse(date_data)
    week = relativedelta(days=+7)
    print(date_data+week)

def next_date_for_nutriant_refill():
    pass

date_time_frame=customtkinter.CTkFrame(master=root,width=480,height=50,corner_radius=20,border_color='Green',border_width=2)
time_label = customtkinter.CTkLabel(master=date_time_frame, font=fcg30)
date_label = customtkinter.CTkLabel(master=date_time_frame, font=fcg30)
date_time_frame.place(relx=0.5,rely=0.05,anchor=CENTER)
time_label.place(relx=0.8,rely=0.5, anchor=CENTER)
date_label.place(relx=0.3,rely=0.5, anchor=CENTER)
Time()
Date()

#Exit Button 
exit_button = customtkinter.CTkButton(master=root, text= "Exit", command=root.destroy,width=200,height=40,corner_radius=20,font=fcg20,
                                        hover_color='Red4')
exit_button.place(relx=0.9,rely=0.95,anchor=CENTER)

#Nutrition Frame
nutrition_frame=customtkinter.CTkFrame(master=root,width=500,height=300,corner_radius=20,border_color='Green',border_width=2)
top_label_nutrition=customtkinter.CTkLabel(master=nutrition_frame,text='Nutritional Information',font=('Century Gothic',30,UNDERLINE),
                                            text_color='Yellow')
nutrient_a_label=customtkinter.CTkLabel(master=nutrition_frame,text='Nutrient A (20ml)',font=fcg30,text_color='white')
nutrient_b_label=customtkinter.CTkLabel(master=nutrition_frame,text='Nutrient B (20ml)',font=fcg30,text_color='white')
info_display_text=customtkinter.CTkTextbox(master=nutrition_frame,width=300,height=80,state='disabled',corner_radius=10,border_width=2,font=fcg15)
check_box_nutrition_a=customtkinter.CTkCheckBox(master=nutrition_frame,text=' ',onvalue='nutrition_a_on',offvalue='nutrition_a_off',
                                                command=check_box,font=fcg20)
check_box_nutrition_b=customtkinter.CTkCheckBox(master=nutrition_frame,text=' ',onvalue='nutrition_b_on',offvalue='nutrition_b_off',
                                                command=check_box,font=fcg20)
save_button_nutrition=customtkinter.CTkButton(master=nutrition_frame,text='Save',width=150,height=30,corner_radius=20,font=fcg20,state='disabled')
reset_button=customtkinter.CTkButton(master=nutrition_frame,text='Clear All',width=50,height=20,command=refresh,fg_color='Red4',hover_color='Red4')
week_var= IntVar()
week_one_rdbtn=customtkinter.CTkRadioButton(master=nutrition_frame,text='Week One',variable=week_var,value=1,font=fcg15,command=week_one)
week_two_rdbtn=customtkinter.CTkRadioButton(master=nutrition_frame,text='Week Two',variable=week_var,value=2,font=fcg15,state='disabled')
week_three_rdbtn=customtkinter.CTkRadioButton(master=nutrition_frame,text='Week Three',variable=week_var,value=3,font=fcg15,state='disabled')
week_four_rdbtn=customtkinter.CTkRadioButton(master=nutrition_frame,text='Week Four',variable=week_var,value=4,font=fcg15,state='disabled')
nutrition_frame.place(relx=0.22,rely=0.33,anchor=CENTER)
top_label_nutrition.place(relx=0.5,rely=0.1,anchor=CENTER)
nutrient_a_label.place(relx=0.29,rely=0.3,anchor=CENTER)
nutrient_b_label.place(relx=0.29,rely=0.5,anchor=CENTER)
info_display_text.place(relx=0.35,rely=0.77,anchor=CENTER)
check_box_nutrition_a.place(relx=0.7,rely=0.32,anchor=CENTER)
check_box_nutrition_b.place(relx=0.7,rely=0.51,anchor=CENTER)
save_button_nutrition.place(relx=0.83,rely=0.88,anchor=CENTER)
reset_button.place(relx=0.85,rely=0.1)
week_one_rdbtn.place(relx=0.7,rely=0.25)
week_two_rdbtn.place(relx=0.7,rely=0.39)
week_three_rdbtn.place(relx=0.7,rely=0.53)
week_four_rdbtn.place(relx=0.7,rely=0.66)

#Water Frame
water_frame=customtkinter.CTkFrame(master=root,width=500,height=200,corner_radius=20,border_color='Green',border_width=2)
save_button_water=customtkinter.CTkButton(master=water_frame,text='Save',width=150,height=30,corner_radius=20,font=fcg20,state='disabled')
top_label_water=customtkinter.CTkLabel(master=water_frame,text='Water Replenishment',font=('Century Gothic',30,UNDERLINE),
                                            text_color='Yellow')
date_label_water=customtkinter.CTkLabel(master=water_frame,text='Last Water Change',font=fcg20,text_color='white')
date_clear=customtkinter.CTkButton(master=water_frame,text='Clear Selection',font=fcg15,hover_color='Red4',command=lambda:date_selector.delete(0,'end'))
date_change_var=StringVar()
date_selector=DateEntry(master=water_frame,selectmode='day',date_pattern='yyyy-mm-dd',textvariable=date_change_var)
date_selector.set_date(date.today())
date_change_var.trace('w',date_update)
info_water=customtkinter.CTkTextbox(master=water_frame,width=300,height=80,state='disabled',corner_radius=10,border_width=2,font=fcg15)
water_frame.place(relx=0.22,rely=0.7,anchor=CENTER)
save_button_water.place(relx=0.83,rely=0.77,anchor=CENTER)
top_label_water.place(relx=0.5,rely=0.1,anchor=CENTER)
date_label_water.place(relx=0.25,rely=0.3,anchor=CENTER)
date_selector.place(relx=0.47,rely=0.26)
date_clear.place(relx=0.83,rely=0.3,anchor=CENTER)
info_water.place(relx=0.35,rely=0.65,anchor=CENTER)

#Data Display Frame 
data_display_frame=customtkinter.CTkFrame(master=root,width=300,height=250,corner_radius=20,border_color='Green',border_width=2)
data_display_frame_label=customtkinter.CTkLabel(master=data_display_frame,text='Data',font=('Century Gothic',30,UNDERLINE),
                                            text_color='Yellow')
data_display_frame.place(relx=0.55,rely=0.3,anchor=CENTER)
data_display_frame_label.place(relx=0.5,rely=0.1,anchor=CENTER)

#looping root
root.mainloop()