from src.questionmanager import Question

class CLI:
    def __init__(self):
        self.qs = Question()

    def start(self):
        pass

    def get_question(self, q):
        return exec(f"print(self.qs.{q}.question)")

    def get_answer(self, q):
        return exec(f"print(self.qs.{q}.answer)")

