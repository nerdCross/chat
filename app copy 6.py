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




data = [
  {
    "answer": "Doing Presentations Like A Pro ",
    "question": "What is the name of the course that will help you elevate your presentation game?"
  },
  {
    "answer": "elevate your presentation game ",
    "question": "What course is designed to help you elevate your presentation game context?"
  },
  {
    "answer": "academic presentations ",
    "question": "What is the context of academic presentations?"
  },
  {
    "answer": "knowledge, creation, as they facilitate cross-fortalization of ideas ",
    "question": "What is the purpose of a poster presentation?"
  },
  {
    "answer": "poster and oral presentations ",
    "question": "What are the two main types of presentations?"
  },
  {
    "answer": "poster presentations ",
    "question": "What is the context of a poster presentation?"
  },
  {
    "answer": "format, content, organization, words, fonts, colors, and printing needed for a good poster ",
    "question": "What is the format, content, organization, words, fonts, colors, and printing needed for a good poster?"
  },
  {
    "answer": "visual representation of an idea or research finding to be disseminated to an audience ",
    "question": "What is a poster a visual representation of?"
  },
  {
    "answer": "A zero paper size ",
    "question": "What is the most common standard size of a poster?"
  },
  {
    "answer": "33.1 by 46.8 inches ",
    "question": "What is the typical size of a poster?"
  },
  {
    "answer": "5 minutes ",
    "question": "In a poster presentation, the presenter would usually take about 5 minutes to speak to the poster and then stand by for questions."
  },
  {
    "answer": "number of questions a poster presentation generates ",
    "question": "What can be a deciding factor for the success of a poster presentation?"
  },
  {
    "answer": "you will know how successful your poster presentation is if it generates a lot of questions afterwards ",
    "question": "How successful is a poster presentation if it generates a lot of questions afterwards?"
  },
  {
    "answer": "interesting to people ",
    "question": "What type of context does \"interesting to people\" refer to?"
  },
  {
    "answer": "presenter ",
    "question": "What is the role of a presenter in a presentation?"
  },
  {
    "answer": "you are allowed to choose what you like ",
    "question": "When you are allowed to choose what you like context: \" Welcome to the second lesson of the course, Doing Presentations Like A Pro."
  },
  {
    "answer": "downloaded online and adapted for use as a property ",
    "question": "What kind of templates can be downloaded online and adapted for use as a property context: \" Welcome to the second lesson of the course, Doing"
  },
  {
    "answer": "you adjust them to your own taste ",
    "question": "How do you edit templates of format you find, you adjust them to your own taste context: \" Welcome to the second lesson of the course, Doing"
  },
  {
    "answer": "edit templates of format you find, you adjust them to your own taste ",
    "question": "How do you edit templates of format you find?"
  },
  {
    "answer": "title, summary, brief introduction, in-s and objectives, methodology, result, discussion and conclusion ",
    "question": "What is the title of a poster?"
  },
  {
    "answer": "ensure you do justice to each part ","question": "How do you ensure you do justice to each part of a poster?"
  },
  {
    "answer": "maximum impact ",
    "question": "What is the meaning of a maximum impact poster?"
  },
  {
    "answer": "real game changer ",
    "question": "What can be a real game changer context?"
  },
  {
    "answer": "words should only be used when necessary ",
    "question": "When should words be used when necessary context?"
  },
  {
    "answer": "too many words or words in unnecessary places in your poster can be be used whenever necessary ",
    "question": "How can words be used in unnecessary places in a poster?"
  }
]





questions = []




def convert_json_Question_to_list():
  for item in data:
   for item in data:
    if len(item['question']) > 0:
      if '?' in item['question']:
        print("The question contains a question mark.")
        questions.append(item['question'])
        print("question: ", questions)
    else:
        pass
    
    


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
                


@app.route('/',methods=['POST', 'GET'])
def index():
    return render_template('dashboard.html')

@app.route('/interview',methods=['POST', 'GET'])
def interview():
    convert_json_Question_to_list()
    
    q = Queue()
    listen_process = Process(target=listen, args=(q,))
    speak_process = Process(target=speak, args=(q,))
    listen_process.start()
    speak_process.start()
    listen_process.join()
    speak_process.join()


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


# def speak(q):
#     engine = pyttsx3.init()
#     engine.say("Welcome! I am an automated interviewer. Please answer the following questions to the best of your ability.")
#     engine.runAndWait()
#     while True:
#         if not q.empty():
#             response = q.get()
#             while not response:
#                 engine.say("I'm sorry, I didn't hear your response. Please try again.")
#                 engine.runAndWait()
#                 time.sleep(2)
#                 if not q.empty():
#                     response = q.get()
#             print(f"User response: {response}")
#             engine.say("Thank you for your response.")
#             engine.runAndWait()
#             # yield response
def speak(q):
    engine = pyttsx3.init()
    engine.say("Welcome! I am an automated interviewer. Please answer the following questions to the best of your ability.")
    engine.runAndWait()
    while True:
        for question in questions:
            engine.say(question)
            engine.runAndWait()
            time.sleep(2)
            if not q.empty():
                response = q.get()
                print(f"User response: {response}")
                engine.say("Thank you for your response.")
                engine.runAndWait()




if __name__ == "__main__":
    app.run(port=8000, debug=True)
    

# this code parse the json and extracts the questions then perform the interview