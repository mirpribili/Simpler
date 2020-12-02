###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# https://www.youtube.com/watch?v=sUR_fRgqk9Q&feature=youtu.be
#	факт		ходил					хожу			буду ходить
#	процесс		шел						иду				буду идти
#	результат 	сходил(уже вчера)		сходил(уже)		схожу
#	долго		проходил(вчера пол дня)	проходил(3часа)	прохожу

tests = list()
mark = list()
temp = {
	"Simple.1":"[Момент](действие происх. единожды, неск. раз. или никогда)",
	"Simple.2":"[Момент](действие происх. друг за другом)",
	"Simple.condition":"[Момент](состояние)",
	}
#--------------------------- P.S.
mark = ["#Tenses", "P.S.", "ed", "№2 - 21 комбинация времен"]
#:"-= " +
#:mark[1] +
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он играл в футбол каждый вторник" ,#+ temp["Simple.1"],
	"answer":["He played football every Tuesday"],
	"tags":mark,
	"mark":mark[0]
	})
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он играл в футбол, а потом пошел домой" ,#+ temp["Simple.2"],
	"answer":["He played football and then he went home"],
	"tags":mark,
	"mark":mark[0]
	})
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он любил футбол" ,#+ temp["Simple.condition"],
	"answer":["He loved football"],
	"tags":mark,
	"mark":mark[0]
	})
#--------------------------- Pr.S.
mark = ["#Tenses", "Pr.S.", "Vs", "№2 - 21 комбинация времен"]
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он играет в футбол каждый вторник" ,#+ temp["Simple.1"],
	"answer":["He plays football every Tuesday"],
	"tags":mark,
	"mark":mark[0]
	})
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он играет в футбол, а потом идет домой" ,#+ temp["Simple.2"],
	"answer":["He plays football and then he goes home"],
	"tags":mark,
	"mark":mark[0]
	})
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он любит футбол" ,#+ temp["Simple.condition"],
	"answer":["He loves football"],
	"tags":mark,
	"mark":mark[0]
	})
#--------------------------- F.S.
mark = ["#Tenses", "F.S.", "will", "№2 - 21 комбинация времен"]
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он будет играть в футбол каждый вторник" ,#+ temp["Simple.1"],
	"answer":["He will play football every Tuesday"],
	"tags":mark,
	"mark":mark[0]
	})
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он будет играть в футбол, а потом пойдет домой" ,#+ temp["Simple.2"],
	"answer":["He will play football and then he will go home"],
	"tags":mark,
	"mark":mark[0]
	})
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он будет любить футбол" ,#+ temp["Simple.condition"],
	"answer":["He will love football"],
	"tags":mark,
	"mark":mark[0]
	})
#--------------------------- P.C.
temp = {
	"Continuous.1":"[Период](длительное действие, происх. в данный момент)",
	"Continuous.2":"[Период](действия, происх. одновременно)",
	}
mark = ["#Tenses", "P.C.", "ing", "№2 - 21 комбинация времен"]
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он играл в футбол (в тот момент)" ,#+ temp["Continuous.1"],
	"answer":["He was playing football"],
	"tags":mark,
	"mark":mark[0]
	})
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он играл в футбол а она смотрела (в тот момент)" ,#+ temp["Continuous.2"],
	"answer":["He was playing football and she was watching"],
	"tags":mark,
	"mark":mark[0]
	})

#--------------------------- Pr.C.
mark = ["#Tenses", "Pr.C.", "ing", "№2 - 21 комбинация времен"]
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он играет в футбол (в наст. момент)" ,#+ temp["Continuous.1"],
	"answer":["He is playing football"],
	"tags":mark,
	"mark":mark[0]
	})
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он играет в футбол, а она смотрит" ,#+ temp["Continuous.2"],
	"answer":["He is playing football and she is watching"],
	"tags":mark,
	"mark":mark[0]
	})
#--------------------------- F.C.
mark = ["#Tenses", "F.C.", "ing", "№2 - 21 комбинация времен"]
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он будет играть в футбол (в этот момент)" ,#+ temp["Continuous.1"],
	"answer":["He will be playing football"],
	"tags":mark,
	"mark":mark[0]
	})
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он будет играть в футбол, а она будет смотреть" ,#+ temp["Continuous.2"],
	"answer":["He will be playing football and she will be watching"],
	"tags":mark,
	"mark":mark[0]
	})
#--------------------------- P.P.
temp = {
	"Perfect.1":"[Результат](действие происходит до определенного момета. Подчеркивая результат)",
	}
mark = ["#Tenses", "P.P.", "ed", "№2 - 21 комбинация времен"]

tests.append({
	"main_db":"tests",
	"test":"-= " + "Он выйграл пять матчей до того дня" ,#+ temp["Perfect.1"],
	"answer":["He had won five matches untill that day"],
	"tags":mark,
	"mark":mark[0]
	})
#--------------------------- Pr.P.
mark = ["#Tenses", "Pr.P.", "ed", "№2 - 21 комбинация времен"]
tests.append({
	"main_db":"tests",
	"test":"-= " + "Пока что он выйграл пять матчей" ,#+ temp["Perfect.1"],
	"answer":["He has won five matches so far"],
	"tags":mark,
	"mark":mark[0]
	})
#--------------------------- F.P.
mark = ["#Tenses", "F.P.", "ed", "№2 - 21 комбинация времен"]
tests.append({
	"main_db":"tests",
	"test":"-= " + "Он выйграет пять матчей к тому моменту" ,#+ temp["Perfect.1"],
	"answer":["He will have won five matches by then"],
	"tags":mark,
	"mark":mark[0]
	})
#--------------------------- P.P.C.
temp = {
	"Past.Perfect.Continuous.1":"[Длительность](действие происходит до определенного момета. Подчеркивая результат)",
	}
mark = ["#Tenses", "P.P.C.", "ing", "№2 - 21 комбинация времен"]

tests.append({
	"main_db":"tests",
	"test":"-= " + " Он  играл в футбол 10 лет(и продолжил играть)" ,#+ temp["Past.Perfect.Continuous.1"],
	"answer":["He had been playing football for ten years"],
	"tags":mark,
	"mark":mark[0]
	})
#--------------------------- Pr.P.C.
mark = ["#Tenses", "Pr.P.C.", "ing", "№2 - 21 комбинация времен"]

tests.append({
	"main_db":"tests",
	"test":"-= " + " Он  играет в футбол 10 лет(и продолжает играть)" ,#+ temp["Past.Perfect.Continuous.1"],
	"answer":["He has been playing football for ten years"],
	"tags":mark,
	"mark":mark[0]
	})
#--------------------------- F.P.C.
mark = ["#Tenses", "F.P.C.", "ing", "№2 - 21 комбинация времен"]

tests.append({
	"main_db":"tests",
	"test":"-= " + " Он будет играть в футбол 10 лет(и будет продолжать играть)" ,#+ temp["Past.Perfect.Continuous.1"],
	"answer":["He will have been playing football for ten years"],
	"tags":mark,
	"mark":mark[0]
	})

###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###################################### 15 #####\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


tests.append({
	"main_db":"tests",
	"test":"Мне скучно",
	"answer":["I'm bored"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})
tests.append({
	"main_db":"tests",
	"test":"Я скучаю",
	"answer":["I'm boring"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})

tests.append({
	"main_db":"tests",
	"test":"Он думает, что театр это скучно",
	"answer":["He thinks theatre is boring"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})
tests.append({
	"main_db":"tests",
	"test":"Я думаю, что этот фильм очень вдохновляющий",
	"answer":["I think this movie is very inspiring"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})
tests.append({
	"main_db":"tests",
	"test":"У него есть несколько интересных идей",
	"answer":["He has a few interesting ideas"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})
tests.append({
	"main_db":"tests",
	"test":"Вы видели тот сюжет о потерянной девочке сегодня утром?*",
	"answer":["Have you seen that story about the losed girl this morning?"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})
tests.append({
	"main_db":"tests",
	"test":"Я не заинтересован современным исскуством",
	"answer":["I'm not interested in modern art"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})
tests.append({
	"main_db":"tests",
	"test":"Он был так вдохновлен той выставкой",
	"answer":["He was so inspired by that exhibition"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "preposition", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})
tests.append({
	"main_db":"tests",
	"test":"Они заинтересованы в покупке вашей квартиры",
	"answer":["They're interesting in buying your apartment"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})
tests.append({
	"main_db":"tests",
	"test":"У меня очень воодушевляющие новости",
	"answer":["I have very encouraging news"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})
tests.append({
	"main_db":"tests",
	"test":"Эта музыка такая раздражающая",
	"answer":["This music is so annoyed"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})
tests.append({
	"main_db":"tests",
	"test":"Я никогда не чувствовал себя так расслабленно*",
	"answer":["I've never felt so relaxed"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})
tests.append({
	"main_db":"tests",
	"test":"Это была очень неловкая ситуация",
	"answer":["It was a very embarrassing situation"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})
tests.append({
	"main_db":"tests",
	"test":"Я не считаю, что театр - это скучно",
	"answer":["I don't think theatre is boring"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})
tests.append({
	"main_db":"tests",
	"test":"Я никогда не чувствовал себя таким смущенным",
	"answer":["I've never felt so embarrassing"],
	"tags":["#Up.Interm.ed.ing", "ed", "ing", "№1 - отглагольные прилагательные"],
	"mark":"#Up.Interm.ed.ing"
})

###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###################################### 15 #####\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


rules = list()



rules.append({
	"main_db":"rules",
	"rule":"выражает признак | если объект САМ СОВЕРШАЕТ действие;; " +
		 "{прилагательное = глагол + ing};; " +
		 "звук РАЗДРАЖАЕТ вас = раздражающий annoying",
	"examples":["what an embrassing situation?", "who's dating who?"],
	"tags":["отглагольные прилагательные", "глагол + ing", "V + ing", "#Up.Interm.V.ing"],
	"mark":"#Up.Interm.V.ing"
})
rules.append({
	"main_db":"rules",
	"rule":"выражает чувство | если объект ПОДВЕРГАЕТСЯ воздействию;; " +
		 "{прилагательное = глагол + ed (3ф.)};; " +
		 "вас РАЗДРАЖАЕТ звук = вы раздражены annoyed",
	"examples":["brokEN", "relaxed"],
	"tags":["отглагольные прилагательные", "глагол + ed", "V + ed", "#Up.Interm.V.ed"],
	"mark":"#Up.Interm.V.ed"
})

rules.append({
	"main_db":"rules",
	"rule":"Сослагательное наклонение образ. с пом. {would - БЫ};; " +
		 "{вопрос: Wh. would + подлеж. + глагол? Отриц: wouldn't};; " +
		 "C мест-ем сокращ до {'d};;" +
		 "{ if } условие при котором СЕЙСЧАС НАСТУПИЛО БЫ событ.;;" +
		 "{if + усл. в прош. вр. +[be -> were] + событие с would}",
	"examples":["I would do it for you - я !с!делаю это для тебя"],
	"tags":["Сослагательное наклонение", "would", "would + if", "would + if + be", "Present.would",  "#Interm.would"],
	"mark":"#Interm.would"
})

rules.append({
	"main_db":"rules",
	"rule":"Вероятность событий. Если событие ВПОЛНЕ может быть, то may | might | could;;" +
		 "{подлеж. + may | might | could  + глагол} ",
	"examples":["it might rain tomorrow - завтра может пойти дождь"],
	"tags":["Вероятность событий", "событие ВПОЛНЕ может быть", "may might could", "may", "might", "could",  "#Interm.may.might.could"],
	"mark":"#Up.Interm.may.might.could"
})

rules.append({
	"main_db":"rules",
	"rule":"Вероятность событий. Слова, обозначающие уверенность:;; should | must - должны, can't - не может;;" +
		 "{подлеж. + should (shouldn't) | must | can't  + глагол} ;;" +
		 "Вопрос: {should подлеж. + глагол} ",
	"examples":[""],
	"tags":["Вероятность событий", "Слова, обозначающие уверенность", "should must can't", "should", "must", "can't",  "#Interm.should.must.can't"],
	"mark":"#Up.Interm.should.must.can't"
})

# Tenses------------------------
'''
s.add_rule(
	"rule":"Pr.S. действие происходит обычно / в принципе;;" +
		 "{+:_ V,(he)V s; -:_ don't(he)doesn't V};;" +
		 "{+:_ have|has; -:_ don't(he)doesn't have };;" +
		 "{+:_ am|is|are|can; -:_ am|is|are|can not };;" +
		 "Собираться что-то делать;;" +
		 "{+:Wh. am|is|are _ going to V};;" +
		 "Следует, стоит;;" +
		 "{+:_ should V; -:_ shouldn't V};;" +
		 "Обязан;;" +
		 "{+:_ have|has to V; -:_ don't|doesn't have|has to V};;";
	"examples":["I work. She has a work*. We don't work. He doesn't work"],
	"tags":["Pr.S", "V s", "does", "do", "have", "has", "am are is", "can", "am going to", "am going to", "ing", "should V", "have to V", ],
	"mark":"#Elem.Pr.S.do.does.Vs.have.am.are.is.can.going.to"
})
'''
rules.append({
	"main_db":"rules",
	"rule":"Pr.S. действие происходит обычно / в принципе;;" +
		 "{+:_ V,(he)V s; -:_ don't(he)doesn't V};;" +
		 "{+:_ have|has; -:_ don't(he)doesn't have };;" +
		 "{+:_ am|is|are|can; -:_ am|is|are|can not };;",
	"examples":["I work. She has a work*. We don't work. He doesn't work"],
	"tags":["Pr.S", "V s", "does", "do", "have", "has", "am are is", "can",],
	"mark":"#Elem.Pr.S.do.does.Vs"
})

rules.append({
	"main_db":"rules",
	"rule":"Собираться что-то делать;;" +
		 "{+:Wh. am|is|are _ going to V}",
	"examples":[""],
	"tags":["am going to", "am going to", "ing",  ],
	"mark":"#Elem.going.to"
})

rules.append({
	"main_db":"rules",
	"rule":"Следует, стоит;;" +
		 "{+:_ should V; -:_ shouldn't V};;",
	"examples":[""],
	"tags":["should V", ],
	"mark":"#Elem.should"
})
rules.append({
	"main_db":"rules",
	"rule":"Обязан;;" +
		 "{+:_ have|has to V; -:_ don't|doesn't have|has to V};;",
	"examples":[""],
	"tags":["have to V", ],
	"mark":"#Elem.have.to"
})

rules.append({
	"main_db":"rules",
	"rule":"Должен сделать;;" +
		 "{+:_ must V; -:_ mustn't V}",
	"examples":[""],
	"tags":["must V"],
	"mark":"#Elem.must"
})

rules.append({
	"main_db":"rules",
	"rule":"P.S. действие произошло в завершенный промежуток времени;;" +
		 "{+:_ V ed; -:_ did not V };;" +
		 "{+:_ was|were|could; -:_ was|were|could not };;" +
		 "{  ? string ? [ yesterday | last week | once | two days ago] };;",
	"examples":["It was cold. We didn't buy tea. We bought tea. We washed the window.*"],
	"tags":["P.S", "was", "were", "could", "yesterday", "V ed", "did",],
	"mark":"#Elem.P.S.was.were.could"
})


rules.append({
	"main_db":"rules",
	"rule":"Я мог мне удолось;;"  +
		 "{ _ was|were able to V}" ,
	"examples":[""],
	"tags":["was were able to V", "able to V", "was able to V"],
	"mark":"#Elem.was.were.able.to"
})
rules.append({
	"main_db":"rules",
	"rule":"Действие было в планах;;" +
		 "{+:Wh. was|were _ going to V }" ,
	"examples":[""],
	"tags":["was were going to V", "going to V", "was going to V"],
	"mark":"#Elem.was.were.going.to"
})
rules.append({
	"main_db":"rules",
	"rule":"Способности, возможности в прошлом;;" +
		 "{ could V, couldn't V }",
	"examples":[""],
	"tags":["could V", "could V"],
	"mark":"#Elem.could"
})



rules.append({
	"main_db":"rules",
	"rule":"F.S. действие случится в будущем;;" +
		 "{+:_ will V; -:_ won't V };;" +
		 "При каком условии наступит событ. в будущем;;" +
		 "{if + усл. в наст. вр. + событие в будущем};;" +
		 " Я смогу, я буду уметь ;;" +
		 "{+:_ will be able to; -:_ won't be able to}",
	"examples":[""],
	"tags":["F.S", "will", "will if", "will br able to"],
	"mark":"#Elem.F.S.will"
})

rules.append({
	"main_db":"rules",
	"rule":"Pr.C. Совершается прямо сейчас и еще не завершилось;;" +
		 "{+:_ am|is|are V ing; -:_ am|is|are not V ing }",
	"examples":[""],
	"tags":["Pr.C", "V ing", "was V ing", "ing"],
	"mark":"#Elem.Pr.C"
})

rules.append({
	"main_db":"rules",
	"rule":"P.C. одно действие было прервано другим;;" +
		 "{+:_ was|were V ing; -:_ was|were not V ing }",
	"examples":[""],
	"tags":["P.C", "V ing", "was V ing", "were V ing", "ing"],
	"mark":"#Elem.P.C"
})

rules.append({
	"main_db":"rules",
	"rule":"F.C. будет происходить и в указанный момент не завершится;;" +
		 "{+:_ will be V ing; -:_ won't be V ing };;" +
		 "{+:Will there be _ ?; }",
	"examples":[""],
	"tags":["F.C", "V ing", "will be V ing", "will V ing", "be V ing", "ing", "F.C.", "F.C"],
	"mark":"#Elem.F.C"
})

rules.append({
	"main_db":"rules",
	"rule":"Pr.P. (не было) сделано к настоящему моменту (не важно когда!);;" +
		 "{+: _ have|has V ed; -:_ have|has not V ed }",
	"examples":[""],
	"tags":["have V ed", "has V ed", "have ed", "ed", "V ed", "Pr.P", "Pr.P."],
	"mark":"#Interm.Pr.P"
})

rules.append({
	"main_db":"rules",
	"rule":"Pr.P.C. Действие длится неколторое время и продолжается сейчас;;" +
		 "{+: _ have|has been V ing; -:_ have|has been not V ing }",
	"examples":[""],
	"tags":["have been V ing", "have been V ing", "Pr.P.C.", "Pr.P.C"],
	"mark":"#Interm.Pr.P.C."
})


rules.append({
	"main_db":"rules",
	"rule":"P.P. Действие завершилось РАНЕЕ другого события в прошлом;;" +
		 "{+: _ had V ed; -:_ hadn't V ed }",
	"examples":[""],
	"tags":["had V ed", "hadn't V ed", "P.P.", "P.P"],
	"mark":"#Interm.P.P."
})

rules.append({
	"main_db":"rules",
	"rule":"F.P. Действие завершится к указанному моменту;;" +
		 "{+: _ will have V ed; -:_ won't have V ed };;" +
		 "{by the time }",
	"examples":[""],
	"tags":["will have V ed", "F.P.", "F.P"],
	"mark":"#Interm.F.P."
})

rules.append({
	"main_db":"rules",
	"rule":"it be. Нельзя определить кто выполняет действие;;" +
		 "{it is|was ...; it will be ...}",
	"examples":[""],
	"tags":["it be", "it.be", "it was", "is was"],
	"mark":"#Elem.it.be"
})





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


if __name__ == '__main__':
	import sqlite3
	# https://habr.com/en/post/321510/

	#import pypyodbc

	#connection = pypyodbc.connect('Chinook_Sqlite.sqlite')
	connection = sqlite3.connect('Chinook_Sqlite.sqlite')
	"""
	(
		'Driver={SQL Server};'
		'Server=MANOWAR\SQLEXPRESS;' 127.0.0.1
		'Database=nortwind;'
		'uid=username;'
		'pwd=pass'
		)
	"""
	#cursor = connection.cursor()
	cursor = connection.cursor()

	#mySQLquery = ("""
	#            SELECT *
	#""")



	#--------------------------------------------Чтение из базы





	try:
	    # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
	    cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
	    # Получаем результат сделанного запроса
	    results = cursor.fetchall()
	    results2 = cursor.fetchall()
	except sqlite3.DatabaseError as err:
	    print("Error: ", err)
	else:
	    connection.commit()


	#print(results[0])   # [('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',), ('Aaron Goldberg',)]
	print(results2)  # []

	#--------------------------------------------Запись в базу

	# Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
	cursor.execute("insert into Artist values (Null, 'A Aagrh!') ")

	# Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
	connection.commit()

	# Проверяем результат
	cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
	results = cursor.fetchall()
	print(results)  # [('A Aagrh!',), ('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',)]

	#--------------------------------------------Разбиваем запрос на несколько строк в тройных кавычках
	cursor.execute("""
	  SELECT name
	  FROM Artist
	  ORDER BY Name LIMIT 31
	""")
	print("*", cursor.fetchall())
	#--------------------------------------------Объединяем запросы к базе данных в один вызов метода
	








	#-------------------------------------------- delate
	cursor.execute("DELETE FROM Artist WHERE TRUE")
	connection.commit()
	print("*", cursor.fetchall())
	#-------------------------------------------- 


	#Для решения такой задачи можно либо несколько раз вызывать метод курсора .execute()
	'''
	cursor.execute("""insert into Artist values (Null, 'A Aagrh!');""")
	cursor.execute("""insert into Artist values (Null, 'A Aagrh-2!');""")


	#Либо использовать метод курсора .executescript()

	cursor.executescript("""
	 insert into Artist values (Null, 'A Aagrh!');
	 insert into Artist values (Null, 'A Aagrh-2!');
	""")

	'''
	connection.close()

	"""
	1.Устанавливаем и обновляем библиотеки Пайтона:
	sudo apt-get install --reinstall python-pkg-resources
	sudo apt-get install build-essential python-dev

	2.Качаем PyInstaller:
	wget https://github.com/pyinstaller/pyinstaller/releases/download/v3.6/PyInstaller-3.6.tar.gz.asc

	https://github.com/pyinstaller/pyinstaller

	https://github.com/pyinstaller/pyinst...

	3.Раcпаковываем PyInstaller:
	tar -xvf PyInstaller-3.2.tar.gz

	4.Заходим в распакованный PyInstaller:
	cd PyInstaller-3.2

	5.Устанавливаем PyInstaller:
	./pyinstaller.py setup.py

	6.Конвертим ваш .py файл:
	./pyinstaller.py myscript.py


	Ваш бинарный байл будет в /PyInstaller-3.2/myscript/dist
	"""

