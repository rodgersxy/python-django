import segno

# import segno which is a library for making QR codes
qrcode = segno.make_qr("Changing Qr code, Rodgers Mogaka, Software Engineer")

# Changing the color of only the dark data modules
qrcode.save(
    "green_datadark_qrcode.png",
    scale=5,
    light="lightblue",
    dark="darkblue",
    data_dark="green",
)

# Changing the color of the dark and light data modules
qrcode.save(
    "green_datamodules_qrcode.png",
    scale=5,
    light="lightblue",
    dark="darkblue",
    data_dark="green",
    data_light="lightgreen",
)