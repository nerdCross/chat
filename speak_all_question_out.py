
from main import text_to_speech

import time


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
#========function to loop through the dataset and print out only the questions.==========
#for item in data:
 #  for item in data:
  #  if len(item['question']) > 0:
   #     #print("Question: ", item['question'])
    #    print(item['question'])
    #else:
    #    pass
#======================================================================================

#========function to loop through the dataset and compare the questions with the answers.==========

#========function to loop through the dataset and compare the questions with the answers.==========

#==============================================================================================


def speakQuestions():
  for item in data:
   for item in data:
    if len(item['question']) > 0:
        #print("Question: ", item['question'])
        #speak the question

        #print(item['question'])
        text = item['question']
        gender = 'Male'
        print(item['question'])
        #insert the inner html here.
        text_to_speech(text, gender)
        #speak the question
        
        time.sleep(20)
        
    else:
        pass
    
#speakQuestions()
def introduction():
  text = "Welcome to Relen, kindly listen to the audio lecture below, to start the assesement, type Start into the text box below, each question will take 20 seconds before the next, goodluck!."
  gender = 'Male'
  #incert the inner html here.
  text_to_speech(text, gender)

#introduction()


def check_the_ans():
  pass