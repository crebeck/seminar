from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class ProposerDecision(Page):
    form_model = models.Group
    form_fields = ['offer']

    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

    timeout_seconds = 60
    timeout_submissions = {'offer': 0}



class ResponderDecision(Page):
    form_model = models.Group
    form_fields = ['accept']

    def is_displayed(self):
        return self.player.id_in_group == 2

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.calculate_payoffs()


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {'results_accept': "Accept" if self.group.accept == True else "Decline"}

class ResponderWaitPage(WaitPage):

    def is_displayed(self):
        return self.player.id_in_group == 2


page_sequence = [
    Instructions,
    ProposerDecision,
    ResponderWaitPage,
    ResponderDecision,
    ResultsWaitPage,
    Results
]
