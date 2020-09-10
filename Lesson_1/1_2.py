sec = int(input('Введите кол-во секунд: '))
hour = sec // 3600
minute = (sec - hour * 3600) // 60
sec = sec % 60 % 60 

# Решение через форматирование
print(f'{hour:02.0f}:{minute:02.0f}:{sec:02.0f}')

# Решение через проверки
# if hour < 10:
#     hour = '0' + str(hour)
# if minute < 10:
#     minute = '0' + str(minute)
# if sec < 10:
#     sec = '0' + str(sec)
# print(f'{hour}:{minute}:{sec}')