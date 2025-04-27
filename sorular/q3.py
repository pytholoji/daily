
class question3:
    if __name__ == "__main__":

        palindrom = "ey edip adanada pide ye"
    question = """
    Bu cümleyi tersten nasıl yazdırabiliriz?
        A) print(palindrom[-1::])
        B) print(palindrom[:-1:])
        C) print(reversed(palindrom))
        D) print(palindrom[::-1])
    """

    answer = """
    Cevap: D) print(palindrom[::-1])
    Çıktı:
    ey edip adanada pide ye
    """

    def __init__(self):
        self.question = question
        self.answer = answer

    def answer_obj(self):
        palindrom = "ey edip adanada pide ye"
        return palindrom
