
class question4:
    if __name__ == "__main__":

        t = "She's broken because she believed."
        print(t[1:5],t[8:10],
              t[13:20],t[22:24],
              t[27:29]+t[31:33])
    question = """
    Hangisi doğru çıktıyı gösteriyor?
        A) She's ok becuase she lied.
        B) He's ok because she lied.
        C) he's ok because he lied.
        D) She's broke because he lied.
    """

    answer = """
    Çıktı:
    he's ok because he lied.
    Cevap: C) he's ok beacuse he lied.
    """

    def __init__(self):
        self.question = question
        self.answer = answer

    def answer_obj(self):
        t = "She's broken because she believed."
        ans = (t[1:5],t[8:10],
              t[13:20],t[22:24],
              t[27:29]+t[31:33])
        return " ".join(ans)
