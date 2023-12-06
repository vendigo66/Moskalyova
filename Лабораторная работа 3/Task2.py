# TODO Напишите функцию find_common_participants


def find_common_participants(a, b, c=","):
    common = []
    for i in a.split(c):
        for j in b.split(c):
            if i==j:
                common.append(i)
    common.sort()
    return common
sep = '|'
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, sep))

# TODO Провеьте работу функции с разделителем отличным от запятой
