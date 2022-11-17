from core import IslamoWesternCalendar, ChineseNewYearCalendar, SAT, SUN
from registry_tools import iso_register


@iso_register('CM')
class Mauritius(IslamoWesternCalendar, ChineseNewYearCalendar):
    "Mauritius"
    "This calendar doesn't include the Hinduist's holidays since it is not yet included in the API"

    # Civil holidays
    include_labour_day = True
    # Christian holidays
    include_easter_monday = False
    include_good_friday = False
    include_ascension = False
    include_whit_monday = False
    include_assumption = True
    include_all_saints = False
    # Islamic holidays
    include_day_after_prophet_birthday = False
    include_eid_al_fitr = True
    include_day_of_sacrifice = False
    include_day_of_sacrifice_label = "Feast of the Sacrifice"

    FIXED_HOLIDAYS = IslamoWesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "New Year"),
        (1, 3, "New Year"),
        (2, 1, "Abolition of Slavery"),
        (3, 12, "National Day"),
        (11, 2, "Arrival of Indentured Labourers "),
    )

    # Ivory Coast has adopted the "western" workweek.
    WEEKEND_DAYS = (SAT, SUN)
