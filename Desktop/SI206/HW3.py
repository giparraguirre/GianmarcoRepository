# Your name: Gianmarco Iparraguirre
# Your student id: 6361 1583
# Your email: gianmarc@umich.edu 
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.
# e.g.: Asked Chatgpt hints for debugging and suggesting the general structure of the code

import random
from collections import Counter

# Create a Digital Book of Answers
class DigitalBookofAnswers:
    # Constructor (__init__) method
    # ARGUMENTS:
    # self: the current object
    # answers: a list of potential answers
    # RETURNS: None
    def __init__(self, answers) :
        self.book_answer_list = answers

        self.questions_asked_list = []

        self.answered_list = []

    # Create the __str__ method
    # ARGUMENTS:
    # self: the current object
    # RETURNS: a string
    def __str__(self) :
        if not self.book_answer_list :
            return ""
        return " - ".join(self.book_answer_list)

    # Creates the check_get_answer method
    # ARGUMENTS:
    # self: the current object
    # question: the question the user wants to ask the digital book of answers
    # RETURNS: a string
    def check_get_answer(self, question):
    # Check if the question has already been asked
        if question in self.questions_asked_list:
            question_index = self.questions_asked_list.index(question)
            answer_index = self.answered_list[question_index]  # Access the correct answer index
            answer = self.book_answer_list[answer_index]
            return f"I’ve already answered this question. The answer is: {answer}"
        
        # If the question is new, pick a random answer
        else:
            random_index = random.randint(0, len(self.book_answer_list) - 1)
            answer = self.book_answer_list[random_index]
            self.questions_asked_list.append(question)
            self.answered_list.append(random_index)  # Ensure to add the corresponding answer index
            return answer


    # Creates the open_book method
    # ARGUMENTS:
    # self: the current object
    # RETURNS: None
    def open_book(self) :
        while True :
            turn_number = len(self.questions_asked_list) + 1

            question = input(f"Turn {turn_number} - Please enter your question: ")

            if question == "Done" :
                print("Goodbye! See you soon.")
                break

            answer = self.check_get_answer(question)
            print(answer)


    # Create the answer_log method
    # ARGUMENTS:
    # self: the current object
    # RETURNS: a list
    def answer_log(self) :
        if not self.answered_list :
            print("Empty")
            return []
        
        count = Counter(self.answered_list)

        frequency = []
        for index, freq in count.items() : 
            answer = self.book_answer_list[index].lower()
            frequency.append(f"{freq}-{answer}")

        frequency.sort(key=lambda x: int(x.split('-')[0]), reverse = True)

        return frequency

def test():
    answers_list = ['Believe in Yourself', 'Stay Open to the Future', 'Enjoy It']
    book = DigitalBookofAnswers(answers_list)

    print("Test __init__:")
    print(f"Answer History List: Expected: {[]}, Actual: {book.answered_list}")
    print(f"Question History List: Expected: {[]}, Actual: {book.questions_asked_list}")
    print(" ")

    print("Test __str__:")
    expected = "Belive in Yourself - Stay Open to the Future - Enjoy It"
    print(f"Expected: {expected}, Actual: {str(book)}")
    print(" ")

    empty_book = DigitalBookofAnswers([])
    print("Test __str__: when it's an empty book without possible answers")
    expected = ""
    print(f"Expected: {expected}, Actual: {str(empty_book)}")
    print(" ")

    print("Testing return value of check_get_answer:")
    res = book.check_get_answer('test question')
    print(f"Expected: {str}, Actual: {type(res)}")
    print(" ")

    print("Testing check_get_answer")
    book.book_answer_list = ['Go For It']
    res = book.check_get_answer('test question 2')
    print(f"Expected: {'Go For It'}, Actual: {res}")
    print(" ")

    # print("Testing that check_get_answer adds answer index to answered_list:")
    # book.book_answer_list = ['Go For It']
    # book.answered_list = []
    # book.check_get_answer('test question 2')
    # expected = [0]
    # res = book.answered_list
    # print(f"Expected: {expected}, Actual: {res}")
    # print(" ")

    # Now test that check_get_answer adds answer index to answered_list
    print("Testing that check_get_answer adds answer index to answered_list:")
    book.check_get_answer('test question 3')  # This should add an entry to answered_list
    expected = [0, 1, 2]  # Assuming "test question 3" gives the third answer in the list
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing that check_get_answer does not add 'I've already answered this question' part to answered_list:")
    book.book_answer_list = ['Believe In Yourself']
    book.answered_list = [0]
    book.questions_asked_list = ['test question 3']
    book.check_get_answer('test question 3')
    expected = [0]
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing return value of answer_log")
    book.book_answer_list = ['Follow Your Inner Voice', 'Stay Positive', 'Go For It']
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log())
    print(f"Expected: {list}, Actual: {res}")
    print(" ")

    print("Testing return value answer_log elements")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log()[0])
    print(f"Expected: {str}, Actual: {res}")
    print(" ")

    print("Testing answer_log")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = book.answer_log()
    expected = ['3 - follow your inner voice', '2 - stay positive', '1 - go for it']
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing empty answer_log")
    book.answered_list = []
    res = book.answer_log()
    expected = []
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")


# Extra Credit
def my_test():
    # Put your test code here
    pass


def main() :
    book_answer_list = [
        "Follow Your Inner Voice",
        "Stay Positive",
        "Go For It",
        "Believe in Yourself",
        "Stay Open to the Future",
        "Enjoy It"
    ]

    # Create the DigitalBookofAnswers object
    book = DigitalBookofAnswers(book_answer_list)

    # Initiate the book using open_book() method for interactive session
    book.open_book()

    # Show the output of the answer_log() method after the session ends
    log = book.answer_log()
    print(log)


# Only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    # main()
    test()
    # my_test()  # TODO: Uncomment if you do the extra credit
