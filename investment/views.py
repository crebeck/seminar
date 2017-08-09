from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.player.calculate_payoff()

class InvestmentDecision(Page):
    form_model = models.Player
    form_fields = ['investment_decision']

class Results(Page):
    def vars_for_template(self):
        return {"investment_success": "successful" if self.player.did_player_win == True else "a failure"}


page_sequence = [
    Instructions,
    InvestmentDecision,
    ResultsWaitPage,
    Results
]
