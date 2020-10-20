from PIL import Image, ImageDraw, ImageFont
import time

class Generate_img_with_text(object):
	"""docstring for ClassName"""
	def __init__(self, text, background_collor='#599be0', img_weight=150, text_color="white", smesh=0):
		#super(ClassName, self).__init__()
		self.text = text
		self.text_temp = "0"*len(self.text)
		self.img_height = 30
		self.img_weight = img_weight
		self.font_size = 20
		self.pix_in_1_letter = 10
		self.background_collor = background_collor
		self.smesh = smesh
		self.text_color = text_color
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
		if self.text_color != "black":
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
		    	(self.img_weight - self.pix_in_1_letter * len(self.text)) * .5 - self.pix_in_1_letter + self.smesh,  
		    	(self.img_height - self.font_size)*.5 - 2 #height
		    ),
		    self.text,
		    # Добавляем шрифт к изображению
		    font=self.font,
		    fill=self.text_color)
		#im.show()
	def save(self):
		self.im.save(self.text + '.png')

#d = Generate_img_with_text("+", background_collor="white", text_color="black", smesh=10, img_weight=20)
d = Generate_img_with_text("able to", background_collor="#cac8d9", text_color="black")
#d = Generate_img_with_text("глагол", background_collor="white", text_color="black")
#d = Generate_img_with_text("was-were", "#22a221")
d.save()
# cd $HOME/simpler;python generate_img_with_text.py
# git add .;git commit -m "add generate img with text";git push origin

