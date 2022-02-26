import speech_recognition as speech
import pyttsx3 
import pywhatkit as run
import datetime
import wikipedia
import pyjokes
import webbrowser



# Set-up and initialize speech recognition
listen = speech.Recognizer()
engine = pyttsx3.init()



# Change voice of Alfred
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



# Re-usable function for Alfred to speak
def talk(text):
    '''Converts text to speech'''
    engine.say(text)
    engine.runAndWait()



# Takes voice input from user and processes it
def take_command():
    '''Takes voice command from user and processes it'''
    try:
        with speech.Microphone() as mic:
            # Indicate in terminal that Alfred is listening
            print('Listening...')

            # Takes in voice input and convert to lower-case to standardize text
            voice = listen.listen(mic)
            command = listen.recognize_google(voice)
            command = command.lower()

            # Prepare command variable to repeat w/o "alfred"
            if 'alfred' in command:
                command = command.replace('alfred', '')
    except:
        pass
    return command



# Runs the command
def run_command():
    '''Alfred will run any command based on the input'''
    command = take_command()

    # Opens YouTube if you ask Alfred to play something
    if 'play' in command:
        video = command.replace('play', '')
        talk('playing' + video)
        run.playonyt(video)

    # Repeats time if asked
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    # Gives brief Wikipedia description of people you are curious about
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    
    # Tells a joke if asked
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    # Opens Wall Street Journal if asked for current news
    elif 'news' in command:
            webbrowser.open_new_tab("https://www.wsj.com")
            talk("Here are some recent articles")

    # Opens state of stock market if asked
    elif 'stock market' in command:
            webbrowser.open_new_tab("https://money.cnn.com/data/markets")
            talk("Here's the money")

    # Easter Egg
    elif 'grade' in command:
        talk('You all are getting A\'s! Keep up the good work!')

    elif 'do you like me' in command:
        talk('no')

    # If you don't ask any of the commands above, Alfred will tell you to repeat
    else:
        talk('Can you repeat that?')