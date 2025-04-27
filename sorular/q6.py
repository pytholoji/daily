
class question6:
    if __name__ == "__main__":

        rakamlar = {2, 1, 3, 4}
        sonuc = []
        for rakam in rakamlar:
            if rakam == 1:
                sonuc.append("E")
                continue
            if rakam == 2:
                sonuc.append("N")
            if rakam == 3:
                sonuc.append("A")
                continue
            if rakam == 4:
                sonuc.append("M")
                continue
            sonuc.append("D")
        print("".join(sonuc))

    question = """
    Hangisi doğru çıktıdır?
        A) NEMAD
        B) DEMAN
        C) ENDAM
        D) DANEM
    """

    answer = """
    Çıktı: ENDAM
    Cevap: C) ENDAM
    """

    def __init__(self):
        self.question = question
        self.answer = answer

    def answer_obj(self):
        rakamlar = {2, 1, 3, 4}
        sonuc = []
        for rakam in rakamlar:
            if rakam == 1:
                sonuc.append("E")
                continue
            if rakam == 2:
                sonuc.append("N")
            if rakam == 3:
                sonuc.append("A")
                continue
            if rakam == 4:
                sonuc.append("M")
                continue
            sonuc.append("D")
        return "".join(sonuc)
