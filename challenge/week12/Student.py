class Student:
    def __init__(self, name, korean, math, english):
        self.name = name
        self.scores = {'korean': korean, 'math': math, 'english': english}

    def get_average(self):
        # 국어, 수학, 영어 점수의 평균을 계산하여 반환
        return sum(self.scores.values()) / len(self.scores)