from PIL import Image, ImageDraw, ImageFont
import time


im = Image.new('RGB', (150,30), color=('#599be0'))
# Создаем объект со шрифтом
font = ImageFont.truetype('Roboto-Black.ttf', size=20)
draw_text = ImageDraw.Draw(im)
draw_text.text(
    (12, 1),
    'подлежащее',
    # Добавляем шрифт к изображению
    font=font,
    fill='white')
#im.show()

#time.sleep(10)
#im.close()

im.save('test.png')

