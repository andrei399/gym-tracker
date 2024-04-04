from django.test import TestCase
from workout import models


class DefinedExerciseTest(TestCase):
    def setUp(self):
        models.DefinedExercise.objects.create(
            name="Bench Press",
            description="Lay down on bench and push barbell up",
            muscle_group=models.MuscleGroup.CHEST,
        )
        models.DefinedExercise.objects.create(
            name="Squat",
            description="Stand with barbell on shoulders and squat down",
            muscle_group=models.MuscleGroup.LEGS,
        )

    def test_bench_press(self):
        bench_press = models.DefinedExercise.objects.get(name="Bench Press")
        self.assertEqual(bench_press.get_muscle_group_display(), "Chest")

    def test_squat(self):
        squat = models.DefinedExercise.objects.get(name="Squat")
        self.assertEqual(squat.get_muscle_group_display(), "Legs")


class RoutineAndExerciseSetTest(TestCase):
    def setUp(self):
        leg_day = models.Routine.objects.create(
            name="Leg Day",
            description="Legs only",
            type=models.MuscleGroup.LEGS,
            duration=60,
        )
        push_day = models.Routine.objects.create(
            name="Push Day",
            description="Push muscles",
            type=models.MuscleGroup.CHEST,
            duration=60,
        )
        bench_press = models.DefinedExercise.objects.create(
            name="Bench Press",
            description="Lay down on bench and push barbell up",
            muscle_group=models.MuscleGroup.CHEST,
        )
        squat = models.DefinedExercise.objects.create(
            name="Squat",
            description="Stand with barbell on shoulders and squat down",
            muscle_group=models.MuscleGroup.LEGS,
        )
        models.ExerciseSet.objects.create(
            reps=10,
            weight=100,
            defined_exercise=bench_press,
            routine=push_day,
        )
        models.ExerciseSet.objects.create(
            reps=10, weight=100, defined_exercise=squat, routine=leg_day
        )

    def test_bench_press_properties(self):
        bench_set = models.ExerciseSet.objects.get(
            defined_exercise__name="Bench Press"
        )
        self.assertEqual(bench_set.reps, 10)
        self.assertEqual(bench_set.weight, 100)
        self.assertEqual(bench_set.defined_exercise.name, "Bench Press")

    def test_squat_properties(self):
        squat_set = models.ExerciseSet.objects.get(
            defined_exercise__name="Squat"
        )
        self.assertEqual(squat_set.reps, 10)
        self.assertEqual(squat_set.weight, 100)
        self.assertEqual(squat_set.defined_exercise.name, "Squat")

    def test_bench_press_update(self):
        bench_set = models.ExerciseSet.objects.get(
            defined_exercise__name="Bench Press"
        )
        bench_set.weight = 120
        bench_set.save()
        updated_bench_set = models.ExerciseSet.objects.get(
            defined_exercise__name="Bench Press"
        )
        self.assertEqual(updated_bench_set.weight, 120)

    def test_squat_update(self):
        squat_set = models.ExerciseSet.objects.get(
            defined_exercise__name="Squat"
        )
        squat_set.reps = 12
        squat_set.save()
        updated_squat_set = models.ExerciseSet.objects.get(
            defined_exercise__name="Squat"
        )
        self.assertEqual(updated_squat_set.reps, 12)

    def test_routine_properties(self):
        leg_day = models.Routine.objects.get(name="Leg Day")
        self.assertEqual(leg_day.type, "L")
        self.assertEqual(leg_day.duration, 60)
        self.assertEqual(leg_day.description, "Legs only")

    def test_routine_update(self):
        leg_day = models.Routine.objects.get(name="Leg Day")
        leg_day.duration = 90
        leg_day.save()
        updated_leg_day = models.Routine.objects.get(name="Leg Day")
        self.assertEqual(updated_leg_day.duration, 90)

    def add_set_to_routine(self):
        push_day = models.Routine.objects.get(name="Push Day")
        bench_press = models.DefinedExercise.objects.get(name="Bench Press")
        models.ExerciseSet.objects.create(
            reps=10, weight=100, defined_exercise=bench_press, routine=push_day
        )
        self.assertEqual(models.ExerciseSet.objects.count(), 3)

    def add_new_exercise_to_routine(self):
        push_day = models.Routine.objects.get(name="Push Day")
        incline_bench_press = models.DefinedExercise.objects.create(
            name="Incline Bench Press",
            description="Lay down on bench and push barbell up at an incline",
            muscle_group=models.MuscleGroup.CHEST,
        )
        models.ExerciseSet.objects.create(
            reps=10,
            weight=90,
            defined_exercise=incline_bench_press,
            routine=push_day,
        )
        self.assertEqual(models.ExerciseSet.objects.count(), 3)
        self.assertEqual(models.DefinedExercise.objects.count(), 3)
