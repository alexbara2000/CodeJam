import smtplib


def sendemail(receiver, oldPrice, newPrice, name, link):
    sender_email = "amazondiscountgiver@gmail.com"
    rec_email = receiver
    password = "Qazwsxedc123!"
    oldPrice = oldPrice
    newPrice = newPrice
    name = name
    link = link
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

