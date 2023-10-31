import openai
from pydub import AudioSegment
from decouple import config
import os

openai.api_key = config("OPENAI_API_KEY")

for filename in os.listdir("data"):
    if filename.endswith(".ogg"):
        input_file = os.path.join("data", filename)

        # Load the audio file
        audio_file = AudioSegment.from_ogg(input_file)

        # Export the audio file in MP3 format
        mp3_file = os.path.join("data", filename + ".mp3")
        audio_file.export(mp3_file, format="mp3")

        # Open the MP3 file in read mode
        audio_file = open(mp3_file, "rb")

        # Transcribe the audio file
        whisper_response = openai.Audio.transcribe(
            file=audio_file,
            model="whisper-1",
            language="en",
            temperature=0.5,
        )
        audio_file.close()

        # Print the transcription
        print(whisper_response)