import segno

qrcode = segno.make_qr("blue Qr code, Rodgers Mogaka, Software Engineer")

# Without changing the color of the quiet zone
qrcode.save("darkblue_qrcode.png", scale=5, dark="darkblue")

# With quiet zone
qrcode.save(
    "darkblue_qrcode.png", scale=5, dark="darkblue", quiet_zone="maroon"
)