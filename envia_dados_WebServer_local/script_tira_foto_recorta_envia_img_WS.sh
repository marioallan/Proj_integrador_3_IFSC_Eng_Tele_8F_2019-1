# !/bin/bash

fswebcam -d /dev/video0 -r 640x480 --jpeg 85 -D 1 foto.jpg

convert foto.jpg -crop 80x30+300+300 img.jpg

python3 envia_img_unidade_consumidora.py
