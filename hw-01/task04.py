"""
Задача 4
Песенка "Курочка по зёрнышку" (Im Radio ist ein Kucken).
С помощью этой песенки маленьких детей учат рекурсии :Ну а мы потренируемся писать вложенные циклы.
    Бабушка, бабушка, купим курочку!
    Бабушка, бабушка, купим курочку!
    Курочка по зёрнышку кудах-тах-тах.
    Бабушка, бабушка, купим уточку! (2 раза)
    Уточка та-ти-та-та,
    Курочка по зёрнышку кудах-тах-тах.
Далее персонажи такие:
...индюшонка - Индюшонок фалды-балды,
...кисоньку - А кисуня мяу-мяу,
...собачонку - Собачонка гав-гав,
...коровёнку - Коровёнка муки-муки,
...поросёнка - Поросёнок хрюки-хрюки,
и заканчивается всё последним куплетом:
    Бабушка, бабушка, купим телевизор! (2 раза)
    Телевизор надо, надо, ведь у нас такое стадо!
Примечание. "(2 раза)" - это два раза повторить одну строку.
Напишите программу, которая генерирует текст песенки.
Здесь может потребоваться подстановка строк. Действительно, не всегда бывает удобно собирать строку из кусочков, а тем более, выводить строку по кусочкам.
Для этого используйте любой способ для форматирования строк, который вам удобен.
Также уделите внимание вот какому аспекту.
Эта народная потешка имеет много вариаций, начиная со списка участников, и заканчивая языком (русским, немецким, каким угодно).
Поэтому ваша задача - написать такой код, который как можно проще переделывается под новую вариацию.
Вынесите все данные в отдельное место в программе, чтобы при изменениях текста песни не пришлось выискивать строки, разбросанные по коду.
"""
sounds = {'курочку!':'Курочка по зёрнышку кудах-тах-тах.',
          'уточку!':'Уточка та-ти-та-та,',
          'индюшонка!':'Индюшонок фалды-балды,',
          'кисоньку!':'А кисюня мяу-мяу,',
          'собачонку!':'Собачонка гав-гав,',
          'коровёнку!':'Коровёнка муки-муки,',
          'поросёнка!':'Поросёнок хрюки-хрюки,',
          'телевизор!':'Телевизор надо, надо, ведь у нас такое стадо!'}

character = ['курочку!', 'уточку!', 'индюшонка!', 'кисоньку!', 'собачонку!',
             'коровёнку!', 'поросёнка!', 'телевизор!']

main = 'Бабушка, бабушка, купим'

new = ['']

def song():
  for character in sounds:
    print(main, character)
    print(main, character)
    print(sounds.get(character))
    if sounds.get(character) == 'Телевизор надо, надо, ведь у нас такое стадо!':
      break
    for x in new:
      print(x)
    if sounds.get(character) != 'Телевизор надо, надо, ведь у нас такое стадо!':
      new.insert(0, sounds.get(character))

song()