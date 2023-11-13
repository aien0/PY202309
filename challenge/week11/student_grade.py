class Student:
    name = ""
    korean = 0
    math = 0
    english = 0

    def set_scores(self, korean, math, english):
        self.korean = korean
        self.math = math
        self.english = english

    def get_average(self):
        # 국어, 수학, 영어 점수의 평균을 계산하여 반환
        return (self.korean + self.math + self.english) / 3

# TODO 1: 학생 정보를 딕셔너리에 저장
def loadData(file_path):
    lines = open(file_path, "r", encoding="utf8").readlines()

    # 학생 정보를 저장할 딕셔너리
    student_data = {}

    for line in lines[1:]:  # 첫 줄 무시
        data = line.strip().split(',')
        name = data[0]
        korean, math, english = map(float, data[1:])
        
        # Student 클래스 인스턴스 생성
        student = Student()
        student.name = name
        student.set_scores(korean, math, english)

        # 딕셔너리에 학생 정보 저장
        student_data[name] = student

    # 딕셔너리 반환
    return student_data

# 메인 부분
if __name__ == "__main__":
    # loadData 함수 호출
    student_data = loadData("C:/Users/82102/Desktop/PY202309/challenge/week11/students.csv")

    # 평균 점수 출력 및 파일 저장
    with open("C:/Users/82102/Desktop/PY202309/challenge/week11/average.txt", "w", encoding="utf8") as file:
        for name, student in student_data.items():
            # 출력
            print("%s의 평균 점수는 %s입니다." % (name, student.get_average()))
            # 파일에 저장
            file.write("%s의 평균 점수는 %s입니다.\n" % (name, student.get_average()))
