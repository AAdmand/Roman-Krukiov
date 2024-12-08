def parol(n):
    vseperemenn = {}
    vseperemenn.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
    vseperemenn.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
    vseperemenn.update({14: 1611325212343114105968, 15: 1214114232133124115106978})
    vseperemenn.update({16: 1317115262143531341251161079, 17: 11621531441351261171089})
    vseperemenn.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
    vseperemenn.update({20: 13141911923282183731746416515614713812911})
    passcode = vseperemenn.get(n)
    return passcode

n = int(input('введите переменную :'))

parnumers1 = list(range(1, n))
parnumers2 = list(range(1, n))
pars = []
result = ''

for i in parnumers1:
    for j in parnumers2:
        numer1 = i
        numer2 = j
        if numer1 >= numer2:
            continue
        else:
            kratno = n % (numer1 + numer2)
            if kratno == 0:
                pars.append([numer1, numer2])
                result = result + str(numer1) + str(numer2)
print('Пары чисел', *pars)
print('пароль', result)
