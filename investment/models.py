from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Christoph'

doc = """
An investment task.
"""


class Constants(BaseConstants):
    name_in_url = 'investment'
    players_per_group = None
    num_rounds = 1
    endowment_high_stakes = c(1000)
    endowment_low_stakes = c(100)
    win_probability = 0.5
    win_multiplier = 2



class Subsession(BaseSubsession):
    def before_session_starts(self):
        for player in self.get_players():
            #player.treatment = random.choice(['low_stakes', 'high_stakes'])
            if 'treatment' in self.session.config:
                player.treatment = self.session.config['treatment']
            else:
                player.treatment = random.choice(['low_stakes', 'high_stakes'])
            # player.endowment = Constants.endowment_high_stakes if random.uniform(0, 1) > Constants.win_probability \
            #     else Constants.endowment_low_stakes


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.CharField()
    endowment = models.CurrencyField()

    def endowment_assignment(self):
       self.endowment = Constants.endowment_high_stakes if self.treatment == 'high_stakes' else Constants.endowment_low_stakes


    investment_decision = models.CurrencyField(
        min = 0,
        # max = 100 if endowment == Constants.endowment_low_stakes else 1000,
        initial = 0,
        widget = widgets.SliderInput(),
        doc = "players investment decision",
        verbose_name = "Choose how much of your endowment you want to invest (in Euro)."
    )


    did_player_win = models.BooleanField()

    def calculate_payoff(self):
        if random.uniform(0,1) > Constants.win_probability:
            self.did_player_win = True
            self.payoff = (self.endowment - self.investment_decision) + self.investment_decision*Constants.win_multiplier
        else:
            self.did_player_win = False
            self.payoff = self.endowment - self.investment_decision
