from core import IslamoWesternCalendar, SAT, SUN
from registry_tools import iso_register


@iso_register('TG')
class BurkinaFaso(IslamoWesternCalendar):
    "Burkina Faso"
    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_easter_monday = True
    include_good_friday = False
    include_ascension = True
    include_whit_monday = False
    include_assumption = True
    include_all_saints = True

    # Islamic holidays
    include_day_after_prophet_birthday = False
    include_eid_al_fitr = True
    include_day_of_sacrifice = True
    include_day_of_sacrifice_label = "Feast of the Sacrifice"
    include_prophet_birthday = True

    FIXED_HOLIDAYS = IslamoWesternCalendar.FIXED_HOLIDAYS + (
        (1, 3, "Soulèvement Populaire"),
        (3, 8, "International Women Day"),
        (8, 5, "National Day"),
        (10, 31, "Martyrs's Day"),
        (12, 11, "Independence Day"),
    )

    # Burkina Faso has adopted the "western" workweek.
    WEEKEND_DAYS = (SAT, SUN)






