#1

s = 'Sementsov Anton Sergeevich'
for index, letter in enumerate(s):
    print (letter)

#2
print('1 Euro = 1.17 Dollar')
dollar = int(input('Введите количество $ для перевода в Euro \n'))
def convert (dollar):
    amount = (1/1.17)*dollar
    amount = round(amount,2)
    return amount
print(convert(dollar))


