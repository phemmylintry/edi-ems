from django.db import models


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
    employee_id = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="employees")
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


class TeamLeader(DateMixin):
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="team_leader_employee"
    )
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="team_leader_team"
    )

    def __str__(self):
        return self.employee.name


class TeamEmployee(DateMixin):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="team_employee_employee"
    )
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="team_employee_team"
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

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="work_arrangements"
    )
    work_arrangement = models.IntegerField(
        choices=WORK_ARRANGEMENT_CHOICES, default=FULL_TIME
    )

    def __str__(self):
        return self.employee.name
