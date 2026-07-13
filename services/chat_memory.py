class ChatMemory:
    def __init__(self):
        self.messages = []

    def add_user_message(self, message):
        self.messages.append({
            "role": "user",
            "content": message
        })

    def add_assistant_message(self, message):
        self.messages.append({
            "role": "assistant",
            "content": message
        })

    def get_history(self):
        history = ""

        for msg in self.messages:
            history += f"{msg['role'].capitalize()}: {msg['content']}\n"

        return history

    def clear(self):
        self.messages = []