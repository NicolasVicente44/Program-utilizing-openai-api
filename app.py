#this is an ai chat bot written in python using openais text completion api

import openai #import openai 
import os
import sys
import tkinter as tk #import gui tooling 

# Set OpenAI API key from environment variable
openai.api_key = os.environ['OPENAI_API_KEY']

def get_response():
    # Get user input from the entry widget
    prompt = entry.get()

    # Call OpenAI's API to get a text completion
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text.strip()

    # Add the user prompt and AI response to the chat history
    chat_history.insert(tk.END, "User: " + prompt + "\n")
    chat_history.insert(tk.END, "AI: " + message + "\n\n")

    # Update the label widget with the AI response
    label.config(text=message)

# Create the GUI
root = tk.Tk()
root.title("OpenAI Text Completion")

# Set the size of the GUI window
root.geometry("500x500")

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create the input label and entry widget
input_label = tk.Label(frame, text="Enter your prompt:")
input_label.pack(pady=10)

entry = tk.Entry(frame, width=60)
entry.pack(pady=10)

# Create the button widget to trigger the API call
button = tk.Button(frame, text="Get AI response", command=get_response)
button.pack(pady=10)

# Create the label widget to display the AI response
output_label = tk.Label(frame, text="AI response:")
output_label.pack(pady=10)

label = tk.Label(frame, text="", wraplength=450, justify='left')
label.pack(pady=10)

# Create a text widget and scrollbar for the chat history
chat_history_frame = tk.Frame(frame)
chat_history_frame.pack(pady=10)

chat_history_label = tk.Label(chat_history_frame, text="Chat History:")
chat_history_label.pack()

chat_history = tk.Text(chat_history_frame, height=10, width=60, wrap="word")
chat_history.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(chat_history_frame, command=chat_history.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_history.config(yscrollcommand=scrollbar.set)

# Start the GUI
root.mainloop()
