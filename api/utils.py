from unicodedata import decimal
from .models import WorkArrangement


def calculate_employee_monthly_salary(
    hourly_rate, hours_per_week=40, team_leader=None
) -> float:
    """
    Calculate montly salary based on work_arrangement and hourly_rate,
    if employee is team leader, add 10% to salary
    """

    salary = (4 * hours_per_week) * hourly_rate

    if team_leader:
        # add 10% to salary
        salary = salary + (salary * 0.1)

    return float(salary)
