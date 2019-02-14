from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Instructions)
        for i in  range(10):
            yield (pages.Q,{'q1':random.randint(2,10)})
            yield (pages.Instructions)
        yield (pages.Q, {'q1': 1})
        yield (pages.Results)
