# datetime

import datetime
from datetime import  timedelta



# date_2 = datetime.date(2022, 5, 25)
# time_2 = datetime.time(13, 30)
# all_date = datetime.datetime.combine(date_2, time_2)  #Объединение
#
# print(now.strftime("%a"))
# print(now.strftime("%A"))   # Вывести текущий день

# print(time_2)

# new_time = now.date() - date_2
# print(now.time())
# print(now.date())
# print(new_time)

# К нашей текущей дате прибавили 30 дней
# now = datetime.datetime.now()
# days = 30
# end_date = now + timedelta(days)
# print(end_date)

# now = datetime.date(2022, 6, 22)
# etap1 = now + timedelta(30)
# print(etap1)
# etap2 = etap1 + timedelta(20)
# print(etap2)
# etap3 = etap2 + timedelta(50)
# print(etap3)

# year = int(input('Year: '))
# month = int(input('month: '))
# day = int(input('day: '))
# data = datetime.datetime(year, month, day)
#
# def devide_time(date):
#     stage1 = date + timedelta(30)
#     stage2 = stage1 + timedelta(20)
#     stage3 = stage2 + timedelta(50)
#     print(f'{stage1} конец первого этапа!')
#     print(f'{stage2} конец второго этапа!')
#     print(f'{stage3} Защита!')
#     return  stage1, stage2, stage3
#
# devide_time(data)


#Взяли товар на какое то время
# ----------------------------------------------------------------
# lists = ['ps4', 'dota', 'll', 'warkraft']
#
# def devide_time(sutki, product_item):
#     now = datetime.datetime.now()
#     item_time = now + timedelta(sutki)
#     print(f'{product_item} должны возвратить {item_time}')
#
#     return {
#         f'{product_item}': item_time
#     }
#
# a = devide_time(2, lists[0])
# -------------------------------------------------------------------------

# Дата без секунд

# now = datetime.datetime.now()
# print(now.strftime('%Y-%m-%d %H:%M'))

#Дата пришла строкой. Переводим её в дату

# dt_string = "12/11/2018 09:15:32"
# print(type(dt_string))
# dt_object1 = datetime.datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
# print(type(dt_object1))
# # print("dt_object1 =", dt_object1)




# Перевод секунд в дату
# timestamp = 1545730073
# dt_object = datetime.datetime.fromtimestamp((timestamp))
# print(dt_object)