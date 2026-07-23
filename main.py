from config import DEFAULT_DATE
from repository import Repository
from converter import Converter
from formatter import Formatter
from statistics import Statistics
from exporter import Exporter

Repository().load()

converted = Converter().build(

    DEFAULT_DATE

)

Formatter().show(

    DEFAULT_DATE,

    converted

)

stats = Statistics().build(

    converted

)

Statistics().print(

    stats

)

Exporter().save(

    converted

)
