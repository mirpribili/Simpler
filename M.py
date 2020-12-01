#вводится первый блок
classi = {}
vopros = []
otvet = []
if False:
    a = int(input())
    b = 0
    while b < a:
        c = input().split()
        vopros.append(c)
        b += 1
    print(vopros)
else:
    vopros = [['A'], ['B', ':', 'A'], ['C', ':', 'A'], ['D', ':', 'B', 'C']]


#print(vopros)
#заполнение словаря, вроде работает правильно
for i in vopros:
    if len(i) == 1:
        classi[i[0]] = []
    elif len(i) == 3:
        if i[2] in classi.keys():
            classi[i[2]] += i[0]
        else:
            classi[i[2]] = []
            classi[i[2]] += i[0]
    elif len(i) > 3:
        for j in range(2, len(i)):
            classi[i[j]] = i[0]

print("classi", classi)
#вводится второй блок
if False:
    a1 = int(input())
    b1 = 0
    while b1 < a1:
        c = input().split()
        otvet.append(c)
        b1 += 1
    #вывод результатов проверки
else:
    otvet = [['A', 'B'], ['B', 'D'], ['C', 'D'], ['D', 'A']]
print("otvet", otvet)

for i in otvet:
    print(i, "\t", end="")
    if i[0] in classi.keys() and i[1] in classi.values():
        print(i, 'Yes')
    #вот тут нужна помощь
    #я хочу перебрать в цикле значения, если ключ совпадает, а длина списка в значении больше 1
    #но он не выводит ответ, так что я видимо не так к ним обращаюсь
    #запрашиваю помощь!
    elif i[0] in classi.keys() and len(classi.values()) > 0:
        for j in classi.values():
            if i[1] == j:
                print('Yes')
            else:
                print(j)
    else:
        print('No')


    for parent in classi:
        if parent == i[0]:
            #print(parent)
            child = classi[parent]
            if i[1] in child:
                print("Yes")
#print(classi)