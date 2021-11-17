# Filler
Игра "Филлер"
В данную игру можно играть вдвоём или против компьютера.
Игра проходит на поле, состоящем из клеток нескольких разных цветов.
В начале игры клетки раскрашены случайным образом.
Каждый игрок начинает игру со своей стартовой клетки, находящейся на краю поля.
На каждом ходу игрок изменяет цвет стартовой клетки на любой другой из имеющихся — при этом все клетки,
примыкающие к стартовой по стороне и окрашенные в тот же цвет, также перекрашиваются в выбранный цвет.
Таким образом игрок захватывает соседние клетки, перекрашивая свою область в цвет этих клеток.
Игрок не может выбрать цвет, которым на этом ходу окрашена область противника.
Игрок побеждает если захватил более половины клеток игрового поля.

ссылка на оригинал: https://glukkazan.github.io/control/filler-40x20.htm?selector=0

ТЗ
1.Реализовать выбор двух режимов игры: одиночный (игрок VS ии) и для двух игроков
2.Реализовать 2 таблицы рекордов (между двумя игроками и между первым игроком и ии (в таблицах рекордов высвечивается кол-во побед)) с использованием базы данных
3.Реализовать выбор типа заполнения поля для игры: с использованием предустановленных цветов и с помощью файлов в формате jpeg или png, имеющих формат 1:1
4.Реализовать возможность настройки предустановвленных цветов(если успею)
5.Реализовать возможность выбора файлов для заполнения поля(если успею)
6.Реализовать перекрашивание цветов на поле во время процесса игры с помощью кнопок внизу формы
