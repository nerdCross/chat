const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.lang = 'en-US';

let currentQuestion = 0;
let score = 0;

function askQuestion(question) {
  const questionContainer = document.getElementById('question-container');
  questionContainer.innerText = question;
  speak(question);

  recognition.start();

  setTimeout(function() {
    recognition.stop();
    checkAnswer();
  }, 5000);
}

function speak(text) {
  const msg = new SpeechSynthesisUtterance();
  msg.text = text;
  window.speechSynthesis.speak(msg);
}

function handleRecognition(event) {
  const answer = event.results[0][0].transcript.trim();
  const question = questions[currentQuestion];

  if (answer.toLowerCase() === question.answer.toLowerCase()) {
    score++;
    speak("Correct!");
  } else {
    speak(`Incorrect! The correct answer is ${question.answer}`);
  }

  currentQuestion++;

  if (currentQuestion === questions.length) {
    displayScore();
    return;
  }

  askQuestion(questions[currentQuestion].question);
}

function checkAnswer() {
  recognition.stop();
  speak("Time's up!");

  const question = questions[currentQuestion];
  speak(`The correct answer is ${question.answer}`);

  currentQuestion++;

  if (currentQuestion === questions.length) {
    displayScore();
    return;
  }

  askQuestion(questions[currentQuestion].question);
}

function displayScore() {
  const scoreContainer = document.getElementById('score-container');
  scoreContainer.innerText = `Your score is ${score} out of ${questions.length}`;
  speak(`Your score is ${score} out of ${questions.length}. Thanks for visiting relen!`);
}

let questions = [];

document.getElementById('start-button').addEventListener('click', function() {
  fetch('/get-questions')
    .then(response => response.json())
    .then(data => {
      questions = data.questions;
      askQuestion(questions[currentQuestion].question);
      speak("Welcome to relen!");
    });
});

recognition.addEventListener('result', handleRecognition);
