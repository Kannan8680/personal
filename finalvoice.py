import speech_recognition as sr
import pyttsx3

# List to store tasks
tasks = []

# Initialize speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def add_task(task):
    """Adds a task and confirms it via speech."""
    tasks.append(task)
    engine.say(f"Task {task} added")
    engine.runAndWait()

def view_tasks():
    """Reads out the list of tasks."""
    if tasks:
        engine.say("Your tasks are:")
        for task in tasks:
            engine.say(task)
    else:
        engine.say("No tasks to show")
    engine.runAndWait()

def remove_task(task_number):
    """Removes a task based on its position in the list."""
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        engine.say(f"Task {removed_task} removed")
    else:
        engine.say("Invalid task number")
    engine.runAndWait()

def recognize_speech():
    """Listens for voice input and converts it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            return command.lower()  # Convert to lowercase for consistency
        except sr.UnknownValueError:
            engine.say("Sorry, I did not understand that")
            engine.runAndWait()
            return None
        except sr.RequestError:
            engine.say("Speech recognition service is unavailable")
            engine.runAndWait()
            return None

def main():
    """Main function to interact with the user via voice commands."""
    while True:
        engine.say("Options: add task, view tasks, remove task, or exit")
        engine.runAndWait()

        command = recognize_speech()
        if not command:
            continue

        if "add task" in command:
            engine.say("What is the task?")
            engine.runAndWait()
            task = recognize_speech()
            if task:
                add_task(task)

        elif "view tasks" in command:
            view_tasks()

        elif "remove task" in command:
            engine.say("Which task number to remove?")
            engine.runAndWait()
            task_number = recognize_speech()
            if task_number and task_number.isdigit():
                remove_task(int(task_number))

        elif "exit" in command:
            engine.say("Exiting...")
            engine.runAndWait()
            break

        else:
            engine.say("Invalid option. Please try again.")
            engine.runAndWait()

if __name__ == "__main__":
    main()
