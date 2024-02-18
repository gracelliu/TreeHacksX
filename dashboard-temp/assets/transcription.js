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
  const startRecordingButton = document.getElementById('startRecording');
  const stopRecordingButton = document.getElementById('stopRecording');
  const visualizerCanvas = document.getElementById('visualizerCanvas');
  const canvasContext = visualizerCanvas.getContext('2d');
  const memory = document.getElementById('memory');
  const memoryId = document.getElementById('memoryId');
  let mediaRecorder;
  let audioChunks = [];
  let analyser;
  let dataArray;
  let recordingStartTime;
  let visualizerInterval;
  // let timerInterval;

  const userIdButton = document.getElementById('userIdButton');
  const userIdInput = document.getElementById('user-id');

  
  userIdButton.addEventListener('click', () => {
    const user_id = userIdInput.value;
    // Replace 'param1' and 'param2' with your parameter names and values
    const params = {
      user_id: user_id,
    }
    
    // Construct the URL with parameters
    const urlWithParams = new URL('http://localhost:8001/photo/');
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
      memory.src = data.link;
      memoryId.innerHTML = data.id;

    })
    .catch(error => {
      console.error('Error:', error);
    });
  })

  startRecordingButton.addEventListener('click', () => {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        mediaRecorder = new MediaRecorder(stream);
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        analyser = audioContext.createAnalyser();
        const source = audioContext.createMediaStreamSource(stream);
        source.connect(analyser);
        analyser.fftSize = 256;
        dataArray = new Uint8Array(analyser.fftSize / 2);

        mediaRecorder.ondataavailable = event => {
          if (event.data.size > 0) {
            audioChunks.push(event.data);
          }
        };

        mediaRecorder.onstop = () => {
          const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });

          clearInterval(visualizerInterval);
          // clearInterval(timerInterval);

          // You can send the audioBlob to the server here
          sendAudioToServer(audioBlob);
        };

        recordingStartTime = new Date().getTime();
        updateVisualizer();
        visualizerInterval = setInterval(updateVisualizer, 50); // Update visualizer every 50 milliseconds

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

  function updateVisualizer() {
    analyser.getByteFrequencyData(dataArray);
    drawVisualizer();
  }

  function drawVisualizer() {
    canvasContext.clearRect(0, 0, visualizerCanvas.width, visualizerCanvas.height);
    const barWidth = visualizerCanvas.width / dataArray.length;
  
    for (let i = 0; i < dataArray.length; i++) {
      const barHeight = dataArray[i] / 2;
      const x = i * barWidth;
      const y = visualizerCanvas.height - barHeight;
  
      const red = Math.floor((barHeight / 2) + 173); // Transition towards the red component of light blue
      const green = Math.floor((barHeight / 2) + 216); // Transition towards the green component of light blue
      const blue = 230; // Starting from a light blue color
  
      canvasContext.fillStyle = `rgb(${red}, ${green}, ${blue})`;
      canvasContext.fillRect(x, y, barWidth, barHeight);
    }
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