import requests
import winsound

print("This code will show you how the random colors sound like.")

response = requests.get("http://api.noopschallenge.com/hexbot")
for i in range(50):

    color = response.json()['colors'][0]['value']
    color = color.replace("#", "")

    print("< " +color + " >")

    frequency = int(color, 16)
    duration = 100  
   #winsound.Beep(frequency, duration)
    winsound.MessageBeep(frequency)
    response = requests.get("http://api.noopschallenge.com/hexbot")