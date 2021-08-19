import qrcode

data = '''https://google.com'''
#To generate a qr code
#Method 1
# img=qrcode.make(data)
# img.save('./qrimages/myqrcode.png')

#Method 2
# qr=qrcode.QRCode(version=1,box_size=10,border=5)
# qr.add_data(data)
# qr.make(fit=True)
# img=qr.make_image(fill_color='red',back_color='white')
# img.save('./qrimages/myqrcode1.jpg')

#Decode the QR Code
from pyzbar.pyzbar import decode
from PIL import Image

img=Image.open('./qrimages/myqrcode.png')
result=decode(img)
print(result)