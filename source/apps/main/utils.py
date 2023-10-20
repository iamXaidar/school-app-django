from typing import List, Tuple

SCHOOL_FOUNDATION_YEAR = 2019
ACTIVE_YEAR = 2024

main_menu = ["ACTIVE CLASSES", "CLASSES ARCHIVE", "TEACHERS", "STAFF", "MANAGEMENT"]

class_years = [i for i in range(SCHOOL_FOUNDATION_YEAR, ACTIVE_YEAR + 1)]


def make_year_fields(year: int, year_arr: List[int]) -> List[Tuple]:
    year_form_fields = list(enumerate(year_arr, start=year))
    year_form_fields.insert(0, ("", "----"))
    return year_form_fields


class GeneralContext:
    def get_general_context(self, **kwargs):
        context = kwargs
        menu = main_menu.copy()
        context["menu"] = menu

        return context
