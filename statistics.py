class Statistics:

    def build(

        self,

        calendars

    ):

        return {

            "systems":

                len(calendars),

            "longest":

                max(

                    calendars,

                    key=lambda c:

                    len(c.value)

                ).calendar

        }

    def print(

        self,

        stats

    ):

        print(

            "Statistics\n"

        )

        print(

            f"Calendar systems: {stats['systems']}"

        )

        print(

            f"Longest representation: {stats['longest']}"

        )
