from PIL import Image, ImageDraw, ImageFont
import time

class Generate_img_with_text(object):
	"""docstring for ClassName"""
	def __init__(self, text, background_collor='#599be0'):
		#super(ClassName, self).__init__()
		self.text = text
		self.text_temp = "0"*len(self.text)
		self.img_height = 30
		self.img_weight = 150
		self.font_size = 20
		self.pix_in_1_letter = 10
		self.background_collor = background_collor
		self.im = Image.new('RGB', (
			self.img_weight,
			self.img_height), color=(self.background_collor))
		# Создаем объект со шрифтом
		self.font = ImageFont.truetype('Roboto-Black.ttf', size=self.font_size)
		self.draw_text = ImageDraw.Draw(self.im)
		#time.sleep(10)
		#im.close()
		#text_width, text_height = draw_text.textsize(text_temp)
		#print(text_width, text_height)
		
		# добавим тень к тексту
		self.draw_text.text(
		    (
		    	(self.img_weight - self.pix_in_1_letter * len(self.text)) * .5 - self.pix_in_1_letter +1,  
		    	(self.img_height - self.font_size)*.5 - 2 +1 #height
		    ),
		    self.text,
		    # Добавляем шрифт к изображению
		    font=self.font,
		    fill='black')

		self.draw_text.text(
		    (
		    	(self.img_weight - self.pix_in_1_letter * len(self.text)) * .5 - self.pix_in_1_letter,  
		    	(self.img_height - self.font_size)*.5 - 2 #height
		    ),
		    self.text,
		    # Добавляем шрифт к изображению
		    font=self.font,
		    fill='white')
		#im.show()
	def save(self):
		self.im.save(self.text + '.png')

d = Generate_img_with_text("подлежащее")
d.save()

