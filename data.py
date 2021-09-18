import time
from datetime import datetime
import webbrowser
import os

#Enter url
url="https://us05web.zoom.us/******"
#Enter start time and end time in 24-hour format
start_time="HH:MM"
end_time="HH:MM"

#registering chrome webbrowser
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("Enter the path of location of chrome.exe"))
current_time=int(datetime.now().strftime("%H%M"))
start_time1=int(start_time[0:2]+start_time[3:5])
end_time1=int(end_time[0:2]+end_time[3:5])
while True:
    if (current_time>=start_time1) and (current_time<=end_time1):              #Comparing if the meeting has already started or is yet to be started
        webbrowser.get('chrome').open(url)                                     #Opening chrome and loading the url

    #You must select the checkbox stating "Always allow us05web.zoom.us to open links of this type in the associated app"
    
        print("The meeting has started and connected")
        time.sleep(5)
        os.system("taskkill /im chrome.exe /f")
        break

    else:
        print("The zoom meeting has not yet started")
        time.sleep(60)
        
