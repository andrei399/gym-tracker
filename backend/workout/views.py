from rest_framework import viewsets
from . import models, serializers


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = models.Routine.objects.all()
    serializer_class = serializers.RoutineSerializer


class ExerciseSetViewSet(viewsets.ModelViewSet):
    queryset = models.ExerciseSet.objects.all()
    serializer_class = serializers.ExerciseSetSerializer


class DefinedExerciseViewSet(viewsets.ModelViewSet):
    queryset = models.DefinedExercise.objects.all()
    serializer_class = serializers.DefinedExerciseSerializer
