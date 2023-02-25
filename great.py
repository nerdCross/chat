import speech_recognition as sr
import pyttsx3
from multiprocessing import Process, Queue
from answer_matching_production import convert_json_answers_to_list , score_the_user
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
                
def calculate(q):
    engine = pyttsx3.init()
    while True:
        if not q.empty():
            text = q.get()
            try:
                # Attempt to parse a math expression from the recognized text
                convert_json_answers_to_list()
                score = score_the_user()
                result = (text)
                print(f"Calculated result: {result}")
                engine.say(result)
                engine.runAndWait()
            except:
                print("Calculation failed")
                
if __name__ == '__main__':
    q = Queue()
    listen_process = Process(target=listen, args=(q,))
    calculate_process = Process(target=calculate, args=(q,))
    listen_process.start()
    calculate_process.start()
    listen_process.join()
    calculate_process.join()
