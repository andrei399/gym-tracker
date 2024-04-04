from rest_framework import serializers
from . import models


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "description",
            "type",
            "duration",
            "created_at",
        )
        model = models.Routine


class ExerciseSetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "set_collection", "reps", "weight", "created_at")
        model = models.ExerciseSet


class DefinedExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "description", "muscle_group")
        model = models.DefinedExercise
