import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather
from PIL import Image, ImageTk
import cv2

def Action(data):
    user_data = data

    if "What is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"
    
    elif "Good morning" in user_data or "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning")
        return "Good morning"
    
    elif "Good afternoon" in user_data or "good afternoon" in user_data:
        text_to_speech.text_to_speech("Good afternoon")
        return "Good afternoon"
    
    elif "Good evening" in user_data or "good evening" in user_data:
        text_to_speech.text_to_speech("Good evening")
        return "Good evening"
    
    elif "Hello" in user_data or "hello" in user_data :
        text_to_speech.text_to_speech("Hey,sir or madam how can i help you")
        return "Hey,sir or madam how can i help you"
    
    elif "Hey" in user_data or "hey" in user_data :
        text_to_speech.text_to_speech("Hey,sir or madam how can i help you")
        return "Hey,sir or madam how can i help you"
    
    elif "time now" in user_data or "What is the time now" in user_data:
        current_time=datetime.datetime.now()
        Time = (str)(current_time) + "Hour :", (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time
    
    elif "shut down" in user_data or "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"
    
    elif "play music" in user_data:
        webbrowser.open("https://gaana.com")
        text_to_speech.text_to_speech("ganna.com is ready for you")
        return "ganna.com is ready for you"

    elif "open YouTube" in user_data or "youtube" in user_data:
        webbrowser.open("https://youtube.com")
        text_to_speech.text_to_speech("Youtube.com is ready for you")
        return "Youtube.com is ready for you"
    
    elif "open google" in user_data or "open Google" in user_data:
        webbrowser.open("https://google.com")
        text_to_speech.text_to_speech("google.com is ready for you")  
        return "google.com is ready for you"

    elif "weather" in  user_data or "Weather" in user_data:
        e = weather.weather()
        text_to_speech.text_to_speech(e)  
        return e
    
    elif "what is the temperature" in  user_data:
        e = weather.weather()
        text_to_speech.text_to_speech(e)  
        return e
    
    elif "open whatsapp" in  user_data or "open WhatsApp" in user_data:
        webbrowser.open("https://web.whatsapp.com/")
        text_to_speech.text_to_speech("Ihatsapp is ready for you")  
        return "Whatsapp is ready for you"
    
    elif "open instagram" in  user_data or "pen Instagram" in user_data:
        webbrowser.open("https://www.instagram.com/accounts/login/?hl=en")
        text_to_speech.text_to_speech("Instagram is ready for you")  
        return "Instagram is ready for you"
       
    elif "open times of india news" in  user_data or "open Times of India news" in user_data:
        webbrowser.open("https://timesofindia.indiatimes.com/")
        text_to_speech.text_to_speech("Times of india is ready for you")  
        return "Times of india is ready for you"
    
    elif "rainbow colour" in user_data or "Rainbow colour" in user_data:
        img = cv2.imread('rainbow.png') 
        cv2.imshow('Image', img)
        text_to_speech.text_to_speech(" here are rainbow colours ")
        return "Here are rainbow colours"
     
    else:
        text_to_speech.text_to_speech("i am not able to understand")
        return "I am not able to understand"
    
    