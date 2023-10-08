import segno
from urllib.request import urlopen

slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=26xUgkTBFTM")
nirvana_url = urlopen("https://media.giphy.com/media/2D8g2rXcWx1DO/giphy.gif")
slts_qrcode.to_artistic(
    background=nirvana_url,
    target="animated_qrcode.gif",
    light="blue",
    scale=5,
)