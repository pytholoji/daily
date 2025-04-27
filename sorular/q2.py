
class question2:
    if __name__ == "__main__":

        a = 10
        print( sum( a for a in range(3) ) )

    question = """
    Hangisi doğru çıktıyı gösteriyor?
        A) 30
        B) 3
        C) Name Error
        D) Syntax Error
        E) 6
        F) 40
    """

    answer = """
    Çıktı:
    3
    Cevap: B)
    """

    def __init__(self):
        self.question = question
        self.answer = answer

    def answer_obj(self):
        try:
            a = 10
            ans = sum( a for a in range(3) )
            return ans
        except Error as e:
            return e
