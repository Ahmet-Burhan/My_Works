from email import message
import smtplib
server = smtplib.SMTP("smtp.gmail.com",587)  #default mail submission portnumber 587
print(server.starttls())  #server i startlayalim
print(server.login("boztasburhan","1453burya"))


adresim = ["boztasburhan@gmail.com"]
message = "Test mail"
print(server.sendmail("boztasburhan@gmail.com",adresim,message,))
print(server.quit())