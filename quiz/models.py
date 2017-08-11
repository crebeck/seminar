from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv
import pprint


author = 'Christoph'

doc = """
This is s simple quiz!
"""


class Constants(BaseConstants):
    name_in_url = 'quiz'
    players_per_group = None

    with open('quiz/quiz.csv') as quiz_questions:
        questions = list(csv.DictReader(quiz_questions))

    # pprint.pprint(questions)

    num_rounds = len(questions)

class Subsession(BaseSubsession):
    def before_session_starts(self):
        #self.session.vars['questions'] = Constants.questions if self.round_number == 1 else None

        if self.round_number == 1:
            # import random
            # randomised_questions = random.sample(Constants.questions, 3)

            self.session.vars['questions'] = Constants.questions



        for p in self.get_players():
            question_data = p.current_question()
            p.question_id = question_data['id']
            p.question = question_data['question']
            p.solution = question_data['solution']



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_id = models.PositiveIntegerField()
    question = models.CharField()
    solution = models.CharField()
    submitted_answer = models.CharField(
        widget = widgets.RadioSelect()
    )
    is_correct = models.BooleanField()

    def current_question(self):
        return self.session.vars['questions'][self.round_number - 1]

    def check_if_correct(self):
        # self.is_correct = self.submitted_answer == self.solution
        self.is_correct = True if self.submitted_answer == self.solution else False # also works