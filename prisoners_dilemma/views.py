from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.calculate_payoffs()


class Choice(Page):
    form_model = models.Player
    form_fields = ['choice']



class Results(Page):
    def vars_for_template(self):
        self.player.partner_choice()

        return {'results_choice': "Cooperate" if self.player.choice==True else "Defect",
                'results_your_partners_choice': "Cooperate" if self.player.your_partners_choice==True else "Defect"
                }


page_sequence = [
    Instructions,
    Choice,
    ResultsWaitPage,
    Results
]
