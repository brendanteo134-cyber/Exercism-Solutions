from datetime import datetime, timedelta
from enum import Enum
class WeekDay(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
DAYS_IN_A_WEEK = 7
def delivery_date(start: str, description: str) -> str:
    start_date = datetime.fromisoformat(start)
    delivery_date: datetime | None = None
    match description:
        case "NOW":
            delivery_date = start_date + timedelta(hours=2)
        case "ASAP":
            is_morning = start_date.hour < 13
            if is_morning:
                delivery_date = start_date.replace(
                    hour=17, minute=0, second=0
                )
            else:
                tomorrow_date = start_date + timedelta(days=1)
                delivery_date = tomorrow_date.replace(
                    hour=13, minute=0, second=0
                )
        case "EOW":
            is_beginning_of_week = start_date.weekday() < 3
            if is_beginning_of_week:
                friday_date = get_next_day(start_date, WeekDay.FRIDAY)
                delivery_date = friday_date.replace(
                    hour=17, minute=0, second=0
                )
            else:
                sunday_date = get_next_day(start_date, WeekDay.SUNDAY)
                delivery_date = sunday_date.replace(
                    hour=20, minute=0, second=0
                )
        case _ if nth_month := get_nth_month(description):
            nth_month_date = start_date.replace(
                month=nth_month, day=1, hour=8, minute=0, second=0
            )
            nth_month_is_passed = start_date.month >= nth_month
            if nth_month_is_passed:
                delivery_date = get_first_workday_of_next_year(nth_month_date)
            else:
                delivery_date = get_first_workday(nth_month_date)
        case _ if nth_quarter := get_nth_quarter(description):
            last_workday_of_nth_quarter_date = get_last_workday_of_nth_quarter(
                start_date, nth_quarter
            )
            delivery_date = last_workday_of_nth_quarter_date
    if delivery_date is None:
        raise ValueError(f"Cannot find delivery date for {description}")
    return delivery_date.isoformat()
def get_next_day(start_date: datetime, target_day: WeekDay) -> datetime:
    temporary_date = start_date
    for _ in range(DAYS_IN_A_WEEK):
        temporary_date = temporary_date + timedelta(days=1)
        if temporary_date.weekday() == target_day.value:
            return temporary_date
    raise ValueError(f"No {target_day.name} found")
def get_nth_month(description: str) -> int | None:
    nth_month = description[:-1]
    if description.endswith("M") and nth_month.isdigit():
        return int(nth_month)
    return None
def get_nth_quarter(description: str) -> int | None:
    nth_quarter = description[1:]
    if description.startswith("Q") and nth_quarter.isdigit():
        return int(nth_quarter)
    return None
def get_first_workday_of_next_year(start_date: datetime) -> datetime:
    next_year_date = start_date.replace(year=start_date.year + 1)
    return get_first_workday(next_year_date)
def get_first_workday(start_date: datetime) -> datetime:
    for _ in range(DAYS_IN_A_WEEK):
        if start_date.weekday() < 5:
            return start_date
        start_date = start_date + timedelta(days=1)
    raise ValueError("No workday found")
def get_last_workday_of_nth_quarter(
    start_date: datetime, nth_quarter: int
) -> datetime:
    is_last_quarter = nth_quarter == 4
    last_workday: datetime | None = None
    if is_last_quarter:
        last_workday = start_date.replace(
            year=start_date.year + 1,
            month=1,
            day=1,
            hour=8,
            minute=0,
            second=0,
        )
    else:
        last_workday = start_date.replace(
            month=(nth_quarter * 3) + 1, day=1, hour=8, minute=0, second=0
        )
    is_last_workday_passed = start_date > last_workday
    if is_last_workday_passed:
        last_workday = last_workday.replace(year=last_workday.year + 1)
    for _ in range(DAYS_IN_A_WEEK):
        last_workday = last_workday - timedelta(days=1)
        if last_workday.weekday() < 5:
            return last_workday
    raise ValueError("No workday found")
