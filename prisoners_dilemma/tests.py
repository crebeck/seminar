from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (views.Instructions)

        if self.player.id_in_group == 1:
            yield (views.Choice, {"choice": True})
            assert self.player.years == 3
        else:
             yield (views.Choice, {"choice": False})
             assert self.player.years == 0

