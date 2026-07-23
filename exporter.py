class Exporter:

    def save(

        self,

        calendars,

        filename="calendar_report.txt"

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            for item in calendars:

                file.write(

                    f"{item.calendar}: {item.value}\n"

                )
