
#fizz-buss

# def fb(n):
#     while n % 3 == 0 and n % 5 == 0:
#         return f'fizzbuzz, {n} é divisível por 3 e 5'
#     if n % 5 == 0:
#         return f'buzz, {n} é divisível por 5'
#     if n % 3 == 0:
#         return f'fizz, {n} é divisível por 3'
#     return f'{n} não corresponde.'


    

# print(fb(int(input('Digite um número: '))))


# from random import randint

# for i in range(100):
#     aleatorio = randint(0,100)
#     print(fb(aleatorio))


print('\t ------ Tabuada ----- ')

num = int(input('Informe o número para ver a Tabuada: '))

print('\nTabuada de', num,':')

for i in range(1,11):
    print(num, 'x', i, '=',(num * i))