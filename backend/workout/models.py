from django.db import models


class Routine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    CHOICES = (
        ("FB", "Full Body"),
        ("UB", "Upper Body"),
        ("LB", "Lower Body"),
        ("Ph", "Push"),
        ("Pl", "Pull"),
        ("L", "Legs"),
        ("C", "Chest"),
        ("B", "Back"),
        ("S", "Shoulders"),
        ("A", "Arms"),
        ("C", "Core"),
        ("Ca", "Cardio"),
        ("Re", "Rest Day"),
    )
    type = models.CharField(max_length=2, choices=CHOICES)

    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class SetCollection(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    number = models.IntegerField()


class ExerciseSet(models.Model):
    set_collection = models.ForeignKey(SetCollection, on_delete=models.CASCADE)
    reps = models.IntegerField()
    weight = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class DefinedExercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(max_length=100)
