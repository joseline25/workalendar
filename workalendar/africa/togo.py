from core import IslamoWesternCalendar, SAT, SUN
from registry_tools import iso_register


@iso_register('TG')
class Togo(IslamoWesternCalendar):
    "Togo"
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_easter_monday = True
    include_good_friday = False
    include_ascension = True
    include_whit_monday = True
    include_assumption = True
    include_all_saints = True

    # Islamic holidays
    include_day_after_prophet_birthday = False
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    include_day_of_sacrifice_label = "Feast of the Sacrifice"
    include_prophet_birthday = True

    FIXED_HOLIDAYS = IslamoWesternCalendar.FIXED_HOLIDAYS + (
        (1, 13, "Liberation Day"),
        (4, 27, "Independence Day"),
        (6, 21, "Martyrs's Day"),
        (9, 24, "Lomé's Attack Anniversary"),
    )

    # Togo has adopted the "western" workweek.
    WEEKEND_DAYS = (SAT, SUN)
