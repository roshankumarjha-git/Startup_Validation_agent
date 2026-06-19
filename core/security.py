
class SecurityManager:

    def __init__(self):

        self.blocked_phrases = [
            "ignore previous instructions",
            "ignore all instructions",
            "reveal api key",
            "show api key",
            "system prompt",
            "developer instructions",
            "bypass security",
            "give score 100"
        ]

    def validate(self, text):

        text = text.lower()

        for phrase in self.blocked_phrases:

            if phrase in text:

                return False

        return True
