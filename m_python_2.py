words_per_card = 4

def ends(string):
    string2 = string.strip()
    if "." in string2:
        string2 = string2[0:len(string2) - 1]
    return string2

words = []
texts = []
text = []
exs = []
ex = []
ex_str =""

# получим объект файла
file1 = open("test_4a.txt", "r")

# считываем все строки
lines = file1.readlines()

# закрываем файл
file1.close

bufer = "###_"
# итерация по строкам
for counter, line in enumerate(lines):
    #
    #line = line.strip()
    #print(line)
    #print(line.find("#"))
    #
    if "#___" in line:
        #--------------------
        if "###_" not in bufer:
            exit("\nERROR\n!! #1 sting №" + str(counter+1))
        #--------------------
        #print(line[4:])
        if len(line)>5:
            words.append(ends(line[4:]))

    if "##__" in line:
        #--------------------
        if "##__" in bufer:
            exit("\nERROR\n!! #2 sting №" + str(counter+1))
        #--------------------
        texts.append(ends(line[4:]))

    if "###_" in line:
        #--------------------
        if "#___" in bufer:
            exit("\nERROR\n!! #3 sting №" + str(counter+1))
        #--------------------
        #print(line)
        exs.append(ends(line[4:]))

    bufer = line



    if "#___" not in line and "##__" not in line and "###_" not in line:
        exit("\nERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n " + str(counter+1))


import random
def func(string):
    while True:
        if string.endswith('.'):
            string = string[0:len(string) - 1]
        else:
            return string


#print(words)
#print(texts)
#print(exs)


#print( texts )
#print( a )

#print("--")


 
#print("--")
#exit("\n-= OK =-\n")
results = []

for i, word in enumerate(words):
    #print(i)
    result = temp =[]
    temp = texts[i].split()
    random.shuffle( temp )
    result.append(' '.join(temp))
    #result.append( word.split(":")[0] )

    #print(result) 

    result.append(texts[i])
    result.append(texts[i])
    result.append(exs[i])
    result = '"' + '";"'.join(result) + '"'
    results.append(result)
    #print(result)

with open(r"result.txt", "w", encoding="utf-8") as file:
    for  result in results:
        file.write(result + '\n')
