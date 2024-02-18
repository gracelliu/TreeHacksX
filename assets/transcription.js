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
    console.log(startRecordingButton)
    const stopRecordingButton = document.getElementById('stopRecording');
    const audioPlayer = document.getElementById('audioPlayer');
    let mediaRecorder;
    console.log("domcontentloaded")
    let audioChunks = [];

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