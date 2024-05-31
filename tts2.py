from gtts import gTTS

# Specify the text to convert to audio
text = "Python is amazing!"

# Create a gTTS object
tts = gTTS(text)

# Save the audio to a file
tts.save("output.mp3")
