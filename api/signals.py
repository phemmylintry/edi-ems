from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TeamEmployee, Employee, WorkArrangement


@receiver(post_save, sender=Employee)
def create_team_employee(sender, instance, created, **kwargs):
    if created:
        TeamEmployee.objects.create(employee=instance, team=instance.team)


@receiver(post_save, sender=Employee)
def create_work_arrangement(sender, instance, created, **kwargs):
    if created:
        WorkArrangement.objects.create(employee=instance)
