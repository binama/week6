# ООП
# st = ''
# print(dir(st))

# class ItSchool:
#     bootcamp = 15000
#     time = '8:30'

# kunduz = ItSchool()
# yaser = ItSchool()
# aliya = ItSchool()
# print(ItSchool.__dict__)
# yaser.bootcamp = 12000
# yaser.free = True
# print(yaser.__dict__)
# print()
# print(aliya.__dict__)

# class CarCarolla:
#     kolesa = 4
#     ob_em = 1.8
#     dvigatel = 'v6'
#     kuzov = 'sedan'
#
#     def __init__(self, bamper, color, otdelka):          # Метод называется конструктор
#         self.bamper = bamper
#         self.color = color
#         self.otdelka = otdelka
#
#     def get_info(self):
#         print(f'{self.bamper}, цвет машины: {self.color},'
#               f' отделка машины: {self.otdelka}')
#
#     def change_otdelka(self, new_otdelka):
#         self.otdelka = new_otdelka
#
#     def get_hello(self):
#         print('Hello world')
#
#
# mirlan = CarCarolla('m obves', 'white', 'alkantaro')
# # # andrei = CarCarolla('v obves', 'dark blue', 'krokodile')
# # mirlan.get_info()
# # mirlan.change_otdelka('alpaka')
# mirlan.get_hello()

lessons_timur = {
    'peremennie': 100,
    'loop': 87,
    'func': 58,
}
lessons_nasyikat = {
    'peremennie': 100,
    'loop': 90,
    'func': 79,
}
lessons_aliya = {
    'peremennie': 100,
    'loop': 78,
    'func': 98,
}
class Student:
    group = 'python_bootcamp 8:30'

    def __init__(self, full_name, age, phone_number, lesson):
        self.full_name = full_name
        self.age = age
        self.phone_number = phone_number
        self.lesson = lesson
        self.sredniy_bal = 0

    def get_info(self):
        print(f'Группа: {self.group} Зовут: {self.full_name} возраст: {self.age} '
              f' номер телефона: {self.phone_number} средний бал: {self.sredniy_bal}')



    def set_sredniy_bal(self):
        result = sum(self.lesson.values()) / len(self.lesson)
        self.sredniy_bal = round(result)

    def set_sredniy_bal2(self):                       #Вычисление среднего бала через цикл
        count = 0
        for i in self.lesson.values():
            count += i
        self.sredniy_bal = round(count/len(self.lesson))

timur = Student('Nasirdinov Timur', 18, '+99655443322', lessons_timur)
nasyikat = Student('Arzibaeva Nasyikat', 38, '+99655443311', lessons_nasyikat)
aliya = Student('Narynbekova Aliya', 21, '+99655443300', lessons_aliya)

# timur.get_info()
# timur.set_sredniy_bal()
# timur.get_info()
# nasyikat.get_info()
aliya.get_info()
aliya.set_sredniy_bal2()
aliya.get_info()