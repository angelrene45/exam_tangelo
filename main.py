from modules import TangeloExam

if __name__ == '__main__':
    exam = TangeloExam()
    status_exam = exam.start()
    print(f"status_exam: {status_exam}")