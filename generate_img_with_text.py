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
		self.text_temp = "0"*len(self.text)
		self.img_height = 30
		self.img_weight = img_weight
		self.font_size = 20
		self.pix_in_1_letter = 6
		self.background_collor = background_collor
		self.smesh = smesh
		self.text_color = text_color

	def get_width_text(self, text):
		self.draw_text = ImageDraw.Draw(self.im)
		#time.sleep(10)
		#im.close()
		text_width, text_height =  self.draw_text.textsize( self.text_temp)
		print(text_width, text_height, self.text)
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

		assert self.text not in Generate_img_with_text.list_png , "I LOVE YOU, i:" + str(Generate_img_with_text.i) + " name:" + self.text
		self.im.save("i/" + self.text + '.png')
		Generate_img_with_text.list_png.add(self.text)

	


# GRAY
#d = Generate_img_with_text("+", background_collor="white", text_color="black")
d = Generate_img_with_text("able to", background_collor="#D8D8D8", text_color="black")
d.save()
d = Generate_img_with_text("what", background_collor="#D8D8D8", text_color="black")
d.save()
d = Generate_img_with_text("why", background_collor="#D8D8D8", text_color="black")
d.save()
d = Generate_img_with_text("глагол", background_collor="#D8D8D8", text_color="black")
d.save()
d = Generate_img_with_text("to", background_collor="#D8D8D8", text_color="black")
d.save()

# BLUE
d = Generate_img_with_text("I")#подлежащее
d.save()
d = Generate_img_with_text("he")#подлежащее
d.save()
d = Generate_img_with_text("she")#подлежащее
d.save()
d = Generate_img_with_text("you")#подлежащее
d.save()
d = Generate_img_with_text("the bulgar")#подлежащее
d.save()


# ORANGE
d = Generate_img_with_text("had", "orange")#will
d.save()
d = Generate_img_with_text("will", "orange")#will
d.save()
d = Generate_img_with_text("must", "orange")#will
d.save()
d = Generate_img_with_text("could", "orange")#will
d.save()
d = Generate_img_with_text("couldn't", "orange")#will
d.save()
d = Generate_img_with_text("should", "orange")#will
d.save()
d = Generate_img_with_text("shouldn't", "orange")#will
d.save()
d = Generate_img_with_text("do", "orange")#will
d.save()
d = Generate_img_with_text("do-does", "orange")#will
d.save()
d = Generate_img_with_text("won't", "orange")#will
d.save()


# ORANGE - RED
d = Generate_img_with_text("don't-doesn't", "#FF521E")#will
d.save()
d = Generate_img_with_text("haven't-hasn't", "#FF521E")#will
d.save()
d = Generate_img_with_text("haven't", "#FF521E")#will
d.save()
d = Generate_img_with_text("mustn't", "#FF521E")#will
d.save()
d = Generate_img_with_text("hadn't", "#FF521E")#will
d.save()


# GREEN
d = Generate_img_with_text("disappeared", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("гл-в-СОВЕРШ-Й ф", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("try", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("called", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("heard", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("turned on", "#22a221")# сказуемое
d.save()


# GREEN
d = Generate_img_with_text("call", "#22a221")#will
d.save()
d = Generate_img_with_text("eat", "#22a221")#will
d.save()
d = Generate_img_with_text("сказуемое", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("have", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("have-has", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("sweam", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("take", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("глагол_", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("we")#подлежащее
d.save()
d = Generate_img_with_text("they")#подлежащее
d.save()
d = Generate_img_with_text("was", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("be", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("wasn't", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("weren't", "#22a221")# сказуемое
d.save()
d = Generate_img_with_text("not", "#FF3030")# not
d.save()
d = Generate_img_with_text("was-were", "#22a221")
d.save()


# PURPL
d = Generate_img_with_text("even", "#C354FF")# сказуемое
d.save()
d = Generate_img_with_text("never", "#C354FF")# сказуемое
d.save()
d = Generate_img_with_text("ever", "#C354FF")# сказуемое
d.save()
# cd $HOME/simpler;python generate_img_with_text.py
# git add .;git commit -m "add generate img with text";git push origin
# pip freeze > requirements.txt

#print("ALL IS OK!! get_created_instances_count:", Generate_img_with_text.get_created_instances_count())
print(f"{bcolors.OKGREEN}OK!!{bcolors.ENDC} \nget_created_instances_count: {Generate_img_with_text.get_created_instances_count()}")

