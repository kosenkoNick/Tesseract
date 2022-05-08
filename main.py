import pytesseract
import pyperclip as clip
from PIL import ImageGrab
from PIL import Image

img = ImageGrab.grabclipboard()
# if img is not None:
#     img.save('image.png')
# img.show()

# img = Image.open('image.png')
# print(pytesseract.image_to_string(img))
clip.copy(pytesseract.image_to_string)
