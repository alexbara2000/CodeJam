import smtplib


def sendemail():
    sender_email = "amazondiscountgiver@gmail.com"
    rec_email = "alexandrubara2000@gmail.com"
    password = "Qazwsxedc123!"
    oldPrice = 499.99
    newPrice = 256.78
    name = "32 inch Oled screen Samsung TV"
    link = "https://www.amazon.ca/Samsung-UN32N5300AFXZC-Glossy-Canada-Version/dp/B07DW7F2FM/ref=sr_1_2?dchild=1&keywords=samsung+oled+32&qid=1605371286&sr=8-2"
    subject = "A product went on sale!"
    body = "Hello, we wanted to inform you that one of the product you were looking at went on sale. The name of the product is: " + name + ". It used to cost: "+str(oldPrice)+"$, but now it is only: "+str(newPrice)+"$. If you want to buy this product, you can click on this link to bring you to the page.\n"+link+"\n\n\nThank you for choosing amazon discount giver. \nHave a nice day"                
    message = f'Subject: {subject}\n\n{body}'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, password)
    print("Login success")
    server.sendmail(sender_email, rec_email, message)


sendemail()