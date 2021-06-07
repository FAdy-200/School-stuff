from __future__ import annotations
from typing import Optional, Any
import hospital.config as config
import datetime
import sqlite3

idn = int


class DoubleEntryError(Exception):
    ...


class Database:
    def __init__(self, path_to_db: str, table: str, columns: str) -> None:
        """
        Implements access and query for database.

        Args:
            path_to_db (str): the FULL path_to_db
            table (str): the name of the table in the database
            columns (str): the name of the columns separated by commas
        """

        self.connection = sqlite3.connect(path_to_db)
        self.table = table
        self.cursor = self.connection.cursor()
        self.columns = columns

    def add_entry(
        self,
        hospital_id: idn,
        occupied_beds: int,
        used_ventilators: int,
        max_beds: int,
        max_ventilators: int,
        date: Optional[datetime.date] = None,
    ) -> None:
        """
        Add entry to database.

        Args:
            hospital_id (idn): the id of the hospital
            occupied_beds (int): number of occupied beds
            used_ventilators (int): number of used ventiltors
            max_beds (int): maximum number of beds in hospital
            max_ventilators (int): maximum number of ventiltors in hospital
            date (datetime.date or None): the date of the record. If None,
                current day is used
        """

        entry = (
            f"INSERT INTO '{self.table}' ({self.columns}) VALUES(?, ?, ?, ?,"
            " ?, ?)"
        )

        if date is None:
            date = datetime.datetime.now()

        entries = self.get_weeks_entries(hospital_id)

        for cur_entry in entries:
            cur_date = datetime.datetime.strptime(
                cur_entry["date"], config.DATE_FORMAT
            )
            cur_date_tup = (cur_date.year, cur_date.month, cur_date.day)
            if cur_date_tup == (date.year, date.month, date.day):
                raise DoubleEntryError("A record of that day already exists.")

        self.cursor.execute(
            entry,
            (
                hospital_id,
                occupied_beds,
                used_ventilators,
                max_beds,
                max_ventilators,
                date.strftime(config.DATE_FORMAT),
            ),
        )
        self.connection.commit()

    def get_weeks_entries(self, hospital_id: idn) -> list[dict[str, Any]]:
        """
        Get hospital records in last week.

        Args:
            hospital_id (idn): the id of the hospital

        Returns:
            List of dicts, each dict representing an entry. The key names is
            same as names of columns, and the value type matches that of the
            database.
        """

        now = datetime.datetime.now()
        week_time_delta = datetime.timedelta(days=7)

        week_ago = now - week_time_delta

        entries = self.connection.execute(
            f"SELECT {self.columns} from {self.table}"
        )

        hospital_entries = [
            entry for entry in entries if entry[0] == hospital_id
        ]

        week_entries = [
            {
                key: entry[val]
                for (val, key) in enumerate(config.DATABASE_COLUMNS)
            }
            for entry in hospital_entries
            if datetime.datetime.strptime(entry[-1], config.DATE_FORMAT)
            >= week_ago
        ]
        return week_entries
