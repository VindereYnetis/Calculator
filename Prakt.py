x = float(input("Введите первое число: "))
Actions = int(input ("Сколько раз вы хотит произвести действие: "))
if (Actions >= 1):
    print ("Возможные действия: \nСложение: + \nВычитание: - \nДеление: / \nУмножение * \nВозведение в степень: **")
    i = 0
    for i in range(Actions):
        Action = input("Выберите действие: ")
        y = float(input("Введите второе число: "))
        if (Action == "+" or Action == "-" or Action == "/" or Action == "*" or Action == "**"):
            if (Action == "+"):
                x += y
                print (f"Промежуточное значение: {x}")
            if (Action == "-"):
                x = x - y
                print (f"Промежуточное значение: {x}")
            if (Action == "/"):
                if (y == 0):
                    print("Деление на 0 невозможно")
                else:
                    x = x / y
                    print (f"Промежуточное значение: {x}")
            if (Action == "*"):
                x = x * y
                print (f"Промежуточное значение: {x}")
            if (Action == "**"):
                x = x ** y
                print (f"Промежуточное значение: {x}")
        else: 
            print("Ошибка, введите корректное действие.")
    print (f"Итоговое значение: {x}")
else: print (f"Итоговое значение: {x}")