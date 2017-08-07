from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christoph'

doc = """
Short demographic survey - our first app.
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.PositiveIntegerField(
        min = 16,
        max = 120,
        verbose_name = "How old are you?",
        doc = "collect age data between 16 and 120",
    )

    field_of_study = models.CharField(
        blank = True, # some subjects might not study
        verbose_name = "What do you study?",
        doc = "collect field of study data, open field",
    )

    likes_experiment = models.CharField(
        choices = ["Yes, of course!", "No, suck it!", "Maybe..."],
        widget = widgets.RadioSelect(),
        verbose_name = "Doy you like the survey?",
        doc = "likes experiment - yes, no, or maybe",
    )

    female = models.PositiveIntegerField(
        choices = [[0, "Male"], [1, "Female"], [2, "Other"]],
        widget = widgets.RadioSelect(),
        verbose_name = "What is your gender?",
        doc = "gender of participant",
    )

    height = models.FloatField(
        min = 1.0,
        max = 2.5,
        verbose_name = "What is your height in meters? Use floating numbers for your answer.",#
        doc = "height of participant in meters",
    )

    weight = models.FloatField(
        min = 30,
        max = 300,
        verbose_name = "How heavy are you in Kg? You can use floating numbers for your answer.",
        doc = "weight of participant in kg",
    )

    bmi = models.FloatField()

    def calculate_bmi(self):
        self.bmi = self.weight / self.height ** 2
