from flask import Flask, Response, render_template
import speech_recognition as sr
import pyttsx3
import time
from multiprocessing import Process, Queue

app = Flask(__name__)

questions = [
    "What is your name?",
    "What is your age?",
    "Where are you from?",
    "What do you do for a living?",
    "What are your hobbies?",
    "What is your favorite color?",
    "What is your favorite food?",
    "What is your favorite movie?",
    "What is your favorite song?",
    "What is your favorite book?",
    "Do you have any pets?",
    "What is your favorite animal?",
    "What is your favorite place to visit?",
    "What is your favorite sport?",
    "What is your favorite hobby?",
    "What is your favorite thing to do?",
    "What is your dream vacation?",
    "What is your favorite thing about yourself?",
    "What is one thing you would like to improve about yourself?",
    "What is your greatest accomplishment?"
]

def listen(q):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        while True:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                q.put(text)
                print(f"Speech recognition results: {text}")
            except:
                print("Speech recognition failed")
                
def speak(q):
    engine = pyttsx3.init()
    while True:
        if not q.empty():
            response = q.get()
            while not response:
                engine.say("I'm sorry, I didn't hear your response. Please try again.")
                engine.runAndWait()
                time.sleep(2)
                if not q.empty():
                    response = q.get()
            print(f"User response: {response}")
            engine.say("Thank you for your response.")
            engine.runAndWait()
            yield response

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/interview')
def interview():
    return Response(speak(q), mimetype='audio/x-wav')

if __name__ == '__main__':
    app.run(debug=True)
