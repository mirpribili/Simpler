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
                print("\t" + text[j] + element)
            print("\t. " * 15)
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
        if rules is "all":
            rules = self.general_rules
        for ids in rules:
            yield [
                self.rules[ids["id_rule"]],
                " | ".join([self.examples[i] for i in ids["ids_examples"]]),
                " | ".join([self.tags[i] for i in ids["ids_tags"]]),
                self.marks[ids["id_mark"]],
            ]

    def print_tagged_rules(self, tag):
        # print(self.general_rules)
        if tag in self.tags:
            id_tags = self.tags.index(tag)
            rules = list()
            for rule in self.general_rules:
                if id_tags in rule["ids_tags"]:
                    rules.append(rule)
            self.print_rules(rules)
        else:
            return "Тег не найден"

    def print_all_tags_yeld():
        pass

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
    rule="если объект САМ СОВЕРШАЕТ действие " +
         "{прилагательное = глагол + ING} " +
         "звук РАЗДРАЖАЕТ вас = раздражающий annoyING",
    examples=["what an embrassing situation?", "who's dating who?"],
    tags=["отглагольные прилагательные", "глагол + ING", "V + ING", "Up.Interm.V.ing"],
    mark="#Up.Interm.V.ing"
)
s.add_rule(
    rule="если объект ПОДВЕРГАЕТСЯ воздействию " +
         "{прилагательное = глагол + ED (3ф.)} " +
         "вас РАЗДРАЖАЕТ звук = вы раздражены annoyED",
    examples=["brokEN", "relaxED"],
    tags=["отглагольные прилагательные", "глагол + ED", "V + ED", "Up.Interm.V.ed"],
    mark="#Up.Interm.V.ed"
)
s.print_rules()

s.print_tagged_rules("V + ED")

'''
print("Object created", s, s.print_arg())
print("="*20)
s1 = Singleton_BD()
print("Object created", s1, s.print_arg())

Вывод выполнения кода должен быть примерно таким:
('Object created', <__main__.Singleton object at 0x10ba9db90>)
('Object created', <__main__.Singleton object at 0x10ba9db90>)
'''
