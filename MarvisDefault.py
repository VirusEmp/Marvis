import webbrowser
import smtplib
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
import pyttsx3
import wolframalpha

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('RXYY99-32K8PJ9X2E')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices [len(voices)-3].id)

def speak(audio):
    print('Marvis :' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetme():
    ch = int(datetime.datetime.now().hour)
    if ch > 0 and ch < 12:
        speak('Good Morning')

    if ch >= 12 and ch < 18:
        speak('Good Afternoon')

    if ch > 18 and ch != 0:
        speak('Good Evening')
greetme()

speak('I am your voice assistant MARVIS!')
speak('How are you?')

def mycommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-US')
        print('User: ' + query + '\n')
    except sr.UnknownValueError:
        speak('Sorry!! i couldn\'t hear you clearly')
        speak('Please type your response')
        query = str(input('Reponse: '))
    return query

if __name__== '__main__':

    while True:
        query = mycommand()
        query = query.lower()

        if 'open youtube' in query:
            speak('Okay!!..Opening Youtube..')
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            speak('Okay!!...Opening Google')
            webbrowser.open('www.google.com')
        elif 'open gmail' in query:
            speak('Okay!!...Opening Gmail')
            webbrowser.open('www.gmail.com')
        elif 'I am fine thank you' or 'fine thank you' or 'doing good' in query:
            speak('Good to know')
            speak('How may i help you?')
        elif 'Not fine' or 'I am sick' or 'I don\'t feel so good' or 'having a bad day' in query:
            speak('Sorry about that')
            speak('How may i make you feel better?')
        elif 'open yahoomail' in query:
            speak('Okay!!..Opening Yahoomail')
            webbrowser.open('www.yahoomail.com')
        elif 'open facebook' in query:
            speak('Okay!!..Opening facebook')
            webbrowser.open('www.facebook.com')
        elif 'i want to send a mail' in query:
            speak('through what mail service?')
            if 'gmail' or 'yahoomail' in query:
                speak('who is the recipient?')
                recipient = mycommand()
                speak('What do i say in the mail?')
                content = mycommand()

                server = smtplib.SMTP('smtp.gmail.com', 587) or smtplib.SMTP('smtp.yahoomail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('Marvelking78', 'GOOGLEACCOUNT1994') or ('Angelmarve', 'YAHOOACCOUNT1994')
                server.sendmail('Marvelking', recipient, content) or ('Angelmarve', recipient, content)
                server.close()
                speak('Email sent!')
            else:
                speak('Sorry, I am unable to send your message at this moment')
        elif 'nothing' or 'abort' or 'Stop' in query:
            speak('Okay!')
            speak('Goodbye, Have a Nice day!!')
            sys.exit()
        elif 'play music' in query:
            music_folder = 'C:\\Users\\Marvellous\\Music\\Xtain\\'
            music = music_folder + '.mp3'
            os.system(music)

            speak('Okay, Enjoy the music!!')

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results) .text
                    speak('Got it!!')
                    speak('WOLFRAM-ALPHA says:- ')
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it!!')
                    speak('WIKIPEDIA says:- ')
                    speak(results)
            except:
                webbrowser.open('www.google.com')

        speak('Next command!!')

