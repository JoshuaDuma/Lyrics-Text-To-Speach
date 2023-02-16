import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os
import sys

# Make an HTTP request to the URL containing the lyrics
url = 'https://genius.com/Lil-jon-snap-yo-fingers-lyrics'
response = requests.get(url)

# Use BeautifulSoup to extract the lyrics from the HTML response
soup = BeautifulSoup(response.text, 'html.parser')
lyrics_divs = soup.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-6 YYrds')
if lyrics_divs:
    lyrics = lyrics_divs[0].get_text()
    # Initialize the gTTS object with the lyrics and set the language to English
    tts = gTTS(text=lyrics, lang='en')

    # Save the audio file to disk as "snap_yo_fingers.mp3"
    tts.save('snap_yo_fingers.mp3')

    # Play the audio file using the appropriate command based on the operating system
    if sys.platform == 'win32':
        os.system('start snap_yo_fingers.mp3')
    elif sys.platform == 'darwin':
        os.system('afplay snap_yo_fingers.mp3')
    else:
        print("Unsupported operating system")
else:
    print("No lyrics found")

