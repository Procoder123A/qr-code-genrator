import pyqrcode
import png
from pyqrcode import QRCode
S="https://tlauncher.org/en/"
URL=pyqrcode.create(S)
URL.svg('Minecraft.svg',scale=8)
URL.png('Fortnite.png',scale=6)