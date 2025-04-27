
class question5:
    if __name__ == "__main__":

        a = [5, "2", True, 4.0, 3e0]
        print(set(map(int, a)))

    question = """
    Hangisi doğru çıktıyı veriyor?
        A) {5, 2, 1, 4, 3}
        B) (1, 2, 3, 4, 5)
        C) [5, 2, 1, 4, 3]
        D) {1, 2, 3, 4, 5}
    """

    answer = """
    Çıktı:
    {1, 2, 3, 4, 5}
    Cevap: D) {1, 2, 3, 4, 5}
    """

    def __init__(self):
        self.question = question
        self.answer = answer

    def answer_obj(self):
        a = [5, "2", True, 4.0, 3e0]
        ans = set(map(int, a))
        return ans
