import pyttsx3


def text_to_speech(text, gender):
    """
    Function to convert text to speech
    :param text: text
    :param gender: gender
    :return: None
    """
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    engine = pyttsx3.init()

    # Setting up voice rate
    engine.setProperty('rate', 207)

    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', 27)

    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    engine.say(text)
    engine.runAndWait()
    engine.startLoop(False)
    # engine.iterate() must be called inside externalLoop()
    engine.endLoop(True)
    # engine.endLoop()


#text = 'Hello ! My name is processor.'
#gender = 'Male'  # Voice assistant 
#text_to_speech(text, gender)