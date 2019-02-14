from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def vars_for_template(self):
        if self.player.cp_error:
            return {'message': 'Please, re-read the instructions!'}


class Q(Page):
    form_model = 'player'
    form_fields = ['q1']

    def before_next_page(self):
        p = self.player
        if self.player.q1 != Constants.correct_answer:
            p.q1 = None
            p.cp_error = True
            self._is_frozen = False
            self._index_in_pages -= 2
            self.participant._index_in_pages -= 2
        else:
            p.cp_error = False


class Results(Page):
    pass


page_sequence = [
    Instructions,
    Q,
    Results
]
