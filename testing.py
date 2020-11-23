#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Затронутые темы:
        - реляционные базы данных
        - декораторы
        - классы
        - генераторы
        - single ton
        - ну и мелочи
        - - отсутствие дублирование кода при работе с 5 бд
        - - случайное смешивание списка
        - - избавление от дублирования в бд (решение проблемы вставки в бд имеющегося в ней значения)
    Реализованный функционал:
        - добавка в бд правил с тегами метками и примерами
        - добавка в бд тестов с тегами метками и примерами
        - вывод правил
        - - всех
        - - по определенному тегу
"""
import random
from random import randrange


def print_all_rules_with_comment(method_to_decorate):
    def wrapper(*args, **kwargs):  # self, rules=rules
        print("=" * 30)
        print("Загружаю все правила")
        print("-" * 30)
        text = [
            "ПРАВИЛО: ",
            "ПРИМЕРЫ: ",
            "Т Е Г И: ",
            "МАРКЕРЫ: "]
        for i, rules_examples_and_outher in enumerate(method_to_decorate(*args, **kwargs)):  # self, rules=rules
            if i % 5 == 0 and i > 0:
                input()
            for j, element in enumerate(rules_examples_and_outher):
                print("\t" + text[j] + element.replace(";;", "\n\t\t\t"))
            print(">",i+1, "\t. " * 14)
        print("-" * 30)
        print("Правила закончились")
        print("=" * 30)

    return wrapper


class Singleton_BD(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton_BD, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.arg = 1
        # list to set? = NO! then id will del
        self.tests = list()
        self.tests_answers = list()
        self.tags = list()
        self.rules = list()
        self.examples = list()

        self.marks = list()  # _for_test

        # only list
        self.general_tests = list()
        self.general_rules = list()

    def add_rule(self, rule, examples, tags, mark):
        id_rule = self.__insert_in_table(rule, self.rules)
        ids_examples = self.__many_insert_in_table(examples, self.examples)
        ids_tags = self.__many_insert_in_table(tags, self.tags)
        id_mark = self.__insert_in_table(mark, self.marks)
        # нужны ли проверки?
        self.general_rules.append(
            {
                "id_rule": id_rule,
                "ids_examples": ids_examples,
                "ids_tags": ids_tags,
                "id_mark": id_mark
            }
        )

    def __many_insert_in_table(self, array, table):
        self.__chek_list_is_list(array)
        ids_array = set()
        for element in array:
            ids_array.add(self.__insert_in_table(element, table))  # update
        return ids_array

    def add_test(self, test, answer, marks):
        pass

    @print_all_rules_with_comment
    def print_rules(self, rules="all"):
        if rules == "all":
            rules = self.general_rules
        for ids in rules:
            yield [
                self.rules[ids["id_rule"]],
                " | ".join([self.examples[i] for i in ids["ids_examples"]]),
                " | ".join([self.tags[i] for i in ids["ids_tags"]]),
                self.marks[ids["id_mark"]],
            ]

    def __for_deep_search_tegged(self, s_tag):
        true_tags = set()
        for index, tag in enumerate(self.tags):
            if s_tag in tag.split(' '):
                true_tags.add(index)
        return true_tags

    def print_tagged_rules(self, tag, deep=0):
        # задекорируй меня
        print(f"Ищу по тегу \"{tag}\"")
        id_tags = set()

        if tag in self.tags:
            id_tags.add(self.tags.index(tag))
        if deep: # глубокий но для односложных запросов
            assert len(tag.split(' ')) < 2, "print_tagged_rules -> deep_search_teged"
            #  а как will be ------ WILL + be
            id_tags.update(self.__for_deep_search_tegged(tag))
        


        if len(id_tags):
            rules = list()
            for rule in self.general_rules:
                for id_tag in id_tags:
                    if id_tag in rule["ids_tags"] and rule not in rules:
                        rules.append(rule)
            self.print_rules(rules)
        else:
            # задекорируй меня
            print( f"\tТег \"{tag}\" не найден" )

    def print_all_tags_yeld():
        pass

    def deep_search_teged():
        pass
        #"would + if + be" -> as "be"

    def print_tag_rules():
        pass

    def rand_shuffle_list(array):
        shuffle_array = array[:]
        random.shuffle(shuffle_array)
        return shuffle_array

    def get_rand_test(self):
        print("!!!!!")

        tests_temp = Singleton_BD.rand_shuffle_list(self.tests)

        for test in tests_temp:
            print(test)
            print("\t Enter you answer:")
            new_answer = input().strip()

    def print_arg(self):
        return self.arg

    def __check_element_not_in_list(element, array):
        if element in array:
            return False

    def __chek_list_is_list(self, array):
        assert isinstance(array, list), "__chek_list_is_list: error array is not list"

    def __insert_in_table(self, string, table):
        string = str(string)
        assert isinstance(table, list), "__insert_in_table: error table is not list"
        # assert string not in table , "__insert_".string
        if string not in table:
            table.append(string)
            id = len(table) - 1
            return id
        else:
            id = table.index(string)
            return id


s = Singleton_BD()

s.add_rule(
    rule="если объект САМ СОВЕРШАЕТ действие;; " +
         "{прилагательное = глагол + ing};; " +
         "звук РАЗДРАЖАЕТ вас = раздражающий annoying",
    examples=["what an embrassing situation?", "who's dating who?"],
    tags=["отглагольные прилагательные", "глагол + ing", "V + ing", "#Up.Interm.V.ing"],
    mark="#Up.Interm.V.ing"
)
s.add_rule(
    rule="если объект ПОДВЕРГАЕТСЯ воздействию;; " +
         "{прилагательное = глагол + ed (3ф.)};; " +
         "вас РАЗДРАЖАЕТ звук = вы раздражены annoyed",
    examples=["brokEN", "relaxed"],
    tags=["отглагольные прилагательные", "глагол + ed", "V + ed", "#Up.Interm.V.ed"],
    mark="#Up.Interm.V.ed"
)

s.add_rule(
    rule="Сослагательное наклонение образ. с пом. {would - БЫ};; " +
         "{вопрос: Wh. would + подлеж. + глагол? Отриц: wouldn't};; " +
         "C мест-ем сокращ до {'d};;" +
         "{ if } условие при котором СЕЙСЧАС НАСТУПИЛО БЫ событ.;;" +
         "{if + усл. в прош. вр. +[be -> were] + событие с would}",
    examples=["I would do it for you - я !с!делаю это для тебя"],
    tags=["Сослагательное наклонение", "would", "would + if", "would + if + be", "Present.would",  "#Interm.would"],
    mark="#Interm.would"
)

s.add_rule(
    rule="Вероятность событий. Если событие ВПОЛНЕ может быть, то may | might | could;;" +
         "{подлеж. + may | might | could  + глагол} ",
    examples=["it might rain tomorrow - завтра может пойти дождь"],
    tags=["Вероятность событий", "событие ВПОЛНЕ может быть", "may might could", "may", "might", "could",  "#Interm.may.might.could"],
    mark="#Interm.may.might.could"
)

s.add_rule(
    rule="Вероятность событий. Слова, обозначающие уверенность: should | must - должны, can't - не может;;" +
         "{подлеж. + should (shouldn't) | must | can't  + глагол} ;;" +
         "Вопрос: {should подлеж. + глагол} ",
    examples=[""],
    tags=["Вероятность событий", "Слова, обозначающие уверенность", "should must can't", "should", "must", "can't",  "#Interm.should.must.can't"],
    mark="#Interm.should.must.can't"
)

# Tenses------------------------
'''
s.add_rule(
    rule="Pr.S. действие происходит обычно / в принципе;;" +
         "{+:_ V,(he)V s; -:_ don't(he)doesn't V};;" +
         "{+:_ have|has; -:_ don't(he)doesn't have };;" +
         "{+:_ am|is|are|can; -:_ am|is|are|can not };;" +
         "Собираться что-то делать;;" +
         "{+:Wh. am|is|are _ going to V};;" +
         "Следует, стоит;;" +
         "{+:_ should V; -:_ shouldn't V};;" +
         "Обязан;;" +
         "{+:_ have|has to V; -:_ don't|doesn't have|has to V};;";
    examples=["I work. She has a work*. We don't work. He doesn't work"],
    tags=["Pr.S", "V s", "does", "do", "have", "has", "am are is", "can", "am going to", "am going to", "ing", "should V", "have to V", ],
    mark="#Elem.Pr.S.do.does.Vs.have.am.are.is.can.going.to"
)
'''
s.add_rule(
    rule="Pr.S. действие происходит обычно / в принципе;;" +
         "{+:_ V,(he)V s; -:_ don't(he)doesn't V};;" +
         "{+:_ have|has; -:_ don't(he)doesn't have };;" +
         "{+:_ am|is|are|can; -:_ am|is|are|can not };;",
    examples=["I work. She has a work*. We don't work. He doesn't work"],
    tags=["Pr.S", "V s", "does", "do", "have", "has", "am are is", "can",],
    mark="#Elem.Pr.S.do.does.Vs"
)

s.add_rule(
    rule="Собираться что-то делать;;" +
         "{+:Wh. am|is|are _ going to V};;" ,
    examples=[""],
    tags=["am going to", "am going to", "ing",  ],
    mark="#Elem.going.to"
)

s.add_rule(
    rule="Следует, стоит;;" +
         "{+:_ should V; -:_ shouldn't V};;",
    examples=[""],
    tags=["should V", ],
    mark="#Elem.should"
)
s.add_rule(
         "Обязан;;" +
         "{+:_ have|has to V; -:_ don't|doesn't have|has to V};;",
    examples=[""],
    tags=["have to V", ],
    mark="#Elem.have.to"
)

s.add_rule(
    rule="Должен сделать;;" +
         "{+:_ must V; -:_ mustn't V};;" ,
    examples=[""],
    tags=["must V"],
    mark="#Elem.must"
)


s.add_rule(
    rule="P.S. действие произошло в завершенный промежуток времени;;" +
         "{+:_ V ed; -:_ did not V };;" +
         "{+:_ was|were|could; -:_ was|were|could not };;" +
         "{  ? string ? [yesterday | last week | once | two days ago] };;" +
         "Действие было в планах;;" +
         "{+:Wh. was|were _ going to V };;" +
         "Способности, возможности в прошлом;;" +
         "{ could V, couldn't V };;"  +
         "Я мог мне удолось;;"  +
         "{ _ was|were able to V};;" ,
    examples=["It was cold. We didn't buy tea. We bought tea. We washed the window.*"],
    tags=["P.S", "was", "were", "yesterday", "ing", "V ed", "V ed", "could V", "was were able to V"],
    mark="#Elem.P.S.was.were.could"
)
s.add_rule(
    rule="F.S. действие случится в будущем;;" +
         "{+:_ will V; -:_ won't V };;" +
         "При каком условии наступит событ. в будущем;;" +
         "{if + усл. в наст. вр. + событие в будущем};;" +
         " Я смогу, я буду уметь ;;" +
         "{+:_ will be able to; -:_ won't be able to}",
    examples=[""],
    tags=["F.S", "will", "will if", "will br able to"],
    mark="#Elem.F.S.will"
)

s.add_rule(
    rule="Pr.C. Совершается прямо сейчас и еще не завершилось;;" +
         "{+:_ am|is|are V ing; -:_ am|is|are not V ing };;" ,
    examples=[""],
    tags=["Pr.C", "V ing", "was V ing", "ing"],
    mark="#Elem.Pr.C"
)

s.add_rule(
    rule="P.C. одно действие было прервано другим;;" +
         "{+:_ was|were V ing; -:_ was|were not V ing };;" ,
    examples=[""],
    tags=["P.C", "V ing", "was V ing", "were V ing", "ing"],
    mark="#Elem.P.C"
)

s.add_rule(
    rule="F.C. будет происходить и в указанный момент не завершится;;" +
         "{+:_ will be V ing; -:_ won't be V ing };;" +
         "{+:Will there be _ ?; };;" ,
    examples=[""],
    tags=["F.C", "V ing", "will be V ing", "will V ing", "be V ing", "ing"],
    mark="#Elem.F.C"
)

s.add_rule(
    rule="Pr.P. (не было) сделано к настоящему моменту (не важно когда!);;" +
         "{+: _ have|has V ed; -:_ have|has not V ed };;" ,
    examples=[""],
    tags=["have V ed", "has V ed", "have ed", "ed", "V ed"],
    mark="#Interm.Pr.P"
)

s.add_rule(
    rule="Pr.P.C. Действие длится неколторое время и продолжается сейчас;;" +
         "{+: _ have|has been V ing; -:_ have|has been not V ing };;" ,
    examples=[""],
    tags=["have been V ing", "have been V ing"],
    mark="#Interm.Pr.P.C."
)


s.add_rule(
    rule="P.P. Действие завершилось РАНЕЕ другого события в прошлом;;" +
         "{+: _ had V ed; -:_ hadn't V ed };;" ,
    examples=[""],
    tags=["had V ed", "hadn't V ed"],
    mark="#Interm.P.P."
)

s.add_rule(
    rule="F.P. Действие завершится к указанному моменту;;" +
         "{+: _ will have V ed; -:_ won't have V ed };;" +
         "{by the time };;" ,
    examples=[""],
    tags=["will have V ed",],
    mark="#Interm.F.P."
)

s.add_rule(
    rule="it be. Нельзя определить кто выполняет действие;;" +
         "{it is|was ...; it will be ...};;" ,
    examples=[""],
    tags=["it be", "it.be"],
    mark="#Elem.it.be"
)



#s.print_rules()

#s.print_tagged_rules("have")
#s.print_tagged_rules("ed",deep=1)
while True:
    s.print_tagged_rules(input("Enter you word:"),deep=1)

'''
print("Object created", s, s.print_arg())
print("="*20)
s1 = Singleton_BD()
print("Object created", s1, s.print_arg())

Вывод выполнения кода должен быть примерно таким:
('Object created', <__main__.Singleton object at 0x10ba9db90>)
('Object created', <__main__.Singleton object at 0x10ba9db90>)
'''
