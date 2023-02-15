# Importing the necessary Libraries
from flask_cors import cross_origin
from flask import Flask, render_template, request
from main import text_to_speech
from   mic_source_speech_to_text import runnertime
from speak_all_question_out import introduction

app = Flask(__name__,template_folder ="template")
#app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')


#the chatbot runtime listening and responding to events acordingly.
#runnertime()

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def homepage():
    if request.method == 'POST':
       return render_template('start.html')
    else:
        #introduction()
        return render_template('start.html')
@app.route('/assesment')
#@cross_origin()
def assesment():
    if request.method == 'POST':
        introduction()
        return render_template('assesment.html')
 
if __name__ == "__main__":
    app.run(port=8000, debug=True)

    #text = 'Hello ! My name is processor.'
#gender = 'Male'  # Voice assistant 
#text_to_speech(text, gender)