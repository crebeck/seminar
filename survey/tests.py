from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from otree.api import SubmissionMustFail
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (views.Instructions)

        for test_number in [-1, -2, 4, 0.5]:
            yield SubmissionMustFail(views.Demographics, {
                'age': 25,
                'field_of_study': "",
                'female': 0,
                'height': test_number,
                'weight': 100,
                'likes_experiment': "Yes, of course!"
                })


# class PlayerBot(Bot):
#
#     def play_round(self):
#         yield SubmissionMustFail(views.Demographics, {
#             'age': 25,
#             'field_of_study': "",
#             'female': 3,
#             'height': 1.5,
#             'weight': 100,
#             'likes_experiment': "Yes, of course!"
#         })
#
#         assert self.player.bmi == 100
#         assert self.player.bmi_eval == "You are overweight, you fat fuck!"
#
#         yield (views.Bmi)
