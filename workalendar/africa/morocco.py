from core import IslamicCalendar
from registry_tools import iso_register


@iso_register('MA')
class Morocco(IslamicCalendar):
    "Morocco"

    include_new_years_day = True

    # Civil holidays
    include_labour_day = True

    FIXED_HOLIDAYS = (
        (1, 11, "Independence Manifesto"),
        (7, 30, "Throne Day"),
        (8, 14, "Anniversary of the Recovery Oued Ed-Dahab"),
        (8, 20, "Anniversary of the Revolution of the King and the People"),
        (8, 21, "Youth Day"),
        (11, 6, "Anniversary of the Green March"),
        (11, 18, "Independence Day"),
    )
    include_start_ramadan = True
    include_eid_al_fitr = True
    length_eid_al_fitr = 2
    include_eid_al_adha = True
    length_eid_al_adha = 2
    include_prophet_birthday = True

