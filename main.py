print("Starting Jarvis...")  # Debugging

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import re
import pyjokes
import time

listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    print(f"Jarvis says: {text}")  # Debugging
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    """Listens to user input and returns recognized text."""
    try:
        with sr.Microphone() as origin:
            listener.adjust_for_ambient_noise(origin, duration=1)  # Reduce noise
            print("Listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech).lower()
            
            if "jarvis" in instruction:
                instruction = instruction.replace("jarvis", "").strip()

            print("You said:", instruction)  # Debugging
            return instruction

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand. Please repeat.")
        return ""
    except sr.RequestError:
        print("Network issue. Please check your connection.")
        return ""
    
    
def simple_calculator(expression):
    """Evaluates basic arithmetic expressions safely."""
    try:
        # Replace words with symbols
        expression = expression.replace("plus", "+").replace("minus", "-")\
            .replace("multiply", "*").replace("times", "*")\
            .replace("divided by", "/").replace("divide", "/")\
            .replace("mod", "%").replace("modulus", "%")\
            .replace("square", "**2").replace("cube", "**3")\

        # Extract numbers and operators
        numbers = re.findall(r'[\d\+\-\*/%\(\)\.]+', expression)
        final_expression = "".join(numbers)

        print("Final Expression:", final_expression)  # Debugging

        # Secure evaluation
        result = eval(final_expression)
        return result

    except Exception as e:
        return "Invalid calculation"

def play_Jarvis():
    """Executes commands based on user input."""
    while True:
        instruction = input_instruction()
        if not instruction:
            continue

        if "play" in instruction:
            song = instruction.replace("play", "").strip()
            talk("Playing " + song)
            pywhatkit.playonyt(song)

        elif "time" in instruction:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        elif "date" in instruction:
            date = datetime.datetime.now().strftime('%d/%m/%Y')
            talk("Today's date is " + date)

        elif "how are you" in instruction:
            talk("I am fine, how about you?")

        elif "what is your name" in instruction:
            talk("I am Siri, What can I do for you?")
            
        elif "say about my teacher" in instruction:
            talk("ohh! vijay Sir is Good teacher in presidency University ")
        
        elif "joke" in instruction:
            joke = pyjokes.get_joke()
            talk(joke)
            
        elif "set alarm" in instruction:
           match = re.search(r'\d+', instruction)
           if match:
              alarm_time = int(match.group())  # Extract number (e.g., 7 for 7 AM)
              talk(f"Alarm set for {alarm_time} AM")
              while True:
                 current_time = datetime.datetime.now().hour
                 if current_time == alarm_time:
                   talk("Time to wake up!")
                   break
                 time.sleep(60)  # Check every minute


        elif "who is" in instruction:
            human = instruction.replace("who is", "").strip()
            try:
                info = wikipedia.summary(human, 1)
                print(info)
                talk(info)
            except wikipedia.exceptions.DisambiguationError:
                talk("There are multiple results, please be more specific.")
            except wikipedia.exceptions.PageError:
                talk("Sorry, I couldn't find information on .")
                
        elif "where is" in instruction:
            location = instruction.replace("where is", "").strip()
            talk("Locating " + location)
            pywhatkit.search(location + " location")
        
        elif "calculate" in instruction or any(op in instruction for op in ["plus", "minus", "multiply", "divide", "mod", "square", "cube"]):
            result = simple_calculator(instruction)
            talk(f"The result is {result}")
            
        
        elif "exit" in instruction or "stop" in instruction:
            talk("Good bye!  Have a nice day.")
            break

        else:
            talk("Please repeat. Can you say Loudly")

play_Jarvis()
