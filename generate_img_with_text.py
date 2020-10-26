
from PIL import Image, ImageDraw, ImageFont
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Generate_img_with_text(object):
	i = 0
	list_png = set()
	"""docstring for ClassName"""
	def __init__(self, text, background_collor='#599be0', img_weight=150, text_color="white", smesh=0):
		#super(ClassName, self).__init__()
		self.text = text
		self.img_height = 30
		self.img_weight = img_weight
		self.font_size = 20
		self.pix_in_1_letter = 6
		self.background_collor = background_collor
		self.smesh = smesh
		self.text_color = text_color

	def get_width_text(self, text):
		text_temp = "0"*len(text)
		self.draw_text = ImageDraw.Draw(self.im)
		#time.sleep(10)
		#im.close()
		text_width, text_height =  self.draw_text.textsize( text_temp)
		print(text_width, text_height, text)
		return text_width

	def create_image_without_text(self, img_weight):
		self.im = Image.new('RGB', (
			img_weight,
			self.img_height), color=(self.background_collor))
		self.font = ImageFont.truetype('i/AnonymousPro-Bold.ttf', size=self.font_size)
		self.draw_text = ImageDraw.Draw(self.im)
		# Создаем объект со шрифтом
		#self.font = ImageFont.truetype('i/Roboto-Black.ttf', size=self.font_size)

	@staticmethod
	def get_created_instances_count():
		return Generate_img_with_text.i

	def save(self):

		self.create_image_without_text(self.img_weight)
	

		new_width = self.get_width_text( self.text)



		self.smesh = 5
		new_width = new_width*2
		self.create_image_without_text(new_width + self.smesh)

		print("img_weight:", self.img_weight, "new_width:", new_width)

		

		print("-"*25)

		Generate_img_with_text.i += 1
		# добавим тень к тексту
		
		if self.text_color != "black":
			self.draw_text.text(
				(
					self.smesh + 1,#self.img_weight + self.smesh,  
					self.img_height / 2 - 11 + 1  #height
				),
				self.text,
				# Добавляем шрифт к изображению
				font=self.font,
				fill='black')
		
		self.draw_text.text(
			(
				self.smesh,#self.img_weight + self.smesh,  
				self.img_height / 2 - 11  #height
			),
			self.text,
			# Добавляем шрифт к изображению
			font=self.font,
			fill=self.text_color)
		#im.show()

		assert not self.text in Generate_img_with_text.list_png , "I LOVE YOU, i:" + str(Generate_img_with_text.i) + " name:" + self.text

		self.im.save("i/" + self.text + '.png')
		Generate_img_with_text.list_png.add(self.text)

base = [
	#BLUE
	('able to','#D8D8D8', 'black'),
	# BLUE
	('I',0,0),
	('подлежащее', '#599be0', 0),
	# GRAY
	#"+","white","black"),

	("what","#D8D8D8","black"),

	("why","#D8D8D8","black"),

	("глагол","#D8D8D8","black"),

	("to","#D8D8D8","black"),


	# BLUE
	('he',0,0),#подлежащее
	('the hotel',0,0),#подлежащее
	("I'd",0,0),#подлежащее

	("she",0,0),#подлежащее

	("you",0,0),#подлежащее

	("the bulgar",0,0),#подлежащее
	("we'll",0,0),#подлежащее



	# ORANGE
	("had","orange",0),#will

	("will","orange",0),#will

	("must","orange",0),#will

	("could","orange",0),#will

	("couldn't","orange",0),#will

	("should","orange",0),#will

	("shouldn't","orange",0),#will

	("do","orange",0),#will

	("do-does","orange",0),#will
	("won't","orange",0),#will
	("have_","orange",0),#will
	("have-has_","orange", 0),#will



	# ORANGE - RED
	("don't-doesn't","#FF521E", 0),#will
	("called","#FF521E", 0),#will
	("don't","#FF521E", 0),#will
	("heard","#FF521E", 0),#will
	("didn't","#FF521E", 0),#will

	("haven't-hasn't","#FF521E", 0),#will

	("haven't","#FF521E", 0),#will
	("hadn't", "#FF521E", 0),#will

	("mustn't","#FF521E", 0),#will
	("'ve","#FF521E", 0),#will




	# GREEN
	("disappeared","#22a221", 0),

	("гл-в-СОВЕРШ-Й ф","#22a221", 0),
	("locked","#22a221", 0),#will
	("try","#22a221", 0),
	("turned on","#22a221", 0),
	("eavesdropping","#22a221", 0),
	("lost","#22a221", 0),
	("call","#22a221", 0),#will
	("known","#22a221", 0),#will

	("eat","#22a221", 0),#will

	("сказуемое","#22a221", 0),

	("have","#22a221", 0),

	("have-has","#22a221", 0),

	("sweam","#22a221", 0),

	("take","#22a221", 0),

	("глагол_","#22a221", 0),
	("глагол(-ed)","#22a221", 0),
	("touchED","#22a221", 0),

	("we", 0, 0),#подлежащее

	("they", 0, 0),#подлежащее

	("was","#22a221", 0),

	("be","#22a221", 0),

	("wasn't","#22a221", 0),

	("weren't","#22a221", 0),

	("was-were","#22a221", 0),
	("droppedED","#22a221", 0),
	("want","#22a221", 0),
	("left","#22a221", 0), #GREEN
	("movED","#22a221", 0), #GREEN
	("глагол(-ing)","#22a221", 0), #GREEN
	("callING","#22a221", 0), #GREEN

	#RED
	("not","#FF3030", 0),# not


	# PURPL
	("even","#C354FF", 0),
	("perhaps","#C354FF", 0),

	("never","#C354FF", 0),
	("ever","#C354FF", 0),
	("barely","#C354FF", 0),
	("almost","#C354FF", 0),
	("pretty","#C354FF", 0),
	("really","#C354FF", 0),
	("probably","#C354FF", 0),
	("definitely","#C354FF", 0),
	("maybe","#C354FF", 0),
	("already","#C354FF", 0),
	("yet","#C354FF", 0),

	# blye sky
	("they're","#23FFF4", 0),

	# yellow
	("been","yellow", 0),



]
for i in base:
	'''
	if not isinstance(i, list):
		i = list(i)

	try:
		background_collor = i[1]
	except:
		background_collor = '#599be0'

	try:
		text_color = i[2]
	except:
		text_color = 'white'
	i = i[0]
	'''
	assert len(i) == 3, "len i < 3" + str(i)
	background_collor = i[1] if i[1] != 0 else '#599be0'
	text_color = i[2] if i[2] != 0 else 'white'
	i = i[0]
	print(i, background_collor, text_color)
	
	d = Generate_img_with_text(i, background_collor=background_collor, text_color=text_color)
	d.save()
else:
	print("get_created_instances_count:",Generate_img_with_text.get_created_instances_count())

# cd $HOME/simpler;python generate_img_with_text.py
# git add .;git commit -m "add generate img with text";git push origin
# pip freeze > requirements.txt

#print("ALL IS OK!! get_created_instances_count:", Generate_img_with_text.get_created_instances_count())


