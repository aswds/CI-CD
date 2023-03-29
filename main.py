with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    # зчитування вмісту файлів
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()

#Перевіряємо чи у сетів є перетинів у словах
same_lines = set(file1_lines).intersection(file2_lines)

#Перевіряємо чи у сетів немає перетинів у словах
diff_lines = set(file1_lines).symmetric_difference(file2_lines)