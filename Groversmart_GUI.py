import time
from datetime import date, datetime
from os import path
from tkinter import messagebox

import customtkinter
from customtkinter import *
from dateutil.parser import parse
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
fcg15=customtkinter.CTkFont('Century Gothic',15)
fcg20=customtkinter.CTkFont('Century Gothic',20)
fcg30=customtkinter.CTkFont('Century Gothic',30)
fcg45=customtkinter.CTkFont('Century Gothic',45)

#Functions
def Time():
    current_time = ''
    new_time = time.strftime('%H:%M:%S')
    if current_time != new_time:
        current_time=new_time
        time_lbl.configure(text=new_time)
    time_lbl.after(200,Time)    

def Date():
    current_date = date.today()
    current_date = current_date.strftime("%d %B %Y")
    date_lbl.configure(text=current_date)

def check_box():
    var_a = check_box_nutrition_a.get()
    var_b = check_box_nutrition_b.get() 
    if var_a == 'nutrition_a_on' and var_b == 'nutrition_b_on':
        save_button_nutrition.configure(state='normal')
    else:
        save_button_nutrition.configure(state='disabled')

def save_to_file():
   with open ('date.txt','w') as write_file:
       for key , value in date_data_dictionary.items():
           write_file.write('%s :  %s\n'%(key , value))
       write_file.close()    
    
def load_dates():
    global date_data_dictionary
    file_presence = str(path.exists('date.txt'))
    if file_presence == 'True':
       with open('date.txt','r') as read_file:
           date_data=read_file.read()
           read_file.close()
       info_display_text.configure(state='normal')
       info_display_text.delete("0.0", "end")
       info_display_text.insert('0.0', date_data)
       info_display_text.configure(state='disabled')
       alert_and_remainingdays()
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
       date_data_dictionary={'Initaial Date':first_day,
                       'First Week':first_week_date,
                       'Second Week':second_week_date,
                       'Third Week':third_week_date,
                       'Fourth Week':fourth_week_date}
       save_to_file()
       updating_date_in_tracker_frame()
       moving_tracker()
       alert_and_remainingdays()
       with open('date.txt','r') as read_file:
           date_data=read_file.read()
           read_file.close()
       info_display_text.configure(state='normal')
       info_display_text.delete("0.0", "end")
       info_display_text.insert('0.0', date_data)
       info_display_text.configure(state='disabled')
    
def refresh():
   if isinstance(check_box_nutrition_a,customtkinter.CTkCheckBox):
      check_box_nutrition_a.deselect()
      check_box_nutrition_a.configure(state='disabled')
   if isinstance(check_box_nutrition_b,customtkinter.CTkCheckBox):
      check_box_nutrition_b.deselect()
      check_box_nutrition_b.configure(state='disabled')
   if isinstance(week_one_rdbtn,customtkinter.CTkRadioButton):
      week_one_rdbtn.deselect()
   if isinstance(week_two_rdbtn,customtkinter.CTkRadioButton):
      week_two_rdbtn.deselect()
   if isinstance(week_three_rdbtn,customtkinter.CTkRadioButton):
      week_three_rdbtn.deselect()
   if isinstance(week_four_rdbtn,customtkinter.CTkRadioButton):
      week_four_rdbtn.deselect()
   if isinstance(info_display_text,customtkinter.CTkTextbox):
      info_display_text.configure(state='normal')
      info_display_text.delete("0.0", "end")
      info_display_text.configure(state='disabled')

def updating_date_in_tracker_frame():
   file_presence = str(path.exists('date.txt'))
   if file_presence == 'True':
       with open('date.txt','r') as read_file:
           date_data=read_file.read()
           date_data_list=date_data.splitlines()
           splited_date_initial=date_data_list[0].split()
           splited_date_first=date_data_list[1].split()
           splited_date_second=date_data_list[2].split()
           splited_date_third=date_data_list[3].split()
           splited_date_fourth=date_data_list[4].split()
           today_lbl.configure(text='• \n'+splited_date_initial[3])
           month_one_lbl.configure(text='• \n'+splited_date_first[3]) 
           month_two_lbl.configure(text='• \n'+splited_date_second[3]) 
           month_three_lbl.configure(text='• \n'+splited_date_third[3])  
           month_four_lbl.configure(text='• \n'+splited_date_fourth[3])
           read_file.close()

def show_info():
   messagebox.showinfo("Nutritional Information", "1.Choose the week \n 2.Next mark the added nutritions \n 3. Save ")

def enabling_check_box():
    check_box_nutrition_a.configure(state='normal')
    check_box_nutrition_b.configure(state='normal')

def alert_and_remainingdays():
    today=parse(str(date.today()))
    first_week=parse(splited_date_first[3])
    second_week=parse(str(splited_date_second[3]))
    third_week=parse(splited_date_third[3])
    fourth_week=parse(splited_date_fourth[3])
    days_remaining_firstweek=str((first_week-today).days)
    days_remaining_secondweek=str((second_week-today).days)
    days_remaining_thirdweek=str((third_week-today).days)
    days_remaining_fourthweek=str((fourth_week-today).days)
    daysleft_week_one_lbl.configure(text=days_remaining_firstweek+'\nDays Left')
    daysleft_week_two_lbl.configure(text=days_remaining_secondweek+'\nDays Left')
    daysleft_week_three_lbl.configure(text=days_remaining_thirdweek+'\nDays Left')
    daysleft_week_four_lbl.configure(text=days_remaining_fourthweek+'\nDays Left')

def moving_tracker():
    global splited_date_first,splited_date_second,splited_date_third,splited_date_fourth
    splited_date_first=StringVar()
    splited_date_second=StringVar()
    splited_date_third=StringVar()
    splited_date_fourth=StringVar()
    today = datetime.now()
    file_presence = str(path.exists('date.txt'))
    if file_presence == 'True':
        with open('date.txt','r') as read_file:
           date_data=read_file.read()
           date_data_list=date_data.splitlines()
           splited_date_first=date_data_list[1].split()
           splited_date_second=date_data_list[2].split()
           splited_date_third=date_data_list[3].split()
           splited_date_fourth=date_data_list[4].split()
           if splited_date_first[3] == today:
              tracker.set(0.25)
           if splited_date_second[3] == today:
               tracker.set(0.503)
           if splited_date_third[3] == today:
               tracker.set(0.755)
           if splited_date_fourth[3]==today:
               tracker.set(1) 

def info_display():
    info_display_text.configure(state='normal')
    info_display_text.configure(border_spacing=7)
    info_display_text.insert("0.0", "• 1.Select The Week \n • 2.Add Nutriants \n • 3.Save ")
    info_display_text.configure(state='disable')

#Date ,Time and mainheading Frame
date_time_frame=customtkinter.CTkFrame(master=root,width=1300,height=100,corner_radius=20,border_color='Green',border_width=2)
time_lbl = customtkinter.CTkLabel(master=date_time_frame, font=fcg30)
date_lbl = customtkinter.CTkLabel(master=date_time_frame, font=fcg30)
main_heading_lbl = customtkinter.CTkLabel(master=date_time_frame,text='Hydroponic System',font=fcg45,text_color='white')
date_time_frame.place(relx=0.5,rely=0.08,anchor=CENTER)
time_lbl.place(relx=0.03,rely=0.1)
date_lbl.place(relx=0.03,rely=0.5)
main_heading_lbl.place(relx=0.65,rely=0.27)
Time()
Date()

#Exit Button 
exit_button = customtkinter.CTkButton(master=root, text= "Exit", command=root.destroy,width=200,height=40,corner_radius=20,font=fcg20,
                                        hover_color='Red4')
exit_button.place(relx=0.9,rely=0.95,anchor=CENTER)

#Nutrition Frame
nutrition_frame=customtkinter.CTkFrame(master=root,width=450,height=300,corner_radius=20,border_color='Green',border_width=2)
top_label_nutrition=customtkinter.CTkLabel(master=nutrition_frame,text='Nutritional Information',font=('Century Gothic',30,UNDERLINE),
                                            text_color='Yellow')
nutrient_a_lbl=customtkinter.CTkLabel(master=nutrition_frame,text='Nutrient A (20ml)',font=fcg20,text_color='white')
nutrient_b_label=customtkinter.CTkLabel(master=nutrition_frame,text='Nutrient B (20ml)',font=fcg20,text_color='white')
info_display_text=customtkinter.CTkTextbox(master=nutrition_frame,width=300,height=110,state='disabled',corner_radius=5,border_width=2,font=fcg15)
check_box_nutrition_a=customtkinter.CTkCheckBox(master=nutrition_frame,text=' ',onvalue='nutrition_a_on',offvalue='nutrition_a_off',
                                                command=check_box,font=fcg20,state='disabled')
check_box_nutrition_b=customtkinter.CTkCheckBox(master=nutrition_frame,text=' ',onvalue='nutrition_b_on',offvalue='nutrition_b_off',
                                                command=check_box,font=fcg20,state='disabled')
save_button_nutrition=customtkinter.CTkButton(master=nutrition_frame,text='Save',width=120,height=30,corner_radius=20,font=fcg20,state='disabled',
                                              command=load_dates)
reset_button=customtkinter.CTkButton(master=nutrition_frame,text='Clear All',width=50,height=20,command=refresh,fg_color='Red4',hover_color='Red4')
week_var= IntVar()
week_one_rdbtn=customtkinter.CTkRadioButton(master=nutrition_frame,text='Week One',variable=week_var,value=1,font=fcg15,command=enabling_check_box)
week_two_rdbtn=customtkinter.CTkRadioButton(master=nutrition_frame,text='Week Two',variable=week_var,value=2,font=fcg15,state='disabled')
week_three_rdbtn=customtkinter.CTkRadioButton(master=nutrition_frame,text='Week Three',variable=week_var,value=3,font=fcg15,state='disabled')
week_four_rdbtn=customtkinter.CTkRadioButton(master=nutrition_frame,text='Week Four',variable=week_var,value=4,font=fcg15,state='disabled')
show_info_btn=customtkinter.CTkButton(master=nutrition_frame,text='i',width=20,height=20,corner_radius=20,command=show_info,font=('Times',25,'italic'))
nutrition_frame.place(relx=0.18,rely=0.38,anchor=CENTER)
top_label_nutrition.place(relx=0.5,rely=0.1,anchor=CENTER)
nutrient_a_lbl.place(relx=0.25,rely=0.3,anchor=CENTER)
nutrient_b_label.place(relx=0.25,rely=0.43,anchor=CENTER)
check_box_nutrition_a.place(relx=0.6,rely=0.3,anchor=CENTER)
check_box_nutrition_b.place(relx=0.6,rely=0.43,anchor=CENTER)
save_button_nutrition.place(relx=0.83,rely=0.88,anchor=CENTER)
info_display_text.place(relx=0.02,rely=0.5)
reset_button.place(relx=0.05,rely=0.9)
week_one_rdbtn.place(relx=0.7,rely=0.25)
week_two_rdbtn.place(relx=0.7,rely=0.39)
week_three_rdbtn.place(relx=0.7,rely=0.53)
week_four_rdbtn.place(relx=0.7,rely=0.66)
show_info_btn.place(relx=0.9,rely=0.05)
info_display()

#Progress Bar
tracking_data_frame=customtkinter.CTkFrame(master=root,width=840,height=300,corner_radius=20,border_color='Green',border_width=2)
tracking_main_lbl=customtkinter.CTkLabel(master=tracking_data_frame,text='Progress',font=('Century Gothic',30,UNDERLINE),
                                            text_color='Yellow')
tracker=customtkinter.CTkProgressBar(master=tracking_data_frame,width=690,height=10,corner_radius=10,mode='determinate')
tracker.set(0)
today_lbl=customtkinter.CTkLabel(master=tracking_data_frame,text=' • \n Start',font=fcg20,text_color='white')
month_one_lbl=customtkinter.CTkLabel(master=tracking_data_frame,text=' • \n Week \n One',font=fcg20,text_color='white')
month_two_lbl=customtkinter.CTkLabel(master=tracking_data_frame,text='• \n Week \n Two',font=fcg20,text_color='white')
month_three_lbl=customtkinter.CTkLabel(master=tracking_data_frame,text='• \n Week \n Three',font=fcg20,text_color='white')
month_four_lbl=customtkinter.CTkLabel(master=tracking_data_frame,text='• \n Week \n Four',font=fcg20,text_color='white')
daysleft_week_one_lbl=customtkinter.CTkLabel(master=tracking_data_frame,text='',font=fcg20,text_color='white')
daysleft_week_two_lbl=customtkinter.CTkLabel(master=tracking_data_frame,text='',font=fcg20,text_color='white')
daysleft_week_three_lbl=customtkinter.CTkLabel(master=tracking_data_frame,text='',font=fcg20,text_color='white')
daysleft_week_four_lbl=customtkinter.CTkLabel(master=tracking_data_frame,text='',font=fcg20,text_color='white')
tracking_data_frame.place(relx=0.67,rely=0.38,anchor=CENTER)
tracker.place(relx=0.5,rely=0.3,anchor=CENTER)
tracking_main_lbl.place(relx=0.5,rely=0.1,anchor=CENTER)
today_lbl.place(relx=0.05,rely=0.35)
month_one_lbl.place(relx=0.25,rely=0.35)
month_two_lbl.place(relx=0.45,rely=0.35)
month_three_lbl.place(relx=0.65,rely=0.35)
month_four_lbl.place(relx=0.85,rely=0.35)
daysleft_week_one_lbl.place(relx=0.25,rely=0.7)
daysleft_week_two_lbl.place(relx=0.45,rely=0.7)
daysleft_week_three_lbl.place(relx=0.65,rely=0.7)
daysleft_week_four_lbl.place(relx=0.85,rely=0.7)
updating_date_in_tracker_frame()
moving_tracker()


#looping root
root.mainloop()