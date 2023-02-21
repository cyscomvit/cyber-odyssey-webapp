import json
from random import choice as randchoice
from random import shuffle as randshuffle


def answerify(given_answer: str) -> str:
    return given_answer.strip().replace(" ", "").casefold()


def get_questions() -> list:
    with open("./questions.json", "r") as f:
        question_list = json.load(f)
    return question_list


class Question:
    def __init__(self, question_num_in_list: int):
        question = get_questions()[int(question_num_in_list) - 1]
        self.type = question["type"]
        self.question_text = ""
        self.image_url = ""
        if self.type == "image":
            self.image_url = question["text"]
        elif self.type == "text":
            self.question_text = question["text"]
        self.answer = answerify(question["answer"])
        self.difficulty = question["difficulty"]

    def check_answer(self, given_answer: str) -> bool:
        if answerify(given_answer) == self.answer:
            return True
        return False


def get_question_object(question_number: int) -> Question:
    return Question(question_number)


def get_answer_for_a_question(question_number: int | str = 1) -> str:
    q = Question(question_number)
    return q.answer


def get_specific_difficulty_questions(question_dict: dict, difficuty: str) -> list[int]:
    to_return = [
        i
        for i in range(len(question_dict))
        if question_dict[i]["difficulty"].casefold() == difficuty.casefold()
    ]
    return to_return if to_return else []


def get_personal_current_question_number(regno: str):
    from csv_functions import get_team_details
    from firebase_functions import get_team_details

    current_question = get_team_details(regno, "current_question")
    return int(current_question)


def str_sequence_to_int_list(sequence: str) -> list[int]:
    to_return = sequence.strip("[").strip("]").split(",")
    for i in range(len(to_return)):
        to_return[i] = int(to_return[i].strip().strip("'"))
    return to_return


def generate_sequence_for_a_team() -> list[int]:
    """Generates a sequence of questions for each team."""
    question_dict = get_questions()
    easy_questions = get_specific_difficulty_questions(question_dict, "easy")
    medium_questions = get_specific_difficulty_questions(question_dict, "medium")
    hard_questions = get_specific_difficulty_questions(question_dict, "hard")
    # print(easy_questions, medium_questions, hard_questions)
    sequence = []
    if easy_questions:
        randshuffle(easy_questions)
        sequence += easy_questions
    if medium_questions:
        randshuffle(medium_questions)
        sequence += medium_questions
    if hard_questions:
        randshuffle(hard_questions)
        sequence += hard_questions
    return sequence


def get_nth_question_for_a_player(n: int, sequence: str):
    return
    player_sequence = str_sequence_to_int_list(sequence)
