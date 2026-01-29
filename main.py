# NORMAL METHOD :
import qrcode
qr=qrcode.make("URL")
qr.save("normal.png")

# ADVANCED METHOD :-

# import qrcode
# qr = qrcode.QRCode(
#     version=2,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4
# )
# qr.add_data('https://maps.app.goo.gl/BfFLDkxqNPHjDh4s6?g_st=aw')
# qr.make(fit=True)

# img = qr.make_image(fill_color="BLACK", back_color="WHITE")
# img.save("qrcode.png")





