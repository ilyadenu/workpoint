# Моделирование работы оптической схемы для измерения дрейфа фазы сигнала

Схема находится в папке 'pictures'.

Элементы схемы:

ГПН – генератор пилообразного напряжения, Л – непрерывный п\п лазер, ЭОМ – электрооптический модулятор, ФП – фотоприемник, ОСЦ – осциллограф.

# Склонировать проект с репозитория https://github.com/ilyadenu/workpoint

git clone https://github.com/ilyadenu/workpoint.git

# Установка зависимостей 

Для работы проекта, нужно локально установить необходимые пакеты:

poetry install

# В папке 'measurements' лежат файлы с измерениями, полученные с помощью осциллографа

Их можно поделить на группы по времени измерения. Первыми были сделаны измерения с 1 по 5, затем с 30 по 35 и последние с 52 по 59.
Так же измерения отличаются по уровню стабильности. Порядок повышения стабильности такой же, как и по времени измерений.
Графики строятся в основном по самым стабильным измерениям(52-59).

# Выбор нужного измерения

Все графики сделаны для одного конкретного измерения. Как таковой необходимости в смене измерения нет. 
Но если нужно, то для этого необходимо менять индексы в экземплярах класса, отдельно в каждом файле. 

# Графики

Графики лежат в папке 'pictures'. Для того чтобы посмотреть весь набор, нужно в файле 'main.py' раскомментировать нужный метод:

- main.init_cond_plot - отвечает за построение графиков полученных из начальных условий:
  - 1 - начальные условия. График показывает, как зависят сигнал фотоприемника и сигнал пилообразного напряжения от времени.
  - 2 - зависимость сигнала фотоприемника от сигнала пилы. Выделяется некоторый участок, для выбора рабочей точки
  - 3 - сигнал стандарта частоты. Параметры подбираются исходя из графика полученного выше.

- main.approximation_plots - отвечает за построение графиков полученных с помощью аппроксимации:
  - 1 - аппроксимирование зависимости сигнала фотоприемника от сигнала пилы. Выполняется для получения аналитической зависимости.
  - 2 - сигнал стандарта частоты после модулятора.

- main.filtration_plots - отвечает за построение графиков полученных с помощью преобразований Фурье и фильтраций:
  - 1 - гармоники. На полученном спектре сигнала можно наблюдать 3 гармоники, 2 из которых впоследствии обрезаются.
  - 2 - очищенный сигнал. Сигнал прошедший фильтр и очищенный от лишних гармоник.

- main.phase_shift_plots - отвечает за построение графиков сдвига фазы при изменении рабочей точки

# Изменение рабочей точки

Для того чтобы менять рабочую точку, необходимо перейти в файл 'sinus_definition'. Найти метод 'u_params_calc' и в нем менять значения знаменателей u0 и um.

