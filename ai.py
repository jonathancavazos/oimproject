# import the package and rename it as speech (simplified)
import speech_recognition as speech
import pyttsx3 
import pywhatkit as run
import datetime
import wikipedia
import pyjokes

'''Speech recognition functionality'''
# Create a variable under listen that will be able to recognize and process your voice
# Try block because mic might not work or something
# Except --> pass because we don't want anything to happen if nothing is inputed (however, we could add a command like, "Turn on mic pls")
# In try block, we will use the microphone function included in the package and store it as mic
# voice will 'listen' to the words inputed through the mic
# *****Suggestion: I could probably add the HTML here to display listening instead of terminal, but terminal is to indicate that program is running*****
# listen.recognize_google will convert speech to text; stored under command (user's command) 
# command.lower() to convert the "professor" we are addressing to make sure input is correct
# if statement -- will only print command if you are addressing professor
# then we replace 'professor' with nothing because we don't want alexa in a request like a song

'''Text to speech functionality'''
# initialize pyttsx3 under the variable engine
# voices bock changes the voice to female; the default is male
# engine.say() will repeat whatever is passed through as the argument -- in this case, the professor is introducing themselves and asking a question
# run and wait will run the engine command and wait for the sound to play
# talk() function will make the text to speech more dynamic -- repeats what you say

listen = speech.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

'''
engine.say('Hello, I am your professor. What can I do for you?')
engine.runAndWait()
If we want to introduce them, then keep it
'''

# Takes the input from user
def take_command():
    try:
        with speech.Microphone() as mic:
            print('Listening...')
            voice = listen.listen(mic)
            command = listen.recognize_google(voice)
            command = command.lower()
            if 'aaron' in command:
                command = command.replace('aaron', '')
                # talk(command)
    except:
        pass
    return command

'''Running command functionality'''
# command will store the take_command() function
# if the command has 'play', then we replace it with 'playing'
# playonyt will be play the command through youtube
# strftime() will conver the current time to a string
# %I will convert time to 12 hour; %M will display minutes; %p will tell am or pm
# Addition -- add many sorts of types of questions that will run wikipedia (who, where, what)
# wikipedia will provide a summary of that person with 1 line (or many if specified)
# if you ask professor to a date, they will respond nah fam
# ask professor for a joke, they will get a joke
# add a bunch of easter eggs and features


# Runs the command
def run_command():
    command = take_command()
    # print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        run.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Nah, fam')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'detective' in command:
        talk('Ay, what\'s that sound? I don\'t know. I am messed up, it\'s the deon show')
    elif 'what grade are we getting' in command:
        talk('Jonathan and Deon, you are getting A\'s. You are awesome')
    else:
        talk('Can you repeat that?')


run_command()


# A lot of the prints can be displayed and should be through HTML