import tkinter as tk
from tkinter import scrolledtext
import requests
import threading

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("chatbots")
        self.root.geometry("400x500")

        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(padx=10, pady=10, fill=tk.X)

        self.entry_text = tk.Entry(self.entry_frame, width=50)
        self.entry_text.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)

        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def display_message(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}: {message}\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.yview(tk.END)

    def send_message(self):
        user_input = self.entry_text.get()
        if user_input.strip():
            self.display_message("User", user_input)
            threading.Thread(target=self.get_response, args=(user_input,)).start()
        self.entry_text.delete(0, tk.END)

    def get_response(self, user_input):
        try:
            response = requests.post("http://127.0.0.1:5001/chat", json={"message": user_input})
            response_data = response.json()
            reply = response_data.get("reply", "I didn't understand that.")
            self.display_message("Bot", reply)
        except requests.exceptions.RequestException:
            self.display_message("Bot", "Server is unavailable. Please try again later.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
