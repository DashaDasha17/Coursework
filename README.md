# Coursework
# Проверка установленного программного обеспечения
Выполняли: Попова Дарья (сканирование и запись), Петухова Инна (сравнение результатов), Теслева Елизавета (поиск)

### Запуск:
python3 soft_scanner.py

### Аргументы:
**-p, --print** ('t', 'f') - вывести список установленного ПО. По умолчанию 't' (да)

**-s, --save** ('t', 'f') - записать результат сканирования в файл. По умолчанию 'f' (нет)

**-f, --file** (<filename>) - выбрать название файла для записи и сравнения. 

**-c, --compare** ('t', 'f') - запустить сравнение списка текущих установленных программ с тем списком, который был записан в файл в последний раз. 

Если файла нет, выведется ошибка. По умолчанию 'f' (нет)

**-sr, --search** (<названия через пробел>) - запустить поиск ПО по выданным аргументам. 

**--full ('t', 'f')** - вывести все файлы с разрешением на исполнение. По умолчанию 'f' (нет)

### Пример запуска:
python3 soft_scanner.py -p f -s t -f 'ye.txt' -c t -sr python3-brlapi/focal,now 6.0+dfsg-4ubuntu6 nepiton

### Вывод:

Найдены следующие совпадения:

python3-brlapi/focal,now 6.0+dfsg-4ubuntu6 amd64 [установлен, автоматически]
brltty/focal,now 6.0+dfsg-4ubuntu6 amd64 [установлен, автоматически]
libbrlapi0.7/focal,now 6.0+dfsg-4ubuntu6 amd64 [установлен, автоматически]
python3-brlapi/focal,now 6.0+dfsg-4ubuntu6 amd64 [установлен, автоматически]
xbrlapi/focal,now 6.0+dfsg-4ubuntu6 amd64 [установлен, автоматически]

По следующим запросам совпадений не найдено:

nepiton

Новых программ не обнаружено

Удаления программ с прошлого сканирования не обнаружено
