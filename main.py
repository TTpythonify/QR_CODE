import qrcode

def generate_website_qr_code(url):
    # Create a QRCode object with specified parameters
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add URL data to the qr code
    qr.add_data(url)
    # Generate qr code
    qr.make(fit=True) 

    my_code = qr.make_image(fill_color="black", back_color="white")
    my_code.save("my_qrcode.png") # Saves to a file
    my_code.show() # Displays qrcode

if __name__ == "__main__":
    
    # When users scan "URL" it takes them to the website
    website_url = "https://www.tiktok.com/@pythonify" 
    
    generate_website_qr_code(website_url)
    print(f"QR code for '{website_url}' ")
