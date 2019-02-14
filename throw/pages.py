from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def vars_for_template(self):
        if self.player.cp_error:
            return {'message': 'Please, re-read the instructions!'}


class Q(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2']

    def before_next_page(self):
        p = self.player
        p.cp_error = False
        for k, v in Constants.correct_answers.items():
            if getattr(p, k) != v:
                p.cp_error = True
                break
        if p.cp_error:
            for f in self.form_fields:
                setattr(p, f, None)
            self._is_frozen = False
            self._index_in_pages -= 2
            self.participant._index_in_pages -= 2


class Results(Page):
    pass


page_sequence = [
    Instructions,
    Q,
    Results
]
