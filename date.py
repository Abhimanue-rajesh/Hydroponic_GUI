# import calendar
# # PYCON_DATE = datetime(year=2023, month=1, day=7, hour=1)
# # countdown = PYCON_DATE + datetime.now()
# # print(f"Countdown to PyCon US 2021: {countdown}")


# # tc= calendar.TextCalendar(firstweekday=5)
# # print(tc.formatmonth(2016, 5))
# # for x in tc.iterweekdays():
# #     print(x)

# # cal = calendar.monthcalendar(2023,month=1)
# # print(cal)

# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# import time 
# import pickle





# def storeing_data():
#     t_and_d=time.localtime()
#     current_year  = t_and_d.tm_year
#     current_month = t_and_d.tm_mon
#     current_day   = t_and_d.tm_mday
#     current_min   = t_and_d.tm_min
#     data_base = {}
#     data_base[0]=current_year
#     data_base[1]=current_month
#     data_base[2]=current_day
#     data_base[3]=current_min
#     data_base_file=open('d_&_t','ab')
#     pickle.dump(data_base,data_base_file)
#     data_base_file.close

# def loading_data():
#     data_base_file=open('d_&_t','rb')
#     data_base=pickle.load(data_base_file)
#     print(data_base)
#     for keys in data_base:
#         print(keys, '=>', data_base[keys])
#     data_base_file.close

import dill

dill.load_session('test.pkl')
print(a)

import pickle
from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()
print(now)
week = relativedelta(days=+7)
first_week = now+week
print(first_week)
second_week = first_week+week 
print(second_week)
third_week= second_week+week
print(third_week)
fourth_week=third_week+week
print(fourth_week) 

first_week_strg = pickle.dumps(first_week)