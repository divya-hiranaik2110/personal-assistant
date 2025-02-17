import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random

# Initialize recognizer
recognizer = sr.Recognizer()
class PersonalAssistant:
    def __init__(self, name="Jarvis"):  # Use double underscores (init_)
        self.name = name  # Fix the missing attribute

        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()

        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Set voice properties
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[0].id)  # Index 0 for male voice
        self.engine.setProperty("rate", 150)  # Speaking rate
        
    def speak(self, text):
        """Convert text to speech"""
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
        
    def listen(self):
        """Listen to user's voice input and convert to text"""
        with self.microphone as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                return command
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
                return ""
            except sr.RequestError:
                print("Error with the speech recognition service.")
                return ""
            
    def process_command(self, command):
        """Process user's command and respond appropriately"""
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
            
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            self.speak(f"Today is {current_date}")
            

        elif "watch" in command:
            watch_term = command.replace("watch", "").strip()
            if watch_term:
                url = f"https://www.youtube.com/watch?q={watch_term}"
                webbrowser.open(url)
                self.speak(f"Searching for {watch_term}")
            else:
                self.speak("What should I watch for?")

        elif "search" in command:
            search_term = command.replace("search", "").strip()
            if search_term:
                url = f"https://www.google.com/search?q={search_term}"
                webbrowser.open(url)
                self.speak(f"Searching for {search_term}")
            else:
                self.speak("What should I search for?")
            
        elif "open" in command:
            app = command.replace("open", "").strip()
            if app:
                self.speak(f"Opening {app}")
                try:
                    os.system(f"start {app}")
                except:
                    self.speak(f"Sorry, I couldn't open {app}")
            else:
                self.speak("Please specify the application to open.")
                
        elif "hello" in command or "hi" in command:
            greetings = ["Hello!", "Hi there!", "Greetings!", "Hey!"]
            self.speak(random.choice(greetings))
            
        elif "bye" in command or "goodbye" in command:
            self.speak("Goodbye! Have a great day!")
            return False
            
        elif "thank you" in command:
            responses = ["You're welcome!", "My pleasure!", "Glad I could help!"]
            self.speak(random.choice(responses))
            
        else:
            self.speak("I'm not sure how to help with that yet.")
            
        return True

    def run(self):
        """Main loop to run the assistant"""
        self.speak(f"Hello, I am {self.name}. How can I help you?")
        
        running = True
        while running:
            command = self.listen()
            if command:
                running = self.process_command(command)


if __name__ == "__main__":
    assistant = PersonalAssistant()  # Ensure instance creation is correct
    assistant.run()
