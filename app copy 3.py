# Importing the necessary Libraries
# from flask_cors import cross_origin
from flask import Flask,Response, render_template, redirect, render_template, request,url_for
import speech_recognition as sr
import pyttsx3
import time
from multiprocessing import Process, Queue

#from   mic_source_speech_to_text import runnertime
# from speak_all_question_out import introduction, speakQuestions
# from realtime_assesment import start_assesement

#app = Flask(__name__,template_folder ="template")
app = Flask(__name__, template_folder='template', static_folder='static')


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

#the chatbot runtime listening and responding to events acordingly.
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

@app.route('/',methods=['POST', 'GET'])
def index():
    return render_template('dashboard.html')

@app.route('/interview',methods=['POST', 'GET'])
def interview():
    q = Queue()
    engine = pyttsx3.init()
    engine.say("Welcome! I am an automated interviewer. Please answer the following questions to the best of your ability.")
    engine.runAndWait()
    return Response(speak(q), mimetype='audio/x-wav')








if __name__ == "__main__":
    app.run(port=8000, debug=True)

    #text = 'Hello ! My name is processor.'
#gender = 'Male'  # Voice assistant 
#text_to_speech(text, gender)