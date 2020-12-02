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


w ;ljk,n0mkoin+R CMD
cd /d e:/[git]/
git clone https://github.com/mirpribili/Simpler.git
e:\[git]\Simpler>python testing_v2.py
git add .
git commit -m "Add to help"
git config --global user.email "mirpribili@ya.ru"
git config --global user.name "mirpribili"
git push origin
mirpribili@ya.ru

To do:
- время тестов 
- - время каждого вопроса
- % ошибок
- как же мощны твои ответы, как же хороши твои 
- мммм мужик с тестом
"""
# preposition

import random
from random import randrange
import json
import time
import os

import migrate

from datetime import datetime
start_time = datetime.now()

def print_special_for_test_decoration_v2(method_to_decorate):
	def wrapper(*args, **kwargs):  # self, rules=rules
		print("=" * 30)
		print("Загружаю все тесты по 1")
		print("-" * 30)
		text = [
			"Вопрос: ",
			"Ответ: ",
			"Т Е Г И: ",
			"МАРКЕРЫ: "]

		key = True
		errors = set()

		while key:
			length_of_generator, max_length_of_generator = 0, 0

			all_tests = method_to_decorate(*args, **kwargs)

			for i, tests in enumerate(all_tests):  # self, rules=rules
				length_of_generator += 1

				#print(tests)
				if i not in errors:
					for j, test in enumerate(tests):
						#print("*",test)
						if len(test):
							if j == 0: 
								print(">", i+1, end="")
								print("\t" + text[j] + test.replace(";;", "\n\t\t"))
							if j == 1:
								#attempt = input("Жду ответ на вопрос теста:\n" + text[j]).strip().lower()
								attempt = ""
								while attempt == "":
									attempt = input("Жду ответ на вопрос теста:\n" + text[j]).strip().lower()
								time.sleep(random.choice(tuple(
									[0.1, 0.2, 0.3]
									)))

								answer = str(test).strip().lower()
								["I", "He", "She", "We", "You", "They"]
								[" has ", "'s ",
								 " have ", "'ve ", 
								 " will ", "'ll "]
								for replace in ["I am ", "I'm ", "He has ", "He's "]:
									pass
								if attempt == answer:
									errors.add(i)
									print("\t",
										random.choice(tuple(
											["Отлично", "Так держать", "И еще разок", "Можешь же если хочешь", "Верно", "Латум", "За Императора!!!"]
											))
										)
									time.sleep(random.choice(tuple(
										[1, 2, 3]
										)))
								else:
									print("Ответ:", test)
									input("Я запомню")# I'll be back
									os.system('cls') #
									#os.popen('clear') #
									#lambda: os.system('cls')

									print("Попробуй еще", " "*30) #\r
									time.sleep(random.choice(tuple(
										[1, 2, 3]
										)))

						else:
							errors.add(i)
			max_length_of_generator = max(length_of_generator, max_length_of_generator)
			if max_length_of_generator == len(errors): key = False

			print("\t. " * 16)
		print("-" * 30)
		print("Поздравляю ты все решил!!!") # 26 11 2020
		time_taken = datetime.now() - start_time
		print('Duration: {}'.format(time_taken))
		hours, rest = divmod(time_taken,3600)
		minutes, seconds = divmod(rest, 60)
		print('Duration: {hours}:{minutes}:{seconds}'.format(hours=hours, minutes=minutes, seconds=seconds))
		print("=" * 30)

	return wrapper

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
				input("...continue")
			print(">", i+1, end="")
			for j, element in enumerate(rules_examples_and_outher):
				if len(element):
					print("\t" + text[j] + element.replace(";;", "\n\t\t"))
			print("\t. " * 14)
			print("\t. " * 14)
		print("-" * 30)
		print("Правила закончились")
		print("=" * 30)

	return wrapper


def print_selection_tests(method_to_decorate):
	def wrapper(*args, **kwargs):  # self, rules=rules
		print("=" * 30)
		print("Загружаю все тесты")
		print("-" * 30)
		text = [
			"ТЕМА ТЕСТА: ",]
		all_tests = method_to_decorate(*args, **kwargs)
		all_tests_result = []
		for i, rules_examples_and_outher in enumerate(all_tests):  # self, rules=rules
			for j, element in enumerate(rules_examples_and_outher):
				if len(element):
					print("\t" + text[j] + element.replace(";;", "\n\t\t"))
					all_tests_result.append(element)
		print("-" * 30)
		print("Тесты закончились")
		print("=" * 30)
		return all_tests_result

	return wrapper

def print_special_for_test_decoration(method_to_decorate):
	def wrapper(*args, **kwargs):  # self, rules=rules
		print("=" * 30)
		print("Загружаю все тесты по 1")
		print("-" * 30)
		text = [
			"Вопрос: ",
			"Ответ: ",
			"Т Е Г И: ",
			"МАРКЕРЫ: "]
		for i, tests in enumerate(method_to_decorate(*args, **kwargs)):  # self, rules=rules
			print(">", i+1, end="")
			#print(tests)
			for j, test in enumerate(tests):
				#print("*",test)
				if len(test):
					if j == 0: print("\t" + text[j] + test.replace(";;", "\n\t\t"))
					if j == 1:
						next_ = True
						while next_:
							attempt = input("Жду ответ на вопрос теста: *(quit)\n" + text[j]).strip()

							time.sleep(random.choice(tuple(
								[0.1, 0.2, 0.3]
								)))

							if attempt == str(test).strip() or attempt == 'quit': 
								next_ = False
							else:
								print("\rПопробуй еще:")

						else:
							print(
								random.choice(tuple(
									["Отлично", "Так держать", "И еще разок", "Можешь же если хочешь", "Верно", "Латум", "За Императора!!!"]
									))
								)
							time.sleep(random.choice(tuple(
								[1, 2, 3]
								)))

			print("\t. " * 14)
			print("\t. " * 14)
		print("-" * 30)
		print("Поздравляю ты все решил!!!") # 26 11 2020 
		print("=" * 30)

	return wrapper



class Singleton_BD(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton_BD, cls).__new__(cls)
		return cls.instance

	def __init__(self, *args, **kwargs):
		self.id_dict = kwargs
		self.db_dict = {}

		for db in self.id_dict:
			self.id_dict[db] = {item : [] for index, item in enumerate(self.id_dict[db])}

		import copy
		self.db_dict = copy.deepcopy(self.id_dict)
		#print(json.dumps(self.id_dict, indent=4, sort_keys=False, ensure_ascii=False))


	def add_in_id_dict(self, main_db, *db, **dbs):

		#FIX DUBLI?

		for i in dbs:
			if isinstance(dbs[i], list):
				self.id_dict[main_db][i].append(
					self.__many_insert_in_table(dbs[i], self.db_dict[main_db][i])
				)
			else:
				temp = self.__insert_in_table(dbs[i], self.db_dict[main_db][i])
				self.id_dict[main_db][i].append(temp)

	def print_any_from_db(self, main_db, db,  db_itog, vektor_db, query="ALL", deep=0, rand=False):
		# задекорируй меня
		print(f"Ищу \"{query}\"")
		# get "some tag" return "some id tags"
		if query != "ALL":
			ids_tags = self.__search_any_from_db_by_query(main_db, db, query, deep)
			# get "some id tags" return "some id main db"
			ids_main = self.__search_any_from_db_by_id(ids_tags, main_db, db)
		else:
			ids_main = self.__get_all_ids_from_db(main_db, db)
		

		id_result = {}
		#print(ids_tags, ids_main)
		for index in self.id_dict[main_db]:
			#print(index)
			id_result[index] = list()
			for k, item in enumerate( self.id_dict[main_db][index] ):
				if k in ids_main:
					#print(item)
					id_result[index].append(item) 
		#print(id_result)
		#print(vektor_db)

		itog_list = list()
		temp_list = list()

		if len(id_result):
			for name_db in vektor_db:
				#print(self.db_dict[main_db][name_db])
				for single_result in id_result[name_db]:
					if isinstance(single_result, int):
						#print(self.db_dict[main_db][name_db][single_result])
						#
						itog_list.append(self.db_dict[main_db][name_db][single_result])
					else:
						temp_list.clear()
						for i in single_result:
							if len(self.db_dict[main_db][name_db][i]):
								#print("*", self.db_dict[main_db][name_db][i])
								#
								temp_list.append(self.db_dict[main_db][name_db][i])
						itog_list.append(" | ".join(temp_list))
				#print(itog_list)
			step = int(len(itog_list)/len(vektor_db))
			#print(step)

			# @BUG вот тут если бы это была БД + генератор то былабы в память добавленна 1 строчка

			result = list()
			for x in range(0, step):
				temp_list.clear()
				for i,k in enumerate( itog_list[x::step] ):
					#print(i, k)
					temp_list.append(k)
				#print(temp_list)
				#yield temp_list
				result.append(temp_list[:])
			#input()
			if rand: random.shuffle(result)
			for res in result:
				#print(res)
				yield res
		else:
			# задекорируй меня
			print( f"\tТег \"{tag}\" не найден" )

	def __for_deep_search(self, main_db, db, query):
		true_querys = set()
		for index, querys in enumerate(self.db_dict[main_db][db]):
			if query in querys.split(' '):
				true_querys.add(index)
		return true_querys


	def __many_insert_in_table(self, array, table):
		self.__chek_list_is_list(array)
		ids_array = set()
		for element in array:
			ids_array.add(self.__insert_in_table(element, table))  # update
		return ids_array

	def __for_deep_search_tegged(self, s_tag):
		true_tags = set()
		for index, tag in enumerate(self.tags):
			if s_tag in tag.split(' '):
				true_tags.add(index)
		return true_tags

	def __search_any_from_db_by_query(self, main_db, db, query, deep=0):
		ids_query = set()
		#print(self.db_dict[main_db][db])
		if query in self.db_dict[main_db][db]:
			ids_query.add(self.db_dict[main_db][db].index(query))
		if deep: # глубокий но для односложных запросов
			assert len(query.split(' ')) < 2, "print_tagged_rules -> deep_search_teged"
			#  а как will be ------ WILL + be
			ids_query.update(self.__for_deep_search(main_db=main_db, db=db, query=query))
		return ids_query

	def __search_any_from_db_by_id(self, ids, main_db, db0):
		itog = set()
		for id1 in ids:
			for index, result in enumerate(self.id_dict[main_db][db0]):
				if id1 in result:
					itog.add(index)
		return itog

	def __get_all_ids_from_db(self, main_db, db, rand=False):
		itog = list()
		for index, result in enumerate(self.id_dict[main_db][db]):
			itog.append(index)
		return itog

	def _print_all_tags_yeld():
		pass

	def _deep_search_teged():
		pass
		#"would + if + be" -> as "be"

	def _print_tag_rules():
		pass

	def _rand_shuffle_list(array):
		pass
		shuffle_array = array[:]
		random.shuffle(shuffle_array)
		return shuffle_array

	def test1(self):
		pass
		#print(json.dumps(self.db_dict, indent=4, sort_keys=False, ensure_ascii=False))
	def __test1(self):
		pass

	def _get_rand_test(self):
		pass
		print("!!!!!")

		tests_temp = Singleton_BD.rand_shuffle_list(self.tests)

		for test in tests_temp:
			print(test)
			print("\t Enter you answer:")
			new_answer = input().strip()

	def _print_arg(self):
		pass


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


class Singleton_BD_new_prints(Singleton_BD):
	"""docstring for Singleton_BD_new_prints"""
	def __init__(self, *args, **kwargs):
		super(Singleton_BD_new_prints, self).__init__(*args, **kwargs)

	#python decorate function parent class???
	@print_all_rules_with_comment
	def print_any_from_db(self, main_db, db,  db_itog, vektor_db, query="ALL", deep=0,):
		return super().print_any_from_db(main_db=main_db, db=db,  db_itog=db_itog, vektor_db=vektor_db, query=query, deep=deep)

	@print_special_for_test_decoration_v2
	def print_special_for_test(self, main_db, db, db_itog, vektor_db, query="ALL"):
		return super().print_any_from_db(main_db=main_db, db=db, db_itog=db_itog, vektor_db=vektor_db, query=query, deep=0, rand=True)

	@print_selection_tests
	def print_selection_test(self, main_db, db,  db_itog, vektor_db, query="ALL"):
		return super().print_any_from_db(main_db=main_db, db=db,  db_itog=db_itog, vektor_db=vektor_db, query=query, deep=0)

	'''
		self.test()

	def test(self):
		self._test()
		super().test1()
		super()._print_arg()
		super().__test1()

	def _test(self):
		print("ok")
	'''


s = Singleton_BD_new_prints(
	rules=["rule","examples","tags","mark"], 
	tests=["test","answer","tags","mark"],
	tests_thems=["thems"],
	) # "tests", "examples", "tags", "mark", "answer", 
'''
				"id_rule": id_rule,
				"ids_examples": ids_examples,
				"ids_tags": ids_tags,
				"id_mark": id_mark
'''



###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
s.add_in_id_dict(
	main_db="tests_thems",
	thems="№1 - отглагольные прилагательные",
	)
s.add_in_id_dict(
	main_db="tests_thems",
	thems="№2 - 21 комбинация времен",
	)




tests = migrate.tests

for test in tests:
	s.add_in_id_dict(
		main_db=test["main_db"],
		test=test["test"],
		answer=test["answer"],
		tags=test["tags"],
		mark=test["mark"]
	)


tests = migrate.rules

for test in tests:
	s.add_in_id_dict(
		main_db=test["main_db"],
		rule=test["rule"],
		examples=test["examples"],
		tags=test["tags"],
		mark=test["mark"]
	)
#s.print_rules()

#s.print_tagged_rules("have")
#s.print_tagged_rules("ed",deep=1)


'''
print("Object created", s, s.print_arg())
print("="*20)
s1 = Singleton_BD()
print("Object created", s1, s.print_arg())

Вывод выполнения кода должен быть примерно таким:
('Object created', <__main__.Singleton object at 0x10ba9db90>)
('Object created', <__main__.Singleton object at 0x10ba9db90>)
'''

os.system('cls') 
while True:
	#s.test1()
	#s.test2()
	try:
		test_or_rule = int(input("1 - tests, 2 - rule\n"))
	except Exception as e:
		print(e)
		test_or_rule = 0


	if test_or_rule == 2:
		s.print_any_from_db(main_db="rules", db="tags", query=input("Enter you query:"), db_itog="rule", deep=1, vektor_db=["rule", "examples", "tags", "mark"])
	#if test_or_rule == 1:
	#	s.print_special_for_test(main_db="tests", db="test", db_itog="test", vektor_db=["test", "answer", "tags", "mark"])		
	if test_or_rule == 1:
		#s.print_any_from_db(main_db="tests", db="test", db_itog="test", vektor_db=["test", "answer", "tags", "mark"])		
		all_tests = s.print_selection_test(main_db="tests_thems", db="thems", db_itog="thems", vektor_db=["thems",])	
		len_all_tests = len(all_tests)
		#print(all_tests)
		try:
			test_number = int(input("Выбрали номер теста?\n"))
			if test_number - 1 in [ i for i in range(0, len_all_tests) ]:
				#s.print_special_for_test(main_db="tests", db="test", db_itog="test", vektor_db=["test", "answer", "tags", "mark"])	
				s.print_special_for_test(main_db="tests", db="tags", query=all_tests[test_number-1], db_itog="test", vektor_db=["test", "answer", "tags", "mark"])	
		except Exception as e:
			print(e)
			print("Давай-те я верну Вас в начальное меню")

#import re
#>>> s = "a b        c d    e                            f  "
#>>> re.sub('\s{2,}', ' ', s)
#'a b c d e f '





