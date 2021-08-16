words_per_card = 4

def ends(string):
    string2 = string.strip()
    if "." in string2:
        #string2 = string2[0:len(string2) - 1]
        pass
    return string2

words = []
texts = []
text = []
exs = []
ex = []
ex_str =""

# получим объект файла
file1 = open("test_4b.txt", "r", encoding="utf-8")

# считываем все строки
lines = file1.readlines()

# закрываем файл
file1.close
new_i = 0
for i, line in enumerate( lines ):
    if '____' in line[0:4]:
        #print(line)
        new_i = i + 1
        lines = lines[new_i:]
        #print(i)
        break
    

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
            exit("\nERROR\n!! #1 sting тДЦ" + str(counter+1+new_i))
        #--------------------
        #print(line[4:])
        if len(line)>6:
            words.append(ends(line[4:]))

    if "##__" in line:
        #--------------------
        if "##__" in bufer:
            exit("\nERROR\n!! #2 sting тДЦ" + str(counter+1+new_i))
        #--------------------
        texts.append(ends(line[4:]))

    if "###_" in line:
        #--------------------
        if "#___" in bufer:
            exit("\nERROR\n!! #3 sting тДЦ" + str(counter+1+new_i))
        #--------------------
        #print(line)
        exs.append(ends(line[4:]))

    bufer = line



    if "#___" not in line and "##__" not in line and "###_" not in line:
        exit("\nERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n " + str(counter+1+new_i))


import random

def func_list_rand_2_for_mix(list,list_numb_except):
    while True:
        rand = random.randint(0, len(list)-1)
        if rand not in list_numb_except:
            return rand

def func_list_mix_2_elem(list,list_numbs):
    if len(list_numbs) > 2:
        exit("\nERROR in func_list_mix_2_elem()")
    elem1 = list[list_numbs[0]]
    elem2 = list[list_numbs[1]]
    list[list_numbs[0]] = elem2
    list[list_numbs[1]] = elem1
    return list;

def func(string):
    while True:
        if string.endswith('.'):
            string = string[0:len(string) - 1]
        else:
            return string
def shuffl_string(string):
    temp = string.split()
    random.shuffle( temp )
    return ' '.join(temp)

def replace_up(string, what, on_what):
        temp_text = string.replace(str(what), on_what )
        word_up = str(what.capitalize())
        temp_text = temp_text.replace(word_up, on_what )
        return temp_text
#print(words)
#print(texts)
#print(exs)


#print( texts )
#print( a )

#print("--")


 
#print("--")
#exit("\n-= OK =-\n")
results = []
#print(words)
for i, word in enumerate(words):
    #print(i)
    result = temp =[]

    #result.append( word.split(":")[0] )


    #print(result)
    #----------
    #result.append(shuffl_string(texts[i]))
    #result.append(replace_up(texts[i], word.split(":")[0], word.split(":")[1]) )
    #----------
    #print(texts[i])
    result.append(texts[i])
    #print(word)
    #print(str(len(word.split(":"))) + "!")
    word_set = word.split(":")
    #print(word_set)

    if len(texts[i]) > 120 and not 'any length' in word_set[2:]:
        exit("\nERROR:\n" + texts[i])

    if len(word_set) == 2 or 'do not mix' in word_set[2:]:
        result.append(replace_up(texts[i], word.split(":")[0], word.split(":")[1].upper() ) )
    elif word_set[2] == '':
        temp_texts = texts[i].split(" ")
        temp_rand = [0,len(temp_texts)-1]
        temp_rand.append( func_list_rand_2_for_mix(temp_texts, temp_rand) )
        temp_rand.append( func_list_rand_2_for_mix(temp_texts, temp_rand) )
        temp_rand.append( func_list_rand_2_for_mix(temp_texts, temp_rand) )
        #print(temp_rand)
        #print(temp_rand[2:4])
        #print(temp_rand[3:5])
        mix = func_list_mix_2_elem(temp_texts, temp_rand[2:4])
        mix = func_list_mix_2_elem(mix, temp_rand[3:5])
        result.append(
            replace_up(
                #" ".join(func_list_mix_2_elem(temp_texts, temp_rand[2:4])), 
                " ".join(mix), 
                word.split(":")[0], word.split(":")[1].upper() 
                ) 
            )
    
        #result.append(" ".join(func_list_mix_2_elem(temp_texts, temp_rand[2:4])) )
        #print(texts[i])

    result.append(texts[i])
    result.append(exs[i])
    result = '"' + '";"'.join(result) + '"'
    results.append(result)
    #print(result)

#random.shuffle( results )
with open(r"result.txt", "w", 
    encoding="utf-8"
    #encoding="windows-1251"
    ) as file:
    for  result in results:
        file.write(result + '\n')
print(len(results))
