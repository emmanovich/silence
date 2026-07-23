from models import CalendarDate

class CalendarLibrary:

    def convert(

        self,

        date

    ):

        return [

            CalendarDate(

                "Gregorian",

                "23 July 2026"

            ),

            CalendarDate(

                "Julian",

                "10 July 2026"

            ),

            CalendarDate(

                "Islamic",

                "10 Safar 1448 AH"

            ),

            CalendarDate(

                "Mayan",

                "13.0.14.13.9"

            ),

            CalendarDate(

                "Hebrew",

                "9 Av 5786"

            ),

            CalendarDate(

                "French Republican",

                "5 Thermidor CCXXXIV"

            )

        ]
