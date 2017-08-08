from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class WaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class BetOnCoin(Page):
    form_model = models.Player
    form_fields = ['wager', 'choice']

    def before_next_page(self):
        self.player.coin_side()
        self.player.win_against_coin()
        self.player.calculate_payoff()

class Results(Page):
    pass


page_sequence = [
    Instructions,
    BetOnCoin,
    WaitPage,
    Results
]
