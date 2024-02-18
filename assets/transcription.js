// console.log("hi")

if (document.readyState !== 'loading') {
  console.log('document is already ready, just execute code here');
  myInitCode();
} else {
  document.addEventListener('DOMContentLoaded', function () {
      console.log('document was not ready, place code here');
      myInitCode();
  });
}

function myInitCode() {
  const startRecordingButton = document.getElementById('startRecordingButton');
  const stopRecordingButton = document.getElementById('stopRecordingButton');
  const timerDisplay = document.getElementById('timer');
  const userIdButton = document.getElementById('userIdButton');
  const userIdInput = document.getElementById('user-id');

  
  userIdButton.addEventListener('click', () => {
    const user_id = userIdInput.value;
    // Replace 'param1' and 'param2' with your parameter names and values
    const params = {
      user_id: user_id,
    }
    
    // Construct the URL with parameters
    const urlWithParams = new URL('http://localhost:8001/friends/');
    urlWithParams.search = new URLSearchParams(params).toString();
    fetch(urlWithParams, {
      method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
      console.log('Photo id:', data.id, 'Photo link:', data.link);
      const transcriptText = document.getElementById('transcript');
      transcriptText.innerHTML = data.transcription
      audioChunks = []

    })
    .catch(error => {
      console.error('Error:', error);
    });
  })

  let mediaRecorder;
  let audioChunks = [];
  let recordingStartTime;
  
  startRecordingButton.addEventListener('click', () => {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        mediaRecorder = new MediaRecorder(stream);
  
        mediaRecorder.ondataavailable = event => {
          if (event.data.size > 0) {
            audioChunks.push(event.data);
          }
        };
  
        mediaRecorder.onstop = () => {
          const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
          const audioUrl = URL.createObjectURL(audioBlob);
          audioPlayer.src = audioUrl;
          audioPlayer.controls = true;
  
          // You can send the audioBlob to the server here
          sendAudioToServer(audioBlob);
        };
  
        recordingStartTime = new Date().getTime();
        updateTimer();
        setInterval(updateTimer, 1000); // Update timer every second
  
        mediaRecorder.start();
        startRecordingButton.disabled = true;
        stopRecordingButton.disabled = false;
      })
      .catch(error => {
        console.error('Error accessing microphone:', error);
      });
  });
  
  stopRecordingButton.addEventListener('click', () => {
    if (mediaRecorder.state !== 'inactive') {
      mediaRecorder.stop();
      startRecordingButton.disabled = false;
      stopRecordingButton.disabled = true;
    }
  });
  
  function updateTimer() {
    const currentTime = new Date().getTime();
    const elapsedTime = Math.floor((currentTime - recordingStartTime) / 1000);
    timerDisplay.innerText = `Recording time: ${elapsedTime} seconds`;
  }
  
}

function sendAudioToServer(audioBlob) {
  const formData = new FormData();
  formData.append('audio_data', audioBlob);

  fetch('http://localhost:8001/transcribe/', {
    method: 'POST',
    body: formData,
  })
    .then(response => response.json())
    .then(data => {
      console.log('Transcription:', data.transcription);
      const transcriptText = document.getElementById('transcript');
      transcriptText.innerHTML = data.transcription
      audioChunks = []

    })
    .catch(error => {
      console.error('Error:', error);
    });
}