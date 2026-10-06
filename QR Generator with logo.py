import qrcode

img = qrcode.make('¡Te Amo♥!')
img.save('qr_with_logo.png')  # Save the QR code with the logo
img.show()  # Display the QR code with the logo