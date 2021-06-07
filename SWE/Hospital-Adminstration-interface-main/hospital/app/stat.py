from __future__ import annotations
from hospital.app.data import Database

idn = int
item = bool
ventilator, bed = True, False


class Stats:
    def __init__(self, db: Database) -> None:
        self.db = db

    def average_used(
        self,
        cur_item: item,
        hospital_id: idn,
    ) -> float:
        """
        Returns average usage of an item in the current week.

        Args:
            cur_item (item): ventilator or bed
            hospital_id (idn): the id of the hospital

        Returns:
            float, the value of the average.
        """

        entries = self.db.get_weeks_entries(hospital_id)
        if len(entries) == 0:
            return 0

        if cur_item is ventilator:
            return sum([entry["ven_ent"] for entry in entries]) / len(entries)
        else:
            return sum([entry["in_care_ent"] for entry in entries])

    def percentage(
        self,
        cur_item: item,
        hospital_id: idn,
    ) -> float:
        """
        Returns the percentage of item usage in the last day.

        Args:
            cur_item (item): ventilator or bed
            hospital_id (idn): the id of the hospital

        Returns:
            float, the percentage of usage of item.
        """

        entries = self.db.get_weeks_entries(hospital_id)

        if len(entries) == 0:
            return 0

        if cur_item is ventilator:
            return entries[-1]["ven_ent"] / entries[-1]["max_ven_ent"] * 100
        else:
            return (
                entries[-1]["in_care_ent"] / entries[-1]["max_bed_ent"] * 100
            )

    def check_occupancy(
        self,
        hospital_id: idn,
        threshold: int = 90,
    ) -> bool:
        """
        Checks if the occupancy of ventiltors or beds reached a threshold for
        three consecutive days.

        Args:
            cur_item (item): ventilator or bed
            hospital_id (idn): the id of the hospital

        Returns:
            bool
        """

        entries = self.db.get_weeks_entries(hospital_id)
        ventilators_state = [
            (entry["ven_ent"] / entry["max_ven_ent"]) > threshold / 100
            for entry in entries
        ]
        beds_state = [
            (entry["in_care_ent"] / entry["max_bed_ent"]) > threshold / 100
            for entry in entries
        ]
        total_state = [
            cur_vent_state or cur_bed_state
            for (cur_vent_state, cur_bed_state) in zip(
                ventilators_state, beds_state
            )
        ]

        for i in range(2, len(total_state)):
            if total_state[i] and total_state[i - 1] and total_state[i - 2]:
                return True

        return False
