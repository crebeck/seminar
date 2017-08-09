from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Christoph'

doc = """
Ultimatum game
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum_game'
    players_per_group = 2
    num_rounds = 3
    endowment = c(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def role_assignment(self):
        random_role = random.randint(0, 1)

        if random_role == 0:
            responder = self.get_player_by_id(1)
            proposer = self.get_player_by_id(2)
        else:
            responder = self.get_player_by_id(2)
            proposer = self.get_player_by_id(1)

    def calculate_payoffs(self):

        responder = self.get_player_by_id(1)
        proposer = self.get_player_by_id(2)

        if self.accept == True:
            responder.payoff = self.offer
            proposer.payoff = Constants.endowment - self.offer
        else:
            responder.payoff = 0
            proposer.payoff = 0


    offer = models.CurrencyField(
        initial = 0,
        min = 0,
        max = Constants.endowment,
        doc = "decision of the proposer",
        verbose_name = "Please, decide how much money you want to send to the responder."
    )

    accept = models.BooleanField(
        choices = [(True, 'Accept'), (False, 'Decline')],
        widget = widgets.RadioSelect(),
        doc = "does the responder accept?",
        verbose_name = "Do you want to accept the proposers offer?"
    )




class Player(BasePlayer):
    payoff = models.CurrencyField()

