import streamlit as st
import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit
import pyjokes
import datetime
from io import BytesIO

# Initialize Text-to-Speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Streamlit interface
st.set_page_config(page_title="AI Virtual Assistant", page_icon="🤖")
st.title("🤖 AI Virtual Assistant")
st.write("Speak or type your command, and the assistant will respond!")

# User input option
option = st.radio("Input Mode:", ["Text", "Voice"])

if option == "Text":
    user_input = st.text_input("Enter your command:")
    if st.button("Send"):
        command = user_input.lower()
        
        if 'play' in command:
            song = command.replace('play', '')
            speak(f'Playing {song}')
            st.write(f"Playing **{song}** on YouTube")
            pywhatkit.playonyt(song)
        
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            speak(f'The time is {time}')
            st.write(f"The current time is **{time}**")
        
        elif 'who is' in command or 'what is' in command:
            topic = command.replace('who is', '').replace('what is', '')
            info = wikipedia.summary(topic, sentences=2)
            speak(info)
            st.write(info)
        
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)
            st.write(joke)
        
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            st.write("Goodbye! 👋")
        
        else:
            speak("Searching on Google")
            st.write("Searching on Google...")
            pywhatkit.search(command)

elif option == "Voice":
    st.write("Press the button and speak your command")
    if st.button("Start Listening"):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = r.listen(source)
            try:
                command = r.recognize_google(audio, language='en-in')
                st.write(f"You said: **{command}**")
                
                # Same commands as above
                if 'play' in command:
                    song = command.replace('play', '')
                    speak(f'Playing {song}')
                    st.write(f"Playing **{song}** on YouTube")
                    pywhatkit.playonyt(song)
                
                elif 'time' in command:
                    time = datetime.datetime.now().strftime('%H:%M')
                    speak(f'The time is {time}')
                    st.write(f"The current time is **{time}**")
                
                elif 'who is' in command or 'what is' in command:
                    topic = command.replace('who is', '').replace('what is', '')
                    info = wikipedia.summary(topic, sentences=2)
                    speak(info)
                    st.write(info)
                
                elif 'joke' in command:
                    joke = pyjokes.get_joke()
                    speak(joke)
                    st.write(joke)
                
                elif 'exit' in command or 'quit' in command:
                    speak("Goodbye!")
                    st.write("Goodbye! 👋")
                
                else:
                    speak("Searching on Googlecd")
                    st.write("Searching on Google...")
                    pywhatkit.search(command)
            
            except Exception as e:
                st.write("Sorry, could not recognize your voice. Please try again!")
