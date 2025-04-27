
class question1:
    if __name__=="__main__":

        _="-"
        print(f'{_*2:_^4}')

    def __init__(self):
        self.question = """
    Hangisi doğru çıktıyı gösteriyor?
        A) --__
        B) __--
        C) _--_
        D) Name Error
        E) _-_-
        F) Syntax Error
    """
        self.answer = """
    Çıktı:
    _--_
    Cevap: C)
    """

    def run_answer(self):
        _="-"
        return f'{_*2:_^4}'
