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
# preposition

import random
from random import randrange
import json
import time
import os

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
			length_of_generator = 0
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
								attempt = input("Жду ответ на вопрос теста:\n" + text[j]).strip().lower()
								time.sleep(random.choice(tuple(
									[0.1, 0.2, 0.3]
									)))
								if attempt == str(test).strip().lower():
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
			if length_of_generator == len(errors): key = False

			print("\t. " * 16)
		print("-" * 30)
		print("Поздравляю ты все решил!!!") # 26 11 2020 
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
			print("\t. " * 16)
			print("\t. " * 16)
		print("-" * 30)
		print("Правила закончились")
		print("=" * 30)

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

			print("\t. " * 16)
			print("\t. " * 16)
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

	def print_any_from_db(self, main_db, db,  db_itog, vektor_db, query="ALL", deep=0,):
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

			for x in range(0, step):
				temp_list.clear()
				for i,k in enumerate( itog_list[x::step] ):
					#print(i, k)
					temp_list.append(k)
				#print(temp_list)
				yield temp_list
			#input()
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
	def print_special_for_test(self, main_db, db, db_itog, vektor_db):
		return super().print_any_from_db(main_db=main_db, db=db, db_itog=db_itog, vektor_db=vektor_db)
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
s.add_in_id_dict(
	main_db="tests_thems",
	thems="№1 - отглагольные прилагательные",
	)


s.add_in_id_dict(
	main_db="rules",
	rule="выражает признак | если объект САМ СОВЕРШАЕТ действие;; " +
		 "{прилагательное = глагол + ing};; " +
		 "звук РАЗДРАЖАЕТ вас = раздражающий annoying",
	examples=["what an embrassing situation?", "who's dating who?"],
	tags=["отглагольные прилагательные", "глагол + ing", "V + ing", "#Up.Interm.V.ing"],
	mark="#Up.Interm.V.ing"
)
s.add_in_id_dict(
	main_db="rules",
	rule="выражает чувство | если объект ПОДВЕРГАЕТСЯ воздействию;; " +
		 "{прилагательное = глагол + ed (3ф.)};; " +
		 "вас РАЗДРАЖАЕТ звук = вы раздражены annoyed",
	examples=["brokEN", "relaxed"],
	tags=["отглагольные прилагательные", "глагол + ed", "V + ed", "#Up.Interm.V.ed"],
	mark="#Up.Interm.V.ed"
)

s.add_in_id_dict(
	main_db="rules",
	rule="Сослагательное наклонение образ. с пом. {would - БЫ};; " +
		 "{вопрос: Wh. would + подлеж. + глагол? Отриц: wouldn't};; " +
		 "C мест-ем сокращ до {'d};;" +
		 "{ if } условие при котором СЕЙСЧАС НАСТУПИЛО БЫ событ.;;" +
		 "{if + усл. в прош. вр. +[be -> were] + событие с would}",
	examples=["I would do it for you - я !с!делаю это для тебя"],
	tags=["Сослагательное наклонение", "would", "would + if", "would + if + be", "Present.would",  "#Interm.would"],
	mark="#Interm.would"
)

s.add_in_id_dict(
	main_db="rules",
	rule="Вероятность событий. Если событие ВПОЛНЕ может быть, то may | might | could;;" +
		 "{подлеж. + may | might | could  + глагол} ",
	examples=["it might rain tomorrow - завтра может пойти дождь"],
	tags=["Вероятность событий", "событие ВПОЛНЕ может быть", "may might could", "may", "might", "could",  "#Interm.may.might.could"],
	mark="#Up.Interm.may.might.could"
)

s.add_in_id_dict(
	main_db="rules",
	rule="Вероятность событий. Слова, обозначающие уверенность:;; should | must - должны, can't - не может;;" +
		 "{подлеж. + should (shouldn't) | must | can't  + глагол} ;;" +
		 "Вопрос: {should подлеж. + глагол} ",
	examples=[""],
	tags=["Вероятность событий", "Слова, обозначающие уверенность", "should must can't", "should", "must", "can't",  "#Interm.should.must.can't"],
	mark="#Up.Interm.should.must.can't"
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
s.add_in_id_dict(
	main_db="rules",
	rule="Pr.S. действие происходит обычно / в принципе;;" +
		 "{+:_ V,(he)V s; -:_ don't(he)doesn't V};;" +
		 "{+:_ have|has; -:_ don't(he)doesn't have };;" +
		 "{+:_ am|is|are|can; -:_ am|is|are|can not };;",
	examples=["I work. She has a work*. We don't work. He doesn't work"],
	tags=["Pr.S", "V s", "does", "do", "have", "has", "am are is", "can",],
	mark="#Elem.Pr.S.do.does.Vs"
)

s.add_in_id_dict(
	main_db="rules",
	rule="Собираться что-то делать;;" +
		 "{+:Wh. am|is|are _ going to V}",
	examples=[""],
	tags=["am going to", "am going to", "ing",  ],
	mark="#Elem.going.to"
)

s.add_in_id_dict(
	main_db="rules",
	rule="Следует, стоит;;" +
		 "{+:_ should V; -:_ shouldn't V};;",
	examples=[""],
	tags=["should V", ],
	mark="#Elem.should"
)
s.add_in_id_dict(
	main_db="rules",
	rule="Обязан;;" +
		 "{+:_ have|has to V; -:_ don't|doesn't have|has to V};;",
	examples=[""],
	tags=["have to V", ],
	mark="#Elem.have.to"
)

s.add_in_id_dict(
	main_db="rules",
	rule="Должен сделать;;" +
		 "{+:_ must V; -:_ mustn't V}",
	examples=[""],
	tags=["must V"],
	mark="#Elem.must"
)

s.add_in_id_dict(
	main_db="rules",
	rule="P.S. действие произошло в завершенный промежуток времени;;" +
		 "{+:_ V ed; -:_ did not V };;" +
		 "{+:_ was|were|could; -:_ was|were|could not };;" +
		 "{  ? string ? [ yesterday | last week | once | two days ago] };;",
	examples=["It was cold. We didn't buy tea. We bought tea. We washed the window.*"],
	tags=["P.S", "was", "were", "could", "yesterday", "V ed", "did",],
	mark="#Elem.P.S.was.were.could"
)


s.add_in_id_dict(
	main_db="rules",
	rule="Я мог мне удолось;;"  +
		 "{ _ was|were able to V}" ,
	examples=[""],
	tags=["was were able to V", "able to V", "was able to V"],
	mark="#Elem.was.were.able.to"
)
s.add_in_id_dict(
	main_db="rules",
	rule="Действие было в планах;;" +
		 "{+:Wh. was|were _ going to V }" ,
	examples=[""],
	tags=["was were going to V", "going to V", "was going to V"],
	mark="#Elem.was.were.going.to"
)
s.add_in_id_dict(
	main_db="rules",
	rule="Способности, возможности в прошлом;;" +
		 "{ could V, couldn't V }",
	examples=[""],
	tags=["could V", "could V"],
	mark="#Elem.could"
)



s.add_in_id_dict(
	main_db="rules",
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

s.add_in_id_dict(
	main_db="rules",
	rule="Pr.C. Совершается прямо сейчас и еще не завершилось;;" +
		 "{+:_ am|is|are V ing; -:_ am|is|are not V ing }",
	examples=[""],
	tags=["Pr.C", "V ing", "was V ing", "ing"],
	mark="#Elem.Pr.C"
)

s.add_in_id_dict(
	main_db="rules",
	rule="P.C. одно действие было прервано другим;;" +
		 "{+:_ was|were V ing; -:_ was|were not V ing }",
	examples=[""],
	tags=["P.C", "V ing", "was V ing", "were V ing", "ing"],
	mark="#Elem.P.C"
)

s.add_in_id_dict(
	main_db="rules",
	rule="F.C. будет происходить и в указанный момент не завершится;;" +
		 "{+:_ will be V ing; -:_ won't be V ing };;" +
		 "{+:Will there be _ ?; }",
	examples=[""],
	tags=["F.C", "V ing", "will be V ing", "will V ing", "be V ing", "ing", "F.C.", "F.C"],
	mark="#Elem.F.C"
)

s.add_in_id_dict(
	main_db="rules",
	rule="Pr.P. (не было) сделано к настоящему моменту (не важно когда!);;" +
		 "{+: _ have|has V ed; -:_ have|has not V ed }",
	examples=[""],
	tags=["have V ed", "has V ed", "have ed", "ed", "V ed", "Pr.P", "Pr.P."],
	mark="#Interm.Pr.P"
)

s.add_in_id_dict(
	main_db="rules",
	rule="Pr.P.C. Действие длится неколторое время и продолжается сейчас;;" +
		 "{+: _ have|has been V ing; -:_ have|has been not V ing }",
	examples=[""],
	tags=["have been V ing", "have been V ing", "Pr.P.C.", "Pr.P.C"],
	mark="#Interm.Pr.P.C."
)


s.add_in_id_dict(
	main_db="rules",
	rule="P.P. Действие завершилось РАНЕЕ другого события в прошлом;;" +
		 "{+: _ had V ed; -:_ hadn't V ed }",
	examples=[""],
	tags=["had V ed", "hadn't V ed", "P.P.", "P.P"],
	mark="#Interm.P.P."
)

s.add_in_id_dict(
	main_db="rules",
	rule="F.P. Действие завершится к указанному моменту;;" +
		 "{+: _ will have V ed; -:_ won't have V ed };;" +
		 "{by the time }",
	examples=[""],
	tags=["will have V ed", "F.P.", "F.P"],
	mark="#Interm.F.P."
)

s.add_in_id_dict(
	main_db="rules",
	rule="it be. Нельзя определить кто выполняет действие;;" +
		 "{it is|was ...; it will be ...}",
	examples=[""],
	tags=["it be", "it.be", "it was", "is was"],
	mark="#Elem.it.be"
)



###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###################################### 15 #####\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


s.add_in_id_dict(
	main_db="tests",
	test="Мне скучно",
	answer=["I'm bored"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)
s.add_in_id_dict(
	main_db="tests",
	test="Я скучаю",
	answer=["I'm boring"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)

s.add_in_id_dict(
	main_db="tests",
	test="Он думает, что театр это скучно",
	answer=["He thinks theatre is boring"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)
s.add_in_id_dict(
	main_db="tests",
	test="Я думаю, что этот фильм очень вдохновляющий",
	answer=["I think this movie is very inspiring"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)
s.add_in_id_dict(
	main_db="tests",
	test="У него есть несколько интересных идей",
	answer=["He has a few interesting ideas"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)
s.add_in_id_dict(
	main_db="tests",
	test="Вы видели тот сюжет о потерянной девочке сегодня утром?*",
	answer=["Have you seen that story about the losed girl this morning?"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)
s.add_in_id_dict(
	main_db="tests",
	test="Я не заинтересован современным исскуством",
	answer=["I'm not interested in modern art"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)
s.add_in_id_dict(
	main_db="tests",
	test="Он был так вдохновлен той выставкой",
	answer=["He was so inspired by that exhibition"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "preposition", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)
s.add_in_id_dict(
	main_db="tests",
	test="Они заинтересованы в покупке вашей квартиры",
	answer=["They're interesting in buying your apartment"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)
s.add_in_id_dict(
	main_db="tests",
	test="У меня очень воодушевляющие новости",
	answer=["I have very encouraging news"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)
s.add_in_id_dict(
	main_db="tests",
	test="Эта музыка такая раздражающая",
	answer=["This music is so annoyed"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)
s.add_in_id_dict(
	main_db="tests",
	test="Я никогда не чувствовал себя так расслабленно*",
	answer=["I've never felt so relaxed"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)
s.add_in_id_dict(
	main_db="tests",
	test="Это была очень неловкая ситуация",
	answer=["It was a very embarrassing situation"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)
s.add_in_id_dict(
	main_db="tests",
	test="Я не считаю, что театр - это скучно",
	answer=["I don't think theatre is boring"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)
s.add_in_id_dict(
	main_db="tests",
	test="Я никогда не чувствовал себя таким смущенным",
	answer=["I've never felt so embarrassing"],
	tags=["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	mark="#Up.Interm.ed.ing"
)

###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###################################### 15 #####\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

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
	if test_or_rule == 1:
		#s.print_any_from_db(main_db="tests", db="test", db_itog="test", vektor_db=["test", "answer", "tags", "mark"])		
		s.print_special_for_test(main_db="tests", db="test", db_itog="test", vektor_db=["test", "answer", "tags", "mark"])		


'''
be	was, were	been	быть, являться
beat	beat	beaten	бить, колотить
become	became	become	становиться
begin	began	begun	начинать
bend	bent	bent	гнуть
bet	bet	bet	держать пари
bite	bit	bitten	кусать
blow	blew	blown	дуть, выдыхать
break	broke	broken	ломать, разбивать, разрушать
bring	brought	brought	приносить, привозить, доставлять
build	built	built	строить, сооружать
buy	bought	bought	покупать, приобретать
catch	caught	caught	ловить, поймать, схватить
choose	chose	chosen	выбирать, избирать
come	came	come	приходить, подходить
cost	cost	cost	стоить, обходиться
cut	cut	cut	резать, разрезать
deal	dealt	dealt	иметь дело, распределять
dig	dug	dug	копать, рыть
do	did	done	делать, выполнять
draw	drew	drawn	рисовать, чертить
drink	drank	drunk	пить
drive	drove	driven	ездить, подвозить
eat	ate	eaten	есть, поглощать, поедать
fall	fell	fallen	падать
feed	fed	fed	кормить
feel	felt	felt	чувствовать, ощущать
fight	fought	fought	драться, сражаться, воевать
find	found	found	находить, обнаруживать
fly	flew	flown	летать
forget	forgot	forgotten	забывать о (чём-либо)
forgive	forgave	forgiven	прощать
freeze	froze	frozen	замерзать, замирать
get	got	got	получать, добираться
give	gave	given	дать, подать, дарить
go	went	gone	идти, двигаться
grow	grew	grown	расти, вырастать
hang	hung	hung	вешать, развешивать, висеть
have	had	had	иметь, обладать
hear	heard	heard	слышать, услышать
hide	hid	hidden	прятать, скрывать
hit	hit	hit	ударять, поражать
hold	held	held	держать, удерживать, задерживать
hurt	hurt	hurt	ранить, причинять боль, ушибить
keep	kept	kept	хранить, сохранять, поддерживать
know	knew	known	знать, иметь представление
lay	laid	laid	класть, положить, покрывать
lead	led	led	вести за собой, сопровождать, руководить
leave	left	left	покидать, уходить, уезжать, оставлять
lend	lent	lent	одалживать, давать взаймы (в долг)
let	let	let	позволять, разрешать
lie	lay	lain	лежать
light	lit	lit	зажигать, светиться, освещать
lose	lost	lost	терять, лишаться, утрачивать
make	made	made	делать, создавать, изготавливать
mean	meant	meant	значить, иметь в виду, подразумевать
meet	met	met	встречать, знакомиться
pay	paid	paid	платить, оплачивать, рассчитываться
put	put	put	ставить, помещать, класть
read	read	read	читать, прочитать
ride	rode	ridden	ехать верхом, кататься
ring	rang	rung	звенеть, звонить
rise	rose	risen	восходить, вставать, подниматься
run	ran	run	бежать, бегать
say	said	said	говорить, сказать, произносить
see	saw	seen	видеть
seek	sought	sought	искать, разыскивать
sell	sold	sold	продавать, торговать
send	sent	sent	посылать, отправлять, отсылать
set	set	set	устанавливать, задавать, назначать
shake	shook	shaken	трясти, встряхивать
shine	shone	shone	светить, сиять, озарять
shoot	shot	shot	стрелять
show	showed	shown, showed	показывать
shut	shut	shut	закрывать, запирать, затворять
sing	sang	sung	петь, напевать
sink	sank	sunk	тонуть, погружаться
sit	sat	sat	сидеть, садиться
sleep	slept	slept	спать
speak	spoke	spoken	говорить, разговаривать, высказываться
spend	spent	spent	тратить, расходовать, проводить (время)
stand	stood	stood	стоять
steal	stole	stolen	воровать, красть
stick	stuck	stuck	втыкать, приклеивать
strike	struck	struck, stricken	ударять, бить, поражать
swear	swore	sworn	клясться, присягать
sweep	swept	swept	мести, подметать, смахивать
swim	swam	swum	плавать, плыть
swing	swung	swung	качаться, вертеться
take	took	taken	брать, хватать, взять
teach	taught	taught	учить, обучать
tear	tore	torn	рвать, отрывать
tell	told	told	рассказывать
think	thought	thought	думать, мыслить, размышлять
throw	threw	thrown	бросать, кидать, метать
understand	understood	understood	понимать, постигать
wake	woke	woken	просыпаться, будить
wear	wore	worn	носить (одежду)
win	won	won	победить, выиграть
write	wrote	written	писать, записывать
'''