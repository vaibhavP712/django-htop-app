from django.shortcuts import render

import os
import subprocess
import datetime
import pytz  

from django.http import HttpResponse

def htop_view(request):
  
    my_name = "Vaibhav pratap Singh"

    username = os.getlogin() 

    ist_tz = pytz.timezone("Asia/Kolkata")
    ist_time = datetime.datetime.now(ist_tz).strftime("%Y-%m-%d %H:%M:%S %Z")

   
   
    top_output = subprocess.getoutput("top -b -n 1")

    response_html = f"""
    <h1>/htop Endpoint</h1>
    <p><b>Name:</b> {my_name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {ist_time}</p>
    <pre>{top_output}</pre>
    """

    return HttpResponse(response_html)
