from django.db import models
from django.utils.translation import gettext_lazy as _


class MuscleGroup:
    CHEST = "C"
    BACK = "B"
    SHOULDERS = "S"
    ARMS = "A"
    LEGS = "L"
    CORE = "Co"

    CHOICES = [
        (CHEST, _("Chest")),
        (BACK, _("Back")),
        (SHOULDERS, _("Shoulders")),
        (ARMS, _("Arms")),
        (LEGS, _("Legs")),
        (CORE, _("Core")),
    ]


class DefinedExercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(max_length=2, choices=MuscleGroup.CHOICES)


class Routine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    FULL_BODY = "FB"
    UPPER_BODY = "UB"
    LOWER_BODY = "LB"
    PUSH = "Ph"
    PULL = "Pl"
    CARDIO = "Ca"
    REST_DAY = "Re"

    CHOICES = [
        (FULL_BODY, _("Full Body")),
        (UPPER_BODY, _("Upper Body")),
        (LOWER_BODY, _("Lower Body")),
        (PUSH, _("Push")),
        (PULL, _("Pull")),
        (CARDIO, _("Cardio")),
        (REST_DAY, _("Rest Day")),
    ] + MuscleGroup.CHOICES

    type = models.CharField(max_length=2, choices=CHOICES)
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.PROTECT)


class ExerciseSet(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    reps = models.IntegerField()
    weight = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    defined_exercise = models.ForeignKey(
        DefinedExercise, on_delete=models.CASCADE
    )
