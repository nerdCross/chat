
// let timeLeft = 60;

// // Get the timer span element
// const timerSpan = document.querySelector('.timer');

// // Update the timer span every second
// const timerInterval = setInterval(() => {
//   // Decrement the time left by one second
//   timeLeft--;

//   // Update the timer span with the new time left
//   timerSpan.textContent = timeLeft;

//   // Stop the timer when time runs out
//   if (timeLeft === 0) {
//     clearInterval(timerInterval);
//   }
// }, 1000);

// function count_down() {
//   console.log("Button clicked!");
//   let timeLeft = 50;

// // Get the timer span element
// const timerSpan = document.querySelector('.timer');

// // Update the timer span every second
// const timerInterval = setInterval(() => {
//   // Decrement the time left by one second
//   timeLeft--;

//   // Update the timer span with the new time left
//   timerSpan.textContent = timeLeft;

//   // Stop the timer when time runs out
//   if (timeLeft === 0) {
//     clearInterval(timerInterval);
//   }
// }, 1000);
// }

//the following piece of code uses ajax

{/* <script>
function speak() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/speak', true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 && xhr.status == 200) {
      console.log(xhr.responseText);
      var outputDiv = document.getElementById('output');
      outputDiv.innerHTML += '<p>' + xhr.responseText + '</p>';
    }
  };
  xhr.send();
}
</script> */}


const audioButton = document.querySelector('.audio-button');

audioButton.addEventListener('click', () => {
  audioButton.classList.toggle('animate');
});

