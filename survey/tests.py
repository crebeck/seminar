from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from otree.api import SubmissionMustFail
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (views.Demographics, {'field_of_study' = })
        yield SubmissionMustFail(views.Demographics, {'age': -5 })
        yield (views.Bmi)
