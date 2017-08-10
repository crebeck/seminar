from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (views.Instructions)

        if self.player.endowment == 100:
            yield (views.InvestmentDecision, {'investment_decision': 50})
        else:
            yield (views.InvestmentDecision, {'investment_decision': 500})
        yield (views.Results)

        if self.player.endowment == 100 and self.player.did_player_win == True:
            assert self.player.payoff == 150
        elif self.player.endowment == 1000 and self.player.did_player_win == True:
            assert self.player.payoff == 1500
        else:
            assert self.player.payoff == 0.5*self.player.endowment
