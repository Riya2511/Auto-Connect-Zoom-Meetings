import time
from datetime import datetime
#from pynput.keyboard import Controller, Key
#mouse= Controller()
import webbrowser
import os
#from data import lst
url="https://us05web.zoom.us/j/5282133308?pwd=Qm9nck5DZ29lbW8wZ2hqTkg3cXhxQT09"
#keyboard = Controller()
start_time="21:25"
end_time="21:50"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Users\\V S Jain\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"))
current_time=int(datetime.now().strftime("%H%M"))
start_time1=int(start_time[0:2]+start_time[3:5])
end_time1=int(end_time[0:2]+end_time[3:5])
if (current_time>=start_time1) and (current_time<=end_time1):              #Comparing if the meeting has already started or is yet to be started
    webbrowser.get('chrome').open(url)                                     #Opening chrome and loading the url

    #You must select the checkbox stating "Always allow us05web.zoom.us to open links of this type in the associated app"
    
    print("The meeting has started and connected")
    time.sleep(5)
    os.system("taskkill /im chrome.exe /f")

else:
    print("The zoom meeting has not yet started")