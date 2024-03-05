
import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/d4MXCgbY2HLyaf0IhQqD"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "bf64e95f36034eb26c12300117af97b4"
}

data = {
  "text": "Rungta இன்ஸ்டிடியூட் ஆப் டெக்னாலஜி பிலாய், சத்தீஸ்கர் மூலம் ஏற்பாடு செய்யப்பட்டது #smartindiahackathon2023 (மென்பொருள் பதிப்பு) நிறைவடைந்தது!! நாங்கள் 30 நிமிட தூக்கத்துடன் 35 மணிநேரம் நேராக குறியீடு செய்தோம், ஆனால் அது முற்றிலும் மதிப்புக்குரியது. யாருடன் சென்றோம், யாருடன் செல்கிறோம் என்பதில் பெருமை கொள்கிறோம்.",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  },
  "model_id": "eleven_multilingual_v2"  # Add the model_id parameter
}

response = requests.post(url, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
