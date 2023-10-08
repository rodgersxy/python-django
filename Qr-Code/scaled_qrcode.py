import segno

qrcode = segno.make_qr("Scaled Qr code, Rodgers Mogaka, Software Engineer")
qrcode.save("scaled_qrcode.png", scale=4)