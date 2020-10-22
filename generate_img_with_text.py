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

base = {
	#GRAY
	'able to':{'background_collor':'#D8D8D8', 'text_color':'black'},
	# BLUE
	'I':None,
	# GRAY
	#"+":{ 'background_collor':"white", "text_color":"black"},

	"what":{ 'background_collor':"#D8D8D8", "text_color":"black"},

	"why":{ 'background_collor':"#D8D8D8", "text_color":"black"},

	"глагол":{ 'background_collor':"#D8D8D8", "text_color":"black"},

	"to":{ 'background_collor':"#D8D8D8", "text_color":"black"},


	# BLUE
	"he":None,#подлежащее
	"I'd":None,#подлежащее

	"she":None,#подлежащее

	"you":None,#подлежащее

	"the bulgar":None,#подлежащее



	# ORANGE
	"had":{ 'background_collor':"orange"},#will

	"will":{ 'background_collor':"orange"},#will

	"must":{ 'background_collor':"orange"},#will

	"could":{ 'background_collor':"orange"},#will

	"couldn't":{ 'background_collor':"orange"},#will

	"should":{ 'background_collor':"orange"},#will

	"shouldn't":{ 'background_collor':"orange"},#will

	"do":{ 'background_collor':"orange"},#will

	"do-does":{ 'background_collor':"orange"},#will



	# GREEN - RED
	"don't-doesn't":{ 'background_collor':"#FF521E"},#will
	"locked":{ 'background_collor':"#FF521E"},#will
	"heard":{ 'background_collor':"#FF521E"},#will

	"haven't-hasn't":{ 'background_collor':"#FF521E"},#will

	"haven't":{ 'background_collor':"#FF521E"},#will

	"mustn't":{ 'background_collor':"#FF521E"},#will



	# GREEN
	"disappeared":{ 'background_collor':"#22a221"},# сказуемое

	"гл-в-СОВЕРШ-Й ф":{ 'background_collor':"#22a221"},# сказуемое

	"try":{ 'background_collor':"#22a221"},# сказуемое



	# GREEN
	"call":{ 'background_collor':"#22a221"},#will

	"eat":{ 'background_collor':"#22a221"},#will

	"сказуемое":{ 'background_collor':"#22a221"},# сказуемое

	"have":{ 'background_collor':"#22a221"},# сказуемое

	"have-has":{ 'background_collor':"#22a221"},# сказуемое

	"sweam":{ 'background_collor':"#22a221"},# сказуемое

	"take":{ 'background_collor':"#22a221"},# сказуемое

	"глагол_":{ 'background_collor':"#22a221"},# сказуемое

	"we":None,#подлежащее

	"they":None,#подлежащее

	"was":{ 'background_collor':"#22a221"},# сказуемое

	"be":{ 'background_collor':"#22a221"},# сказуемое

	"wasn't":{ 'background_collor':"#22a221"},# сказуемое

	"weren't":{ 'background_collor':"#22a221"},# сказуемое

	"not":{ 'background_collor':"#FF3030"},# not

	"was-were":{ 'background_collor':"#22a221"},



	# PURPL
	"even":{ 'background_collor':"#C354FF"},# сказуемое

	"never":{ 'background_collor':"#C354FF"},# сказуемое


}
for i in base:
	try:
		background_collor = base[i]['background_collor']
	except:
		background_collor = '#599be0'

	try:
		text_color = base[i]['text_color']
	except:
		text_color = 'white'

	print(i, background_collor, text_color)
	d = Generate_img_with_text(i, background_collor=background_collor, text_color=text_color)
	d.save()
else:
	print("get_created_instances_count:",Generate_img_with_text.get_created_instances_count())

# cd $HOME/simpler;python generate_img_with_text.py
# git add .;git commit -m "add generate img with text";git push origin
# pip freeze > requirements.txt

#print("ALL IS OK!! get_created_instances_count:", Generate_img_with_text.get_created_instances_count())


