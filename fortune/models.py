from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Christoph'

doc = """
Multiple player game - betting on a coin toss
"""


class Constants(BaseConstants):
    name_in_url = 'fortune'
    players_per_group = None
    num_rounds = 1
    endowment = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    wager = models.PositiveIntegerField(
        default = 0,
        max = Constants.endowment,
        widget = widgets.SliderInput(attrs={'step': '1'}),
        doc = "money bet by the participant",
        verbose_name = "How much of your endowment do you want to bet?"
    )

    coin_toss = models.FloatField(
        default = round(random.uniform(0,1), 2)
    )

    win_message  = models.CharField()

    payoff = models.PositiveIntegerField()

    final_payoff = models.CurrencyField()

    coin_result = models.PositiveIntegerField()

    choice = models.PositiveIntegerField(
        choices = [[0, "heads"], [1, "tails"]],
        widget = widgets.RadioSelect,
        doc = "choice heads or tails"
    )

    def coin_side(self):
        if self.coin_toss > 0.5:
            self.coin_result = 0  # heads
        else:
            self.coin_result = 1  # tails

    def win_against_coin(self):
        if self.choice == self.coin_result:
            self.win_message = "Congratulations, you won!"
            self.payoff = self.wager * 2
        else:
            self.win_message = "Unfortunately, you lost. Your money now belongs to the mighty oTree-Overlord!"
            self.payoff = 0

    def calculate_payoff(self):
        self.final_payoff = Constants.endowment - self.wager + self.payoff
