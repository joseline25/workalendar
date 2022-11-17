from core import IslamoWesternCalendar, SAT, SUN
from registry_tools import iso_register


@iso_register('SN')
class Senegal(IslamoWesternCalendar):
    "Senegal"
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
    include_ash_wednesday = True
    include_day_after_prophet_birthday = True
    include_laylat_al_qadr = True

    FIXED_HOLIDAYS = IslamoWesternCalendar.FIXED_HOLIDAYS + (
        (1, 20, "Army Day"),
        (3, 26, "Martyrs's Day"),
        (4, 18, "Martyrs's Day"),
        (5, 25, "Africa's Day"),
        (9, 22, "Independence Day"),
        (9, 23, "Independence Day"),

    )

    # Togo has adopted the "western" workweek.
    WEEKEND_DAYS = (SAT, SUN)





