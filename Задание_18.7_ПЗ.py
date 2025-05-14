import random
# Список учеников

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()

# Список предметов

classes = ['Математика', 'Русский язык', 'Информатика']
classes.sort()

# пустой словарь с оценками по каждому ученику и предмету заполянем через цикл

students_marks = {}

for student in students:
    students_marks[student] = {}
    for class_ in classes:
        mark = [random.randint(1, 5) for _ in range(5)]
        students_marks[student][class_] = mark

# Рабочий цикл программы
while True:
    print("Список команд:")
    print("1. Добавить оценки ученика по предмету")
    print("2. Вывести средний балл по всем предметам по каждому ученику")
    print("3. Вывести все оценки по всем ученикам")
    print("4. Редактирование оценок")
    print("5. Редактировать данные по предмету")
    print("6. Редактировать данные по ученикам")
    print("7. Информация по всем оценкам для определенного ученика")
    print("8. Информация по ученику и предмету")
    print("9. Список все студентов или предметов")
    print("10. Анализ успеваемости")
    print("11. Выход из программы")
    a = input('Введите номер команды: ')

    #**************************************************
    # Добавляем оценку ученику
    if a == '1':
        print('1. Добавить оценку ученика по предмету')

        # считываем имя ученика
        student = input('Введите имя ученика: ')

        # считываем название предмета
        class_ = input('Введите предмет: ')

        # считываем оценку
        mark = int(input('Введите оценку: '))

        # Проверка введенных данных
        if student in students_marks:
            if class_ in students_marks[student]:
                # добавляем новую оценку для ученика по предмету
                students_marks[student][class_].append(mark)
                print(f"Для {student} по предмету {class_} добавлена оценка {mark}")
            else:
                print('Неверно введено название предмета')
        # если данные введены неверно
        else:
            print('Неверно введено имя ученика')

    # **************************************************
    # Выводим средний балл
    elif a == '2':
        print('Вывести средний балл по всем предметам по каждому ученику')

        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                if marks_count == 0:
                    marks_avg = 0
                    print(f"Предмет: {class_}, Всего оценок: {marks_count}, Средний балл:  {marks_avg}")
                else:
                    marks_avg = marks_sum / len(students_marks[student][class_])
                    print(f"Предмет: {class_}, Всего оценок: {marks_count}, Средний балл:  {marks_avg}")

    # **************************************************
    # Выводим все оценки по всем ученикам
    elif a == '3':
        for student in students:
            print(f"Студент: {student}")
            for class_ in classes:
                print(f"\tПредмет: {class_,}, Оценки: {students_marks[student][class_]}")
            print()
            print("*********************************************************************")
            print()

    # **************************************************
    # Редактировать данные по оценкам

    elif a == '4':

        student = input('Введите имя студента: ')

        if student not in students_marks:
            print("Студент не найден")

        else:
            class_ = input('Введите название предмета: ')
            if class_ in students_marks[student]:
                print("Выберете действие: ")
                print("1. Удалить все оценки.")
                print("2. Удалить оценку")
                print("3. Редактировать список оценок")
                a = input('Введите номер команды: ')

                if a == '1':
                    students_marks[student][class_].clear()
                    print("Оценки удалены")
                    print(f"{student}, Предемет: {class_}")
                    print(f"Список оценок: {students_marks[student][class_]}")

                elif a == '2':
                    print(f"{student}, Предемет: {class_}")
                    print(f"Список оценок: {students_marks[student][class_]}")
                    a = int(input('Введите оценку которую хотите удалить: '))
                    if a in students_marks[student][class_]:
                        students_marks[student][class_].remove(a)
                        print("Оценка удалена")
                        print(f"{student}, Предемет: {class_}")
                        print(f"Список оценок: {students_marks[student][class_]}")
                    else:
                        print("Введенная оценка не найдена")

                elif a == '3':
                    print(f"{student}, Предемет: {class_}")
                    print(f"Список оценок: {students_marks[student][class_]}")
                    marks_ = []
                    i = 1
                    while True:

                        a = int(input(f'Введите оценку № {i}, для выхода введите 0: '))
                        if 0 < a < 6:
                            marks_.append(a)
                            students_marks[student][class_] = marks_
                            i += 1
                            print(f"{student}, Предемет: {class_}")
                            print(f"Скорректированный список оценок: {students_marks[student][class_]}")
                        elif a == 0:
                            break
                        else:
                            print("ОШИБКА! Введите оценку от 1 до 5")

            else:
                print("Предмет не найден")

    # **************************************************
    # Редактировать предметы

    elif a == '5':
        print("Редактирование по предметам:")
        print("1. Добавить новый предмет")
        print("2. Переименовать существующий предмет")
        print("3. Удалить предмет")
        a = int(input("Введите номер команды: "))
        # Добавить новый предмет
        if a == 1:
            new_class_ = input("Введите название предмета: ")
            if new_class_ not in students_marks[student]:
                classes.append(new_class_)
                for student in students_marks:
                    students_marks[student][new_class_] = []
                print(f"Предмет {new_class_} добавлен в список предметов")
                print("Обновленный список предметов:")
                for class_ in classes:
                    print(class_)

            else:
                print(f"Предмет {new_class_} уже есть в списке предметов")

        # Изменить название предмета
        elif a == 2:
            _class_ = input("Введите название редактируемого предмета: ")

            if _class_ not in students_marks[student]:
                print(f"Предмет {_class_} отсутствует в списке предметов")

            else:
                new_class_ = input("Введите новое название предмета: ")
                classes.remove(_class_)
                classes.append(new_class_)
                for student in students_marks:
                    students_marks[student][new_class_] = students_marks[student][_class_]
                    del students_marks[student][_class_]
                print("Обновленный список предметов:")
                for class_ in classes:
                    print(class_)


        # Удалить предмет
        elif a == 3:
            _class_ = input("Введите название удаляемого предмета: ")

            if _class_ not in students_marks[student]:
                print(f"Предмет {_class_} отсутствует в списке предметов")

            else:
                classes.remove(_class_)
                for student in students_marks:
                    del students_marks[student][_class_]
                print(f"Предмет {_class_} удален. \nОбновленный список предметов:")
                for class_ in classes:
                    print(class_)

    # **************************************************
    # Редактировать данные по ученикам
    elif a == "6":
        print("Редактирование учеников:")
        print("1. Добавить нового ученика")
        print("2. Переименовать ученика")
        print("3. Удалить ученика")
        a = int(input("Введите номер команды: "))

        # Добавить ученика
        if a == 1:

            print("1. Добавить нового ученика")
            new_name = input("Введите имя нового ученика: ")
            if new_name not in students_marks:
                students.append(new_name)
                students_marks[new_name] = {}
                for class_ in classes:
                    marks = []
                    students_marks[new_name][class_] = marks
                print(f"Студент {new_name} добавлен в список. \nАктульный списол студентов:")
                for student in students:
                    print(student)


            else:
                print("Студент уже числится в списке")

        # Переименовать ученика
        elif a == 2:
            print("2. Переименовать ученика")
            old_name = input("Введите имя ученика для изменения: ")
            if old_name not in students_marks:
                print("Ученик не найден")

            else:
                new_name = input("Введите новое имя ученика: ")
                students.append(new_name)
                students.remove(old_name)
                students_marks[new_name] = students_marks[old_name]
                students_marks.pop(old_name)
                print(f"Студент {old_name} переименована в {new_name}")

        # Удалить ученика
        elif a == 3:
            print("3. Удалить ученика")
            name = input("Введите имя ученика для удаления: ")
            if name not in students_marks:
                print("Ученик не найден")
            else:
                students.remove(name)
                students_marks.pop(name)

            print("Актуальный список студентов: ")
            for student in students_marks:
                print(student)

    # **************************************************
    # Информация по всем оценкам для конкретного ученика

    elif a == "7":
        print("7. Информация по всем оценкам для определенного ученика")

        name = input("Введите имя ученика: ")
        if name not in students_marks:
            print("Ученик не найден")


        else:

            print("***********************************************")

            print(name)

            print()

            for class_ in students_marks[name]:

                marks = students_marks[name][class_]

                if len(marks) == 0:

                    avg = 0

                    print(f"Предмет: {class_}, Оценки: {marks}")

                    print(f"Средний балл по предмету {class_}: {avg}")

                    print("***********************************************")

                else:

                    avg = sum(marks) / len(marks)

                    print(f"Предмет: {class_}, Оценки: {marks}")

                    print(f"Средний балл по предмету {class_}: {avg}")

                    print("***********************************************")

    # **************************************************
    #Информация по ученику и предмету

    elif a == "8":
        print("8. Информация по ученику и предмету")
        student = input('Введите имя студента: ')
        if student not in students_marks:
            print('Студент не найден')
        else:
            class_ = input('Введите название предмета: ')
            if class_ not in students_marks[student]:
                print('Неверное название предмета, \n '
                      'сверьтесь с списком предметов:')
                for j in students_marks[student]:
                    print(j)
            else:

                marks = students_marks[student][class_]

                if len(marks) == 0:
                    avg = 0
                    print("***********************************************")
                    print(student)
                    print()
                    print(f"Предмет {class_}, Оценки: {marks}")
                    print(f"Средний балл по предмету: {avg}")
                    print()
                    print("***********************************************")

                else:

                    avg = sum(marks) / len(marks)
                    print("***********************************************")
                    print(student)
                    print()
                    print(f"Предмет {class_}, Оценки: {marks}")
                    print(f"Средний балл по предмету: {avg}")
                    print()
                    print("***********************************************")

    # **************************************************
    # Списки всех предметов и учеников

    elif a == "9":
        print("9. Список все студентов или предметов")
        print("1. Показать список всех студентов")
        print("2. Показать список всех предметов")
        a = int(input("Введите номер команды: "))

        # Список студентов
        if a == 1:
            print("***********************************************")
            print("Список студентов: ")
            for student in students_marks:
                print(student)
            print()
            print("***********************************************")

        # Список предметов
        elif a == 2:
            print("***********************************************")
            print("Список предметов: ")
            for class_ in students_marks[student]:
                print(class_)
            print()
            print("***********************************************")

        else:
            print("Неверная команда")

    # **************************************************
    # Анализ успеваемости, выводим студентов и предметы
    # средний бал по которым меньше 3.

    elif a == "10":
        print("10. Анализ успеваемости")

        for student in students_marks:
            for class_ in students_marks[student]:
                marks = students_marks[student][class_]
                if len(marks) == 0:
                    avg = 0
                else:
                    avg = sum(marks) / len(marks)

                if avg < 3:
                    print(f" Студент {student}")
                    print("Низкая успеваемость.")
                    print(f"Средний балл по предмету {class_} равен {avg} баллов. ")
                    print("***********************************************")



    else:
        break

