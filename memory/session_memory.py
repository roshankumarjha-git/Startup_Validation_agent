
import json
import os

class SessionMemory:

    def __init__(self):

        self.memory_file = "/memory/user_memory.json"

        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w") as f:
                json.dump({}, f)

    def save_user_idea(self, user_id, idea):

        with open(self.memory_file, "r") as f:
            data = json.load(f)

        if user_id not in data:
            data[user_id] = []

        data[user_id].append(idea)

        with open(self.memory_file, "w") as f:
            json.dump(data, f, indent=2)

    def get_user_history(self, user_id):

        with open(self.memory_file, "r") as f:
            data = json.load(f)

        return data.get(user_id, [])
