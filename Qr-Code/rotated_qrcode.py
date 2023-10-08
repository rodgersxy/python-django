import segno

qrcode = segno.make_qr("Rotated qr code, Rodgers Mogaka, Software Engineer")

qrcode_rotated = qrcode.to_pil(
    scale=5, light="lightblue", dark="green"
).rotate(45, expand=True)
qrcode_rotated.save("formatted_rotated_qrcode.png")