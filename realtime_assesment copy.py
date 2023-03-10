import speech_recognition as sr
import pyttsx3
from multiprocessing import Process, Queue

# Define a function to perform calculations based on user's speech
def calculate(queue):
    while True:
        # Wait for user's speech to be put into the queue
        user_speech = queue.get()

        # Convert user's speech to lowercase and remove spaces
        user_speech = user_speech.lower().replace(" ", "")

        # Perform calculations based on user's speech
        if "add" in user_speech:
            nums = user_speech.split("add")[1].split("and")
            result = sum([int(num) for num in nums])
            print(f"The result is {result}")
        elif "subtract" in user_speech:
            nums = user_speech.split("subtract")[1].split("from")
            result = int(nums[1]) - int(nums[0])
            print(f"The result is {result}")
        else:
            print("I didn't understand what you said.")

# Define a function to listen to user's speech and put it into a queue
def listen(queue):
    # Initialize speech recognizer and text-to-speech engine
    r = sr.Recognizer()
    engine = pyttsx3.init()

    # Set up microphone input
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        while True:
            # Listen to user's speech
            print("Listening...")
            audio = r.listen(source)

            # Convert user's speech to text and put it into the queue
            try:
                user_speech = r.recognize_google(audio)
                print(f"You said: {user_speech}")
                queue.put(user_speech)
            except:
                print("Sorry, I didn't catch that.")

# Set up multiprocessing
if __name__ == "__main__":
    queue = Queue()
    p1 = Process(target=listen, args=(queue,))
    p2 = Process(target=calculate, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
