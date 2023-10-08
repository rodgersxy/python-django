import segno

qrcode = segno.make_qr("bordeerless Qr code")
qrcode.save("borderless_qrcode.png", scale=5, border=0)