from csv import writer
from typing import List

from movs.model import Row


def convert(row: Row) -> List[str]:
    return [
        row.data_contabile.isoformat(),
        row.data_valuta.isoformat(),
        str(row.addebiti),
        str(row.accrediti),
        row.descrizione_operazioni
    ]


def write_csv(fn: str, csv: List[Row]) -> None:
    with open(fn, 'w', newline='', encoding='utf-8') as csvfile:
        spamwriter = writer(csvfile)
        for row in csv:
            spamwriter.writerow(convert(row))
