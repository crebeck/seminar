from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

from otree.api import SubmissionMustFail


class PlayerBot(Bot):

    def play_round(self):
        yield (views.Instructions)

        for number in [-1, -10, 200, 300]:
            yield SubmissionMustFail(views.BetOnCoin, {'wager': number})

        yield (views.BetOnCoin, {'wager': 50})

        yield (views.Results)
