# Функции
#
# def yell(text: str):
#     return  text.upper() +'!'

# shout = yell
# del yell
# print('shout', shout.__name__)
# print(yell('hello'))

def speak(volume):
    def whisper(text):
        return text.lower()
    def shout(text):
        return text.upper()
    if volume >5:
        return shout
    else:
        return whisper
# result = speak(4)
# print(result('hey, hgkjgggjhgj'))

def make_adder(x):
    def add(n):
        return x + n
    return add

plus_3 = make_adder(3)
print(plus_3(23))
print(plus_3(35))
print(plus_3(37))