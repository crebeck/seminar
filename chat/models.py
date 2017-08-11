from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christoph'

doc = """
Simple chat implementation
"""


class Constants(BaseConstants):
    name_in_url = 'chat'
    players_per_group = 3
    num_rounds = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    role = models.CharField()

    def role_assignment(self):
        if self.id_in_group == 1:
            self.role = 'Chat Kroeger'
        elif self.id_in_group == 2:
            self.role = 'Text Bundy'
        else:
            self.role = 'Write or Wrong'