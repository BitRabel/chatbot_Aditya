class chatbots:
    def chatbots_response(self, user_input):
        user_input = user_input.lower()
        greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
        farewells = ["bye", "goodbye", "see you", "farewell"]
        thanks = ["thank you", "thanks", "appreciate it"]
        apologies = ["sorry", "apologize", "my apologies"]
        
        if any(greeting in user_input for greeting in greetings):
            return "Hello! How can I assist you today?"
        elif any(farewell in user_input for farewell in farewells):
            return "Goodbye! Have a great day!"
        elif any(thank in user_input for thank in thanks):
            return "You're welcome! If you have more questions, feel free to ask."
        elif any(apology in user_input for apology in apologies):
            return "No worries! How can I assist you?"
        elif "help" in user_input:
            return "Sure! What do you need help with?"
        elif "how are you" in user_input:
            return "I'm a chatbots, so I don't have feelings, but I'm here to help you!"
        elif "what is your name" in user_input:
            return "I'm your virtual assistant. How can I help you today?"
        elif "what can you do" in user_input:
            return "I can assist with various queries, provide information, and help you with basic tasks. What do you need help with?"
        else:
            return "I didn't Get it. Could you please provide more details or ask a specific question?"
