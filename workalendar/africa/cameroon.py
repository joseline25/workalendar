from core import IslamoWesternCalendar, SAT, SUN
from registry_tools import iso_register


@iso_register('CM')
class Cameroon(IslamoWesternCalendar):
    "Cameroon"
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_easter_monday = False
    include_good_friday = True
    include_ascension = True
    include_whit_monday = False
    include_assumption = True
    include_all_saints = False
    # Islamic holidays
    include_day_after_prophet_birthday = False
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    include_day_of_sacrifice_label = "Feast of the Sacrifice"

    FIXED_HOLIDAYS = IslamoWesternCalendar.FIXED_HOLIDAYS + (
        (5, 20, "National Day"),
        (2, 11, "Youth Day"),
    )

    # Ivory Coast has adopted the "western" workweek.
    WEEKEND_DAYS = (SAT, SUN)
