from django.core.management.base import BaseCommand
from workout import models


class Command(BaseCommand):
    def handle(self, *a, **kw):  # noqa
        bench_press = models.DefinedExercise.objects.create(
            name="Bench Press",
            description="Lay down on bench and push barbell up",
            muscle_group=models.MuscleGroup.CHEST,
        )
