words_per_card = 4
'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''
#=============================
words = [
    "considerable",
    "significant"
    ]
print(words)
#=============================
#=============================
texts = [
    [
        "great in amount, size, importance, etc."
    ],
    [
        "large or important enough to have an effect or to be noticed.",
        "having a particular meaning",
        "[usually before noun] having a special or secret meaning that is not understood by everyone",
    ],
]
#=============================

exs = [
    #
    [
        " ".join(
            [
                "Considerable progress has been made in finding a cure for the disease.",
            ]
        )
    ],
    #
    [
        " ".join(
            [
                "There are no significant differences between the two groups of students.",
                "Asthma has a significant impact on the life and well-being of children affected by this disease.",
            ]
        )
        ," ".join(
            [
                "It is significant that he changed his will only days before his death.",
                "The fact that her remarks were leaked to the media in advance is highly significant.",
            ]
        )
        ," ".join(
            [
                "a significant look/smile",
            ]
        )
    ],
]
#=============================
'''
#print(exs)


words = []
texts = []
text = []
exs = []
ex = []
ex_str =""

# получим объект файла
file1 = open("cogitate.txt", "r")

# считываем все строки
lines = file1.readlines()

# закрываем файл
file1.close

bufer = "###_"
# итерация по строкам
for counter, line in enumerate(lines):
    #
    line = line.strip()
    #print(line)
    #print(line.find("#"))
    #
    if "#___" in line:
        #--------------------
        if "###_" not in bufer:
            exit("\nERROR\n!! #1 sting №" + str(counter+1))
        #--------------------
        #print(line[4:])
        if len(line)>4:
            words.append(line[4:])
        if text != []:
            texts.append(text)
            text = []


        if ex_str != "":
            ex.append(ex_str)
            ex_str = ""
        if ex != []:
            exs.append(ex)
            ex = []

    if "##__" in line:
        #--------------------
        if "##__" in bufer:
            exit("\nERROR\n!! #2 sting №" + str(counter+1))
        #--------------------
        text.append(line[4:])
        if ex_str != "":
            ex.append(ex_str)
            ex_str = ""
    if "###_" in line:
        #--------------------
        if "#___" in bufer:
            exit("\nERROR\n!! #3 sting №" + str(counter+1))
        #--------------------
        #print(line)
        if ex_str != "":
            ex_str = ex_str + " " + line[4:]
        else:
            ex_str = line[4:]

    bufer = line



    if "#___" not in line and "##__" not in line and "###_" not in line:
        exit("\nERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n " + str(counter+1))



#print(texts)
#print(words)
#print("--")
#print(exs)

 
#print("--")
#quit("\n-= OK =-\n")



number = res_number = 0
res_text = ""
res_text_ex = ""
res_words =[]

for word in words:
    res_words.append(word)
    #number = number + 1
    new_text = ""
    new_text_ex = ""
    temp_ex = exs.pop(0)
    #print(number)
    number = number + 1
    res_number = res_number + 1

    for text in texts.pop(0):
        temp_text = ""
        temp_ex2 = temp_ex.pop(0)
        
        res_text_ex = res_text_ex + text + '{' + temp_ex2 + '}'
        
        
        temp_text = temp_ex2.replace(str(word), '('+str(res_number)+')' )
        word_up = str(word.capitalize())

        temp_text = temp_text.replace(word_up, '('+str(res_number)+')' )
        
        #print(temp_text)
        

        res_text = res_text + text + '{' + temp_text + '}'
        
    #print(new_text)
    #print(number % 3)
    #print(number)
    #number = number - 1

    if number and not number % words_per_card:
        resalt = '"' + " ".join(map(str, res_words)) + '";"' + res_text + '";"#' + res_text_ex + '#";"trans"'
        res_text = ""
        res_text_ex = ""
        res_words = []
        res_number = 0
        print(resalt)
        #exit()



if number%words_per_card:
    print(len(words))
    print(number//words_per_card)

print("!\tall words add in "+ str(number//words_per_card) +" cards\t!")
'''
list1=[0,1,2,3,4,5,6,7,8,9,10] #pop last element 
#print("pop() returns :",list1.pop(0),"; currently list=",list1)

class Data_english(object):
    """docstring"""
    
    def __init__(self, word, opred, ex, ex_rus):
        """Constructor"""
        self.word = word
        self.opred = opred
        self.ex = ex
        self.ex_rus = ex_rus
    
    def get_word(self):
        return self.word
    
 
if __name__ == "__main__":
    english = Data_english(
        "significant", 
        5, 
        4, 
        "car")
    
    #print(english.get_word())
'''
    

