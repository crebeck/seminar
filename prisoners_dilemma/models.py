from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christoph'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'prisoners_dilemma'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def calculate_payoffs(self):
        players = self.get_players()
        if players[0].choice == Player[1].choice & Player[0].choice == True: # both cooperate
            players[0].years = 1
            players[1].years = 1
        elif players[0].choice == Player[1].choice & Player[0].choice == False: # both defect
            players[0].years = 2
            players[1].years = 2
        elif Player[0].years != Player[1].choice & Player[0].choice == True:  # only P1 cooperates
            players[0].years = 3
            players[1].years = 0
        else: # only P2 cooperates
            players[0],years = 0
            players[1].years = 3

class Player(BasePlayer):
    choice = models.BooleanField(
        choices = [(True, "Cooperate"), (False, "Defect")],
        widget = widgets.RadioSelect(),
        doc = "choice to cooperate or to defect",
        verbose_name = "Please choose whether to cooperate or to defect."
    )

    years = models.PositiveIntegerField()


