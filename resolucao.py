from PIL import Image
import numpy as np

def getGreenPixels(im):
  im = im.convert("RGB") # Convertendo as representações de pixels para RBG
  w,h = im.size # Pegando largura e altura da imagem
  colors = im.getcolors(w*h) # Pegando as cores de cada pixel
  colordict = { x[1]:x[0] for x in colors } # Montando o dicionário com as cores como chave e a quantidade como valor
  for i in colordict:
    if i != (255, 255, 255) and i != (0, 0, 0): # Desconsiderando pixels brancos e pretos
      print("Número de pixels verdes: ", colordict[i])

def getHideMessage(im):
  # Load and reshape the image file
  img = np.array(im)
  shp = img.shape
  the_bytes = img.reshape(np.prod(shp))
  # Extract the message
  char_codes, n, c, m = [], 0, 0, 1
  for byt in the_bytes:
    if byt & 1:
      c += m
    n += 1
    m <<= 1
    if n % 8 == 0:
      if c == 4:
        break
      char_codes.append(c)
      c, m = 0, 1
  s = "".join(map(chr, char_codes))
  print("Mensagem secreta encontrada: ", s)

im = Image.open('Syngenta.bmp')
print("------------------------------")
print("1.")
getGreenPixels(im)
print("------------------------------")
print("2.")
getHideMessage(im)
print("------------------------------")