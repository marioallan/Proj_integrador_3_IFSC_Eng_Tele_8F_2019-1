#Imagem para string

# encoding=utf8
#import sys
#from importlib import reload

#reload(sys)
#sys.setdefaultencoding('utf8')

import pytesseract as ocr

from PIL import Image # A Python Imaging Library (PIL)

img =Image.open('img.jpg') # ABRE A IMG REFERIDA
#img =Image.open('img.png') # ABRE A IMG REFERIDA

phrase = ocr.image_to_string(img, lang='eng', config='--psm 10') # CONVERTE A IMG PARA STRING COM OS PARAMETROS DE LINGUA INGLESA E PSM 10

arquivo = open('arquivo.txt', 'w')  # CRIAR E ABRE ARQUIVO REFERIDO
arquivo.write(phrase) 		    # GRAVA A CONVERSAO DE IMG PARA STRING PARA O ARQUIVO REFERIDO
arquivo.close() 		    # FECHA E SALVA ARQUIVO

print(phrase) # EXIBE NO TERMINAL A CONVERSAO DE IMG PARA STRING

