from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class CollectParticipants(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        pass

class Demographics(Page):
    form_model = models.Player
    form_fields = ['age', 'field_of_study', 'likes_experiment', 'weight', 'height', 'female']

class Bmi(Page):
    def vars_for_template(self):
        self.player.calculate_bmi()

        return{
            "bmi": self.player.bmi
        }


page_sequence = [
    Instructions,
    CollectParticipants,
    Demographics,
    Bmi
]
