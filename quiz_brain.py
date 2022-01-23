class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        total_questions = len(self.question_list)
        return self.question_number < total_questions
        

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {question.text} (True/False)?: ")
        print(user_answer)