#создать словарь из списка
lst_in = ['Пушкин: Сказака о рыбаке и рыбке', 'Есенин: Письмо к женщине', 'Тургенев: Муму', 'Пушкин: Евгений Онегин', 'Есенин: Русь']
lst_tuple = [x.split(': ') for x in lst_in]
d = {}
for i in range(len(lst_tuple)):
    if lst_tuple[i][0] not in d:
        d[lst_tuple[i][0]] = set([lst_tuple[i][1]])
    else:
        d[lst_tuple[i][0]].add( lst_tuple[i][1])

print(d)