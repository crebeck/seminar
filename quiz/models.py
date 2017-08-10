from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv


author = 'Christoph'

doc = """
This is s simple quiz!
"""


class Constants(BaseConstants):
    name_in_url = 'quiz'
    players_per_group = None

    with open('quiz/quiz.csv') as quiz_questions:
        questions = list(csv.DictReader(quiz_questions))

    num_rounds = len(questions)

class Subsession(BaseSubsession):
    def before_session_starts(self):
        # self.session.vars['questions'] = Constants.questions if self.round_number == 1 else None

        if self.round_number == 1:
            self.session.vars['questions'] = Constants.questions

        for player in self.get_players():
            question_data = player.current_question()
            player.question_id = question_data['id']
            player.question = question_data['question']
            player.solution = question_data['solution']



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
        self.is_correct = True if self.submitted_answer == self.solution else None