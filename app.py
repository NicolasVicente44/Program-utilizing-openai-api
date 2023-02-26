import openai
import os
import tkinter as tk

openai.api_key = os.environ['OPENAI_API_KEY']

def get_response():
    prompt = entry.get()
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text.strip()

    chat_history.insert(tk.END, "User: " + prompt + "\n")
    chat_history.insert(tk.END, "AI: " + message + "\n\n")

    label.config(text=message)

root = tk.Tk()
root.title("OpenAI Text Completion")

# Set the size of the GUI window
root.geometry("600x700")

# Set the background color of the GUI
root.configure(bg="#f9f9f9")

# Create a frame to hold the widgets
frame = tk.Frame(root, bg="#f9f9f9")
frame.pack(padx=50, pady=50)

# Create the input label and entry widget
input_label = tk.Label(frame, text="Enter your prompt:", font=("Helvetica", 16), bg="#f9f9f9")
input_label.pack(pady=10)

entry = tk.Entry(frame, width=60, font=("Helvetica", 14))
entry.pack(pady=10)

# Create the button widget to trigger the API call
button = tk.Button(frame, text="Get AI response", font=("Helvetica", 16), bg="#4CAF50", fg="#ffffff", command=get_response)
button.pack(pady=20)

# Create the label widget to display the AI response
output_label = tk.Label(frame, text="AI response:", font=("Helvetica", 16), bg="#f9f9f9")
output_label.pack(pady=10)

label = tk.Label(frame, text="", font=("Helvetica", 14), wraplength=500, justify='left', bg="#f9f9f9")
label.pack(pady=10)

# Create a text widget and scrollbar for the chat history
chat_history_frame = tk.Frame(frame, bg="#f9f9f9")
chat_history_frame.pack(pady=10)

chat_history_label = tk.Label(chat_history_frame, text="Chat History:", font=("Helvetica", 16), bg="#f9f9f9")
chat_history_label.pack()

chat_history = tk.Text(chat_history_frame, height=10, width=60, wrap="word", font=("Helvetica", 14))
chat_history.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(chat_history_frame, command=chat_history.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_history.config(yscrollcommand=scrollbar.set)

root.mainloop()
