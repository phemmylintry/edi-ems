from django.db import models
from uuid import uuid4


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Team(DateMixin):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Employee(DateMixin):
    name = models.CharField(max_length=200)
    employee_id = models.CharField(
        max_length=200, unique=True, blank=True, null=True, default=None
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="employees",
        blank=True,
        null=True,
        default=None,
    )
    hourly_rate = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=True, null=True
    )

    def __str__(self):
        return self.name

    # override save method to set employee_id
    def save(self, *args, **kwargs):
        if not self.employee_id:
            self.employee_id = self.generate_employee_id()
        super(Employee, self).save(*args, **kwargs)

    def generate_employee_id(self):
        """
        Generate a unique employee_id
        """
        employee_id = uuid4().hex[:5].upper()
        return f"EMP-{employee_id}"


class TeamLeader(DateMixin):
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="team_leader_employee"
    )
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE,
        related_name="team_leader_team",
        blank=True,
        null=True,
        default=None,
    )

    def __str__(self):
        return self.employee.name


class TeamEmployee(DateMixin):
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="team_employee_employee"
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="team_employee_team",
        blank=True,
        null=True,
        default=None,
    )

    def __str__(self):
        return self.employee.name


class WorkArrangement(DateMixin):
    FULL_TIME = 1
    PART_TIME = 2

    WORK_ARRANGEMENT_CHOICES = (
        (FULL_TIME, "Full Time"),
        (PART_TIME, "Part Time"),
    )

    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="work_arrangements"
    )
    work_arrangement = models.IntegerField(
        choices=WORK_ARRANGEMENT_CHOICES, default=FULL_TIME
    )
    hours_per_week = models.IntegerField(default=40)

    def __str__(self):
        return self.employee.name

    # check if hours_per_week is less than 40, if yes, set work_arrangement to PART_TIME
    def save(self, *args, **kwargs):
        if self.hours_per_week < 40:
            self.work_arrangement = self.PART_TIME
        super(WorkArrangement, self).save(*args, **kwargs)
