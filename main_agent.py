
from agents.planner import Planner
from agents.worker import Worker
from agents.evaluator import Evaluator
from memory.session_memory import SessionMemory
from core.security import SecurityManager

class MainAgent:

    def __init__(self):
        self.planner = Planner()
        self.worker = Worker()
        self.evaluator = Evaluator()
        self.memory = SessionMemory()
        self.security = SecurityManager()

    def handle_message(self, user_input):

        if not self.security.validate(user_input):
            return {
                "response": "Security Warning: Potential prompt injection detected. Request blocked."
            }

        user_id = "default_user"

        self.memory.save_user_idea(
            user_id,
            user_input
        )

        plan = self.planner.plan(user_input)

        results = self.worker.execute(plan)

        evaluation = self.evaluator.evaluate(results)

        return evaluation


def run_agent(user_input: str):
    agent = MainAgent()
    result = agent.handle_message(user_input)
    return result["response"]
