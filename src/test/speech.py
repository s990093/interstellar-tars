import pyttsx3

class Speech:
    def __init__(self, voice_id='com.apple.eloquence.en-US.Grandpa', rate=166, volume=0.8):
        # Initialize the TTS engine
        self.engine = pyttsx3.init()
        
        # List all available voices
        voices = self.engine.getProperty('voices')
        
        # Set the voice to the specified choice
        self.engine.setProperty('voice', voice_id)
        
        # Set speaking rate and volume
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
    
    def speak(self, message):
        # Speak the provided message
        self.engine.say(message)
        self.engine.runAndWait()

# # Example usage:
# if __name__ == "__main__":
#     tars = TARS()
#     tars.speak("Hello, I am TARS. How can I assist you today?")
