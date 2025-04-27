from src.commandline import CLI

class Run:
    def __init__(self):
        self.cli = CLI()

    def run(self):
        self.cli.start()

    def answer(self):
        self.cli.get_question("q1")
        self.cli.get_answer("q1")
