import csv
import json
import time
from datetime import date, datetime
from os import path
from tkinter import PhotoImage, messagebox,Label

import customtkinter
import cv2
import numpy as np
import pandas as pd
import PIL.Image
import tensorflow as tf
from customtkinter import *
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from keras.models import load_model
from PIL import ImageTk
from tkcalendar import DateEntry

#Theme and apperance of main window
# customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#Main_window_Feature_managment
root = customtkinter.CTk()
root.title('Hydroponics')
root.minsize(1330,690)
root.maxsize(1330,690)
root.configure(background='AntiqueWhite1')
window_width = 1330
window_height = 690
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)-12
center_y = int(screen_height/2 - window_height / 2)
center_y_n = center_y - 35
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y_n}')


# background 
photo = PhotoImage('bg.jpg')
w = Label(root, image=photo)
w.pack()

#Fonts
fcg15=customtkinter.CTkFont('Century Gothic',15)
fcg17=customtkinter.CTkFont('Century Gothic',17)
fcg20=customtkinter.CTkFont('Century Gothic',20)
fcg30=customtkinter.CTkFont('Century Gothic',30)
fcg45=customtkinter.CTkFont('Century Gothic',45)
fcgbtn=customtkinter.CTkFont('Century Gothic',19,'bold')

# Machine Learning Model
model = load_model(os.path.join('models','model_2.h5'))

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

def tds_input_event():
    global input_from_dialog
    tds_input_dialog=customtkinter.CTkInputDialog(text="Enter The TDS Value (In Numbers):", title="TDS Value")
    try:
        input_from_dialog = int(tds_input_dialog.get_input())
        error_lbl_main.configure(text=" ") 
        if input_from_dialog <= 250:
            error_lbl_main.configure(text='TDS Value is Low',text_color='red')
        elif input_from_dialog > 250 and input_from_dialog < 300:
            error_lbl_main.configure(text='TDS Value has been saved',text_color='Green')
            create_csv_file()
            appending_tds_value()
        elif input_from_dialog > 300:
            error_lbl_main.configure(text='TDS Value is High',text_color='red')
    except ValueError:
        error_lbl_main.configure(text="Entered Value is Not an Integer. Please Try Again")          

def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

@run_once    
def create_csv_file():
    with open('TDS_Data.csv', 'w', encoding='UTF8', newline='') as csv_file:
        header = ['   Date   ','      Time   ', '        TDS value']
        writer = csv.writer(csv_file)
        writer.writerow(header)

def appending_tds_value():
    todays_date = datetime.today().strftime('%d-%m-%Y')
    current_time = datetime.now().strftime('%I:%M %p')
    data_to_add = pd.DataFrame({'Date':[todays_date] ,'    Time':[current_time],'TDS value' :[input_from_dialog]})
    data_to_add.to_csv('TDS_Data.csv',mode='a', index=False, header=False)

def current_date():
    todays_date=datetime.today().strftime('%d-%m-%Y')
    todays_date=parse(todays_date).date()
    week_calculator(todays_date)

def custom_date():
    custom_date=calendar_custom_date.get_date()
    week_calculator(custom_date)

def week_calculator(day_today):
    global date_data_dictionary
    week = relativedelta(days=+7)
    first_week = day_today + week
    second_week = first_week + week
    third_week = second_week + week
    fourth_week = third_week + week
    date_today = day_today.strftime('%d-%m-%Y')
    first_week = first_week.strftime('%d-%m-%Y')
    second_week = second_week.strftime('%d-%m-%Y')
    third_week = third_week.strftime('%d-%m-%Y')
    fourth_week = fourth_week.strftime('%d-%m-%Y')
    date_data_dictionary = {'Initial Date':date_today,
                             'First Week':first_week,
                              'Second Week':second_week,
                               'Third Week':third_week,
                                'Fourth Week':fourth_week}    
    who_called = sys._getframe(1).f_code.co_name
    if who_called == 'current_date':
        saving_curret_date()
    elif who_called == 'custom_date':
        saving_custom_date()

def saving_curret_date():
    presence_of_custom_file=path.exists('dd_custom.json')
    if presence_of_custom_file == True:
        cstm_msgbx=messagebox.askokcancel('Additional Files Found!', 'Are You sure you want to continue?\n Additional Files will be cleared !')
        if cstm_msgbx == True:
            os.remove('dd_custom.json')
    else :
     with open("dd_current.json", "w") as write_file:
                json.dump(date_data_dictionary, write_file)
                messagebox.showinfo('Saved','Your Data has been Saved ')

def saving_custom_date():
    presence_of_current_file = path.exists('dd_current.json')
    if presence_of_current_file == True:
        crnt_msgbx = messagebox.askokcancel('Additional Files Found!', 'Are You sure you want to continue?\n Additional Files will be cleared !')
        if crnt_msgbx == True:
            os.remove('dd_current.json')
    else:
     with open("dd_custom.json", "w") as write_file:
        json.dump(date_data_dictionary, write_file)
        messagebox.showinfo('Saved','Your Data has been Saved ')

def info_date():
    info_date = customtkinter.CTkToplevel(root)
    info_date.config(width=1000, height=500)
    info_date.title("Date Information")
    presence_of_custom_file=path.exists('dd_custom.json')
    presence_of_current_file=path.exists('dd_current.json')
    if presence_of_custom_file == True:
        with open("dd_custom.json", "r") as read_file:
            data = json.load(read_file)
            data=str(json.dumps(data))
            newdata = data.replace('"',' ').replace('}',' ').replace('{',' ').replace(',','\n ')
            infolbl=customtkinter.CTkLabel(master=info_date,text=newdata,width=600,height=170,corner_radius=2,font=fcg45)
            infolbl.place(relx=0.5,rely=0.5,anchor=CENTER)
    if presence_of_current_file == True:
        with open('dd_current.json','r') as read_file:
            data = json.load(read_file)
            data=str(json.dumps(data))
            newdata = data.replace('"',' ').replace('}',' ').replace('{',' ').replace(',','\n ')
            infolbl=customtkinter.CTkLabel(master=info_date,text=newdata,width=600,height=170,corner_radius=2,font=fcg45)
            infolbl.place(relx=0.5,rely=0.5,anchor=CENTER)
    info_date.focus()

def info_tds():
    info_tds = customtkinter.CTkToplevel(root)
    info_tds.config(width=1000, height=500)
    info_tds.minsize(1000,0)
    info_tds.maxsize(1000,500)
    info_tds.title("TDS Information")
    presence_of_csv_file = path.exists('TDS_Data.csv')
    if presence_of_csv_file == True:
        data =str(pd.read_csv('TDS_Data.csv'))
        infolbl = customtkinter.CTkLabel(master=info_tds,text=data,width=600,height=170,corner_radius=2,font=fcg20)
        infolbl.place(relx=0.5,rely=0.5,anchor=CENTER)

def select_image():
    global img
    file_position_var = filedialog.askopenfile(title="Select the Image With Supported Formats Only")
    try:
        file_path = file_position_var.name
        if len(file_path) != 0:
            display_info = 'Image Has Been Selected from :\n'+file_path
            messagebox.showinfo('Image Selected',display_info)
            image_input_frame.configure(border_color='Green')
            open_image=PIL.Image.open(file_path)
            resize_image=open_image.resize((350,350))
            display_image = ImageTk.PhotoImage(resize_image)
            image_input_label.configure(image=display_image)
            img = cv2.imread(file_path)
    except AttributeError:
        error_lbl_main.configure(text='No File Selected',text_color='Red')
        image_input_frame.configure(border_color='Red')

def predict():
    try:
        resize = tf.image.resize(img, (256,256))
        prediction=model.predict(np.expand_dims(resize/255, 0))
        max_value = np.argmax(prediction)
        if max_value == 0:
            result_frame_label.configure(text='No Leaf Detected in the Image')
        elif max_value == 1:
            result_frame_label.configure(text='The Leaf Appears To Be Dead')
        elif max_value == 2:
            result_frame_label.configure(text='The Leaf Appears To Be Diseased')
        elif max_value == 3:
            result_frame_label.configure(text='The Leaf Appears To Be a Normal Leaf')
        error_lbl_main.configure(text='Image Selected',text_color='Green')
        image_input_frame.configure(border_color='Green')
    except NameError:
        error_lbl_main.configure(text='No Image Selected. Select an Image and Try Again',text_color='red')
        image_input_frame.configure(border_color='Red')

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

#Nutrition Frame
nutrition_frame=customtkinter.CTkFrame(master=root,width=450,height=180,corner_radius=20,border_color='Green',border_width=2)
top_lbl_nutrition=customtkinter.CTkLabel(master=nutrition_frame,text='Date Selector',font=('Century Gothic',30,UNDERLINE),text_color='Yellow')
calendar_custom_date = DateEntry(master=nutrition_frame,selectmode = 'day',width=10,font=fcg15,date_pattern='dd/mm/yyyy')
custom_date_lbl=customtkinter.CTkLabel(master=nutrition_frame,text='Select a Custom Date :',font=fcg20,text_color='white')
save_custom_date_btn=customtkinter.CTkButton(master=nutrition_frame,text='Save Custom Date',width=180,height=50,corner_radius=20,font=fcgbtn,command=custom_date)
save_initial_date_btn=customtkinter.CTkButton(master=nutrition_frame,text='Save Current Date',width=180,height=50,corner_radius=20,font=fcgbtn,command=current_date)
nutrition_frame.place(relx=0.18,rely=0.3,anchor=CENTER)
top_lbl_nutrition.place(relx=0.5,rely=0.17,anchor=CENTER)
custom_date_lbl.place(relx=0.33,rely=0.42,anchor=CENTER)
calendar_custom_date.place(relx=0.75, rely=0.42,anchor=CENTER)
save_initial_date_btn.place(relx=0.26,rely=0.75,anchor=CENTER)
save_custom_date_btn.place(relx=0.74, rely=0.75,anchor=CENTER)

#TDS Value Frame 
tds_frame=customtkinter.CTkFrame(master=root,width=450,height=180,corner_radius=20,border_color='Green',border_width=2)
top_lbl_tds = customtkinter.CTkLabel(master=tds_frame,text='TDS Value',font=('Century Gothic',30,UNDERLINE),text_color='Yellow')
tds_lbl = customtkinter.CTkLabel(master=tds_frame,text="Mesure the TDS Value with a TDS Meter",font=fcg20,text_color='white')
tds_value_input_btn=customtkinter.CTkButton(master=tds_frame,text='Input Todays TDS Value',width=180,height=50,corner_radius=20,font=fcgbtn,command=tds_input_event)
tds_lbl.place(relx=0.5,rely=0.45,anchor=CENTER)
tds_value_input_btn.place(relx=0.5,rely=0.75,anchor=CENTER)
top_lbl_tds.place(relx=0.5,rely=0.17,anchor=CENTER)
tds_frame.place(relx=0.528,rely=0.3,anchor=CENTER)

#info frame
info_frame=customtkinter.CTkFrame(master=root,width=375,height=180,corner_radius=20,border_color='Green',border_width=2)
info_top_lbl=customtkinter.CTkLabel(master=info_frame,text='Information',font=('Century Gothic',30,UNDERLINE),text_color='Yellow')
show_date_data_btn=customtkinter.CTkButton(master=info_frame,text='View Date Data',width=220,height=45,corner_radius=20,font=fcgbtn,command=info_date)
show_tds_data_btn=customtkinter.CTkButton(master=info_frame,text='View TDS Data',width=220,height=45,corner_radius=20,font=fcgbtn,command=info_tds)
info_top_lbl.place(relx=0.5,rely=0.17,anchor=CENTER)
show_date_data_btn.place(relx=0.5,rely=0.5,anchor=CENTER)
show_tds_data_btn.place(relx=0.5,rely=0.8,anchor=CENTER)
info_frame.place(relx=0.85,rely=0.3,anchor=CENTER)

#image input frame
image_input_frame=customtkinter.CTkFrame(master=root,width=915,height=300,corner_radius=20,border_color='Green',border_width=2)
image_input_label= customtkinter.CTkLabel(master = image_input_frame,text=' ',width=425,height=280,corner_radius=20,
                                          font=fcg20,fg_color="gray21")
image_selection_button=customtkinter.CTkButton(master=image_input_frame,text='Select Image',width=200,height=40,corner_radius=20,
                                               font=fcgbtn,command=select_image)
predict_button=customtkinter.CTkButton(master=image_input_frame,text='Predict',width=200,height=40,corner_radius=20,font=fcgbtn,
                                       command=predict)
image_selection_button.place(relx=0.77,rely=0.4,anchor=CENTER)
predict_button.place(relx=0.77,rely=0.6,anchor=CENTER)
image_input_label.place(relx=0.25,rely=0.5,anchor=CENTER)
image_input_frame.place(relx=0.356,rely=0.67,anchor=CENTER)

#result output frame 
result_output_frame=customtkinter.CTkFrame(master=root,width=300,height=150,corner_radius=20,border_color='Green',border_width=2)
result_frame_label=customtkinter.CTkLabel(master=result_output_frame,text=' ',width=145,height=17,corner_radius=20,
                                          font=fcg15)
result_frame_label.place(relx=0.5,rely=0.5,anchor=CENTER)
result_output_frame.place(relx=0.85,rely=0.67,anchor=CENTER)

#Error Label
error_lbl_main=customtkinter.CTkLabel(master=root,text='',width=400,height=30,font=fcg20,text_color='Red')
error_lbl_main.place(relx=0.01,rely=0.94)

#Exit Button 
exit_button = customtkinter.CTkButton(master=root, text= "Exit", command=root.destroy,width=200,height=40,corner_radius=20,font=fcgbtn,
                                      hover_color='Red4')
exit_button.place(relx=0.88,rely=0.93,anchor=CENTER)

#looping root
root.mainloop()