$(document).ready(function(){
  var questions = [];
  var currentQuestion = 0;
  var score = 0;
  var recognition = new webkitSpeechRecognition();

  //Function to speak a given text using Web Speech API
  function speak(text) {
    var msg = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(msg);
  }

  //Function to ask the current question and start listening for answer
  function askQuestion() {
    if (currentQuestion < questions.length) {
      speak("Question " + (currentQuestion + 1) + ": " + questions[currentQuestion]);
      recognition.start();
      setTimeout(function() { 
        recognition.stop();
        askQuestion();
      }, 10000); //Stop listening after 10 seconds
    } else {
      speak("Assessment complete. Your final score is " + score);
      speak("Thanks for visiting relen");
    }
  }

  //Function to handle the recognition result
  recognition.onresult = function(event) {
    var ans = event.results[0][0].transcript;
    var correctAns = questions[currentQuestion].toLowerCase();
    if (ans.toLowerCase() === correctAns) {
      score++;
      speak("Correct");
    } else {
      speak("Incorrect. The correct answer is " + correctAns);
    }
    currentQuestion++;
  }

  //AJAX request to get the questions from the Flask backend
  $("#start-assessment").click(function(){
    $.ajax({
      url: "/get-questions",
      type: "GET",
      success: function(data) {
        questions = data.questions;
        askQuestion();
      },
      error: function() {
        alert("Error getting questions from server");
      }
    });
  });
});
