from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def before_next_page(self):
        self.player.role_assignment()



class Chat(Page):
    form_model = models.Player


page_sequence = [
    Instructions,
    Chat,
]
