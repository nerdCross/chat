# Importing the necessary Libraries
from flask_cors import cross_origin
from flask import Flask, redirect, render_template, request,url_for
from main import text_to_speech
#from   mic_source_speech_to_text import runnertime
from speak_all_question_out import introduction, speakQuestions
from realtime_assesment import start_assesement

#app = Flask(__name__,template_folder ="template")
app = Flask(__name__, template_folder='template', static_folder='static')


#the chatbot runtime listening and responding to events acordingly.
#runnertime()


@app.route('/', methods=['POST', 'GET'])
def homepage():
    
    return render_template('start.html')
   



@app.route('/score')
def display_score():
    score = 90
    return render_template('score.html', score=score)

    
@app.route('/play_intro', methods=['GET', 'POST'])
def play_intro():
    # Code to be executed when the form is submitted
    # ...
    introduction()
    
    return redirect(url_for('assesment'))



@app.route('/start', methods=['GET', 'POST'])
def start():
    # Code to be executed when the form is submitted
    # ...


    #return start_assesement()

    return speakQuestions()
    






@app.route('/assesment')
def assesment():
    # Code to be executed when the user is redirected to this page
    # ...
    #introduction()

   # return render_template('assesment.html')
    #introduction()
    
    #speakQuestions()
    return render_template('dashboard.html')
    



if __name__ == "__main__":
    app.run(port=8000, debug=True)

    #text = 'Hello ! My name is processor.'
#gender = 'Male'  # Voice assistant 
#text_to_speech(text, gender)