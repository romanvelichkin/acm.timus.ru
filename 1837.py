# 1837. Число Исенбаева

# число команд
teams_amount = int(input())
# список команд
teams_list = []
# список команд, предназначенных для удаления
teams_delete = []
# список участников
names_list = []
# список участников и их связь с Исенбаевым
names_dict = {}
# Сам Исенбаев
start_person = 'Isenbaev'

while teams_amount > 0:
    # состав команды
    team_string = input()

    # записываем все команды Исенбаева
    if start_person in team_string:

        # добавляем самого Исенбаева
        if start_person not in names_dict:
            names_list.append(start_person)
            names_dict[start_person] = 0

        team_string = team_string.split(' ')
        for x in team_string:
            # Добавляем членов команды Исенбаева
            # (проверяем - вдруг у Исинбаева есть одинаковые команды,
            # чтоб не попали дважды)
            if x != start_person and x not in names_dict:
                names_list.append(x)
                names_dict[x] = 1

    # отдельно сохраняем команды, где не было Исенбаева
    else:
        teams_list.append(team_string)

    teams_amount = teams_amount - 1

# степень связи участника с Исенбаевым
level = 1

while len(teams_list) > 0:
    names = [name for name, num in names_dict.items() if num == level]
    if len(names) > 0:
        for x in names:
            for y in teams_list:
                if x in y:
                    current_team = y.split(' ')
                    for z in current_team:
                        if z != x:
                            if z not in names_dict:
                                names_list.append(z)
                                names_dict[z] = level + 1

                    if y not in teams_delete:
                        teams_delete.append(y)

            for team in teams_delete:
                if team in teams_list:
                    teams_list.remove(team)
                teams_delete.remove(team)

        level = level + 1
    else:
        for y in teams_list:
            current_team = y.split(' ')
            for z in current_team:
                if z not in names_dict:
                    names_list.append(z)
                    names_dict[z] = 'undefined'

            if y not in teams_delete:
                teams_delete.append(y)

        for team in teams_delete:
            if team in teams_list:
                teams_list.remove(team)
            teams_delete.remove(team)

names_list.sort()
for x in names_list:
    # name_level = [num for name, num in names_dict.items() if name == x]
    # for y in name_level:
    #    print(x, y)
    print(x, list(names_dict.values())[list(names_dict.keys()).index(x)])
