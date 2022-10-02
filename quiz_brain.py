class QuizBrain:

    def __init__(self, q_list):
        self.q_num = 0
        self.score = 0
        self.q_list = q_list

    # TODO-3 checking if we're the end of the quiz
    def still_has_question(self):
        return self.q_num < len(self.q_list)

    # TODO-1 asking the questions
    def next_question(self):
        question = self.q_list[self.q_num]
        self.q_num += 1
        user_answer = input(f"Q.{self.q_num}: {question.q_text}. (True/False)?: ")
        self.check_answer(user_answer, question.q_answer)

    # TODO-2 checking if the answer was correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.q_num}.")
