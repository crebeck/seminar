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

        player1 = self.get_player_by_role('Player 1')
        player2 = self.get_player_by_role('Player 2')

        if player1.choice == player2.choice and player1.choice == True: # both cooperate
            player1.years = 1
            player2.years = 1
        elif player1.choice == player2.choice and player1.choice == False: # both defect
            player1.years = 2
            player2.years = 2
        elif player1.years != player2.choice and player1.choice == True:  # only P1 cooperates
            player1.years = 3
            player2.years = 0
        else: # only P2 cooperates
            player1.years = 0
            player2.years = 3

class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'Player 1'
        else:
            return 'Player 2'

    choice = models.BooleanField(
        choices = [(True, "Cooperate"), (False, "Defect")],
        widget = widgets.RadioSelect(),
        doc = "choice to cooperate or to defect",
        verbose_name = "Please choose whether to cooperate or to defect."
    )

    years = models.PositiveIntegerField()

    your_partners_choice = models.BooleanField()

    def partner_choice(self):
        self.your_partners_choice = self.get_others_in_group()[0].choice