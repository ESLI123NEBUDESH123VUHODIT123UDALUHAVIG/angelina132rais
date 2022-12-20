from colorama import Fore, Back, Style
from colorama import init
init()
 
print(Style.BRIGHT) 
ls = [
    ("Солнце желтое?", "да"),
    ("Летом холодно?", "нет"),
    ("Ты выспался?", "нет"),
    ("Еще вопросы?", "нет")
]
print(Back.RESET) 
answers_counter = [0,0] 
print(Fore.GREEN) 
for q, a in ls:
    print(q, '[да/нет]' + Style.BRIGHT)
    answer = input().strip().lower()
    if answer == a:
        print("правильный ответ")
        answers_counter[0] += 1 
        answers_counter[1] += 1 
    else:
        print("неправильный ответ")
        answers_counter[0] += 1 
print(Style.RESET_ALL)
print("\nДано ответов: {}, Верных ответов: {}".format(answers_counter[0], answers_counter[1]))
input()
