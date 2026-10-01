import qrcode

url = input("Enter the URL:").strip()
file_path = "E:\\qrcode.png"

if (file_path is None):
    print("file path is not found")

else:
    qr = qrcode.QRCode()
    qr.add_data(url)

    img = qr.make_image()
    img.save(file_path)

    print("qr code was generated")