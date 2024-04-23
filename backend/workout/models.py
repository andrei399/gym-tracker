from django.db import models
from django.utils.translation import gettext_lazy as _


class MuscleGroup(models.TextChoices):
    CHEST = "C", _("Chest")
    BACK = "B", _("Back")
    SHOULDERS = "S", _("Shoulders")
    ARMS = "A", _("Arms")
    LEGS = "L", _("Legs")
    CORE = "Co", _("Core")


class DefinedExercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(max_length=2, choices=MuscleGroup.choices)


class Routine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class RoutineChoices(models.TextChoices):
        FULL_BODY = "FB", _("Full Body")
        UPPER_BODY = "UB", _("Upper Body")
        LOWER_BODY = "LB", _("Lower Body")
        PUSH = "Ph", _("Push")
        PULL = "Pl", _("Pull")
        CARDIO = "Ca", _("Cardio")
        REST_DAY = "Re", _("Rest Day")

    type = models.CharField(
        max_length=2, choices=RoutineChoices.choices + MuscleGroup.choices
    )
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
