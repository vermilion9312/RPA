# 엑셀 만들기
csv_file = open('data.csv', 'w')
csv_file.write('김,이,박')
csv_file.write('\n김,이,박')
csv_file.close()

# 숙제
my_list = ['삼성전자', '카카오', '네이버', '신풍제약']
homework = open('homework.txt', 'w')
for atom in my_list:
    homework.write('\n' + atom)
homework.close()

# gugudan
gugudan = open('gugudan.txt', 'w')
for i in range(2, 10):
    for j in range(1, 10):
        gugudan.write('\n' + str(i * j))
    gugudan.write('\n')
gugudan.close()