# Объявите функцию с именем get_data_fig для вычисления периметра произвольного N-угольника.
# На вход этой функции передаются N длин сторон через аргументы. Дополнительно могут быть указаны именованные аргументы:
#
# type - булево значение True/False
# color - целое числовое значение
# closed - булево значение True/False
# width - целое значение
#
# Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения именованных параметров
# в порядке их перечисления в тексте задания (если они были переданы).
# Если какой-либо параметр отсутствует, его возвращать не нужно (пропустить).

def get_data_fig(*args, **kwargs):
    lst_0 = ['type', 'color', 'closed', 'width'] # список для контроля порядка параметров
    lst_1 = []
    for i in range(len(lst_0)):
        if lst_0[i] not in kwargs:
            continue
        else:
            lst_1.append(kwargs[lst_0[i]])

    return (sum(args), ) + tuple(lst_1)


n = get_data_fig(1, 2, 3,  type = True,  closed = False, width = 7)

print(n)
