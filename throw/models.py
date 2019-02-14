from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'throw'
    players_per_group = None
    num_rounds = 1
    correct_answer = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    cp_error = models.BooleanField()  # set to True when a person answers erroneusly at a comprehension page
    q1 = models.IntegerField()  # comprehension question (correct answer  should be 1 - for instance, see constants)
