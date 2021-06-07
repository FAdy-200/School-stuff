import hospital.config as config
from hospital.app.stat import Stats
from hospital.app.data import Database
from tkinter import Label, Tk
from tkinter import messagebox
import sys


ventilator, bed = True, False


class Metric:
    """
    used for items to be displayed in the GUI
    """

    def __init__(self, name, value):
        self.name = name
        self.value = value


if __name__ == '__main__':
    path_to_db = "/".join(sys.path[0].split("/")[:-1]) + "/data/database.db"
else:
    path_to_db = sys.path[0] + "/data/database.db"


def get_metrics():
    db = Database(
            path_to_db, config.TABLE_NAME, config.DATABASE_COLUMNS_STR
        )

    stats = Stats(db)

    avg_beds = [
        Metric(
            "Average number of beds per week for hospital 1",
            stats.average_used(bed, 1),
        ),
        Metric(
            "Average number of beds per week for hospital 2",
            stats.average_used(bed, 2),
        ),
    ]

    avg_vents = [
        Metric(
            "Average number of ventilators per week for hospital 1",
            stats.average_used(ventilator, 1),
        ),
        Metric(
            "Average number of ventilators per week for hospital 2",
            stats.average_used(ventilator, 2),
        ),
    ]

    occ_percentage_beds = [
        Metric(
            "Beds occupancy percentage for hospital 1",
            stats.percentage(bed, 1),
        ),
        Metric(
            "Beds occupancy percentage for hospital 2",
            stats.percentage(bed, 2),
        ),
    ]

    occ_percentage_vents = [
        Metric(
            "Ventilators occupancy percentage for hospital 1",
            stats.percentage(ventilator, 1),
        ),
        Metric(
            "Ventilators occupancy percentage for hospital 2",
            stats.percentage(ventilator, 2),
        ),
    ]
    alert = [stats.check_occupancy(1, 90), stats.check_occupancy(2, 90)]

    return {
        "stats": [
            *avg_beds,
            *avg_vents,
            *occ_percentage_beds,
            *occ_percentage_vents,
        ],
        "alerts": alert,
    }


class ApplicationWindow(Tk):
    """
    Main window for officials
    """

    def __init__(self):
        # initializing window properties
        super().__init__()
        self.labels_height = 50
        self.title("Officials Application")
        self.geometry(config.WIN_SIZE_STR)
        # self.minsize(config.WIN_MIN_WIDTH, config.WIN_MIN_HEIGHT)

        # creating a header
        self.heading = self.create_label(
            text="Officials Application",
            isheader=True,
            font=config.WIN_HEADER_FONT,
        )

        # looping through the metrics to be displayed
        for metric in get_metrics()["stats"]:
            self.create_stat(metric)

        # popping up a message in case capacity increased over 90%
        if get_metrics()["alerts"][0]:
            messagebox.showwarning(
                "Alert", "+90% capacity exceeded in hospital 1"
            )

        if get_metrics()["alerts"][1]:
            messagebox.showwarning(
                "Alert", "+90% capacity exceeded in hospital 2"
            )

    def create_label(
        self,
        text: str,
        font: str,
        color: str = config.WIN_TXT_COLOR,
        x: int = 0,
        y: int = 0,
        isheader: bool = False,
    ) -> Label:
        """
        :param text:        text of the label
        :param font         font of text
        :param color:       color of text
        :param x:           x-coordinate of label
        :param y:           y-coordinate of label
        :param isheader:    stating whether the label used as header
        :return:            tk.Label object
        """
        label = Label(self, text=text, font=font, fg=color)
        if isheader:
            label.place(x=self.winfo_reqheight(), y=self.labels_height)
            self.labels_height += 150
        else:
            label.place(x=x, y=y)
        return label

    def create_stat(self, metric: Metric) -> tuple[Label, Label]:
        """
        :param metric:      metric to be displayed
        :return:            two labels, one for the text of the metric, and
                            other for its value
        """
        metric_label = self.create_label(
            metric.name,
            font=config.WIN_TXT_FONT,
            color=config.WIN_TXT_COLOR,
            x=20,
            y=self.labels_height,
            isheader=False,
        )
        value_label = self.create_label(
            metric.value,
            font=config.WIN_TXT_FONT,
            color=config.WIN_TXT_COLOR,
            x=self.winfo_reqwidth() + 500,
            y=self.labels_height,
            isheader=False,
        )
        self.labels_height += 80
        return metric_label, value_label


if __name__ == "__main__":
    window = ApplicationWindow()
    window.mainloop()
