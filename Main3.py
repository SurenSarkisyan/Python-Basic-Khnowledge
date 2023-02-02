
# Comments Условные операторы в Pyton

# == - символ присваивания
# != - символ неравенства двух значений
# if isHappy == True: - одно и тоже что прописать - if isHappy:
# if not isHappy: - одно и тоже что - if isHappy == False:
# else - всегда записывается в конце оператора if
# elif - всегда записывается между опреаторами if и else
# elif - дополнительное условие в теле условия
# and  -  оператор означает что оба условия должны быть True
# or - оператор означает что хотя бы одна из частей должна быть True тогда код сработает

# Тернарный оператор - тот же самый if else только в одну строку удобен для конструкций
#                      где есть только if и else

#                      data = input()
# Тернарный оператор - number = 5 if data == "Five" else 0

# Example 1

user_data = int(input("Введите число: "))

isHappy = False

if isHappy or user_data == 7 or user_data > 10:
    print("User is Happy")
elif user_data == 5:
    print("Number is 5")
elif user_data == 7:
    print("Number is 7")
else:
    print("User is unhappy")

# Example 2

user_data = int(input("Введите число: "))

if user_data != 5:
    print ("Done")
    if user_data > 6:
        print ("Number is bigger than 5")

#Example 3 - Тернарный оператор

data = input()

number = 5 if data == "Five" else 0

# Example 4

data = input()

if data == "Five":
    number = 5
else:
    number = 0

print(number)   # При вводе Five будет произведен print с переменной number
                # в которое есть вхождение 5 если же не отработает условие
                # будет выведено условие else равное 0