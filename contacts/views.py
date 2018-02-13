from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json
from .models import *
from .decorators import *
from twilio.rest import Client
from collections import *
# Reading data from the JSON file.

json_data = open('staticfiles/contacts.json').read()
data = json.loads(json_data)

# class Data(object):
#     # def __init__(self,id,first_name,last_name,number,ran_num):
#     #     self.id = id
#     #     self.first_name = first_name
#     #     self.last_name = last_name
#     #     self.number = number
#     #     self.ran_num = ran_num
#
#     def __init__(self , obj):
#         self.id = obj['id']
#         self.first_name = obj['first_name']
#         self.last_name = obj['last_name']
#         self.number = obj['number']
#         self.ran_num = obj['ran_num']
#     def __str__(self):
#         return self.first_name


# Function to display the home page
def home(request):
    #fetching all sent OTP records from the Database
    record = Messages.objects.all()
    # data ---> Contains the data from the JSON file.
    # record ===> Contains all the sent OTP's.
    return render(request,'home.html',{'data':data,'record':record})

# Function to Display details of the selected user.
def detail(request,d):
    obj = [i for i in data if i['id'] == int(d)]
    # obj ---> contains data of the selected user from the contacts list
    return render(request,'Details.html',{'obj': obj})


# generate_random_six ---> Decorator to generate random six digit number as OTP
@generate_random_six
# Function to send message
def sendMessage(ran_num,request,e):
    obj = [i for i in data if i['id'] == int(e)]
    obj[0]['ran_num'] = ran_num
    return render(request, 'message.html', {'obj': obj})

def test(request):
    message_sid = request.GET.get('message')
    return HttpResponse(message_sid)
#Funtion to Send data to the corresponding user and save the Message in the Database.

def sent(request):
    if request.method=='POST':
        message1 = request.POST.get("message")
        data = message1 .split()
        name = data[1]+" "+data[2]
        try:
            obj = Messages(comment=message1,created_by=name,otp=data[6])
            # generate account,token,from from twilio by creating an Account
            account = "AC91181e65d2816679dd9b9844077c2130"
            token = "3db543428e41ccc03ce5a18455e9fa02"
            client = Client(account, token)
            # replace the number in to field with the number of the user.
            message = client.messages.create(to="+918882383607",
                                                 from_="+14798884127 ",
            body=message1)
            obj.save()
            return HttpResponse("<h1>Message successfully sent</h1><a href='/'>home</a>")
        except:
            return HttpResponse("<h1>Something Went Wrong</h1> <a href='/'>Home</a>")
    else:
        return HttpResponse("<h1>Something Went Wrong</h1> <a href='/'>Home</a>")
    return HttpResponse("<h1>Something Went Wrong</h1> <a href='/'>Home</a>")
