from matplotlib.cbook import get_sample_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from constants import Constants
import os
import tkinter as tk
import matplotlib.cbook as cbook
from datetime import datetime
import matplotlib.ticker as ticker
import numpy as np


class Graph:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.fig, self.ax = plt.subplots()

        self.image_path = cbook.get_sample_data(
            os.path.join(os.getcwd(), "pictures", "bg_graph.jpg")
        )

        self.img = plt.imread(self.image_path)
        self.fig.set_facecolor(Constants.BG_COLOR)
        # self.ax.imshow(self.img, extent=[-1, 5, 0, 6], aspect="auto")

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.parent_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def update_graph(self, df, options):
        self.df = df.head(options["qtd_apps"])
        self.y_lim = self.df["daily_usage_seconds"].max()
        if self.y_lim > 600:
            self.y_lim = self.y_lim * 1.15
        else:
            self.y_lim = 900

        self.setup_axes(options)
        self.plot_background_image(options)
        self.bars = self.plot_bars(self.df)
        self.configure_y_ticks(self.df["daily_usage_seconds"].max())
        self.configure_x_ticks()
        self.add_value_labels(self.bars)
        self.canvas.draw()

    def setup_axes(self, options):
        self.ax.clear()
        self.ax.set_title(self.parse_date(options["Date"]))
        self.ax.set_ylabel("Tempo de Uso", fontsize=16)
        self.ax.set_xlabel("Programas", fontsize=16)

    def parse_date(self, date):
        weekday_list_pt_br = [
            "Segunda-feira",
            "Terça-feira",
            "Quarta-feira",
            "Quinta-feira",
            "Sexta-feira",
            "Sábado",
            "Domingo",
        ]
        datetime_obj = datetime.strptime(date.split(".")[0], "%Y-%m-%d")
        weekday = weekday_list_pt_br[datetime_obj.weekday()]
        return f'{weekday} - {datetime_obj.strftime(f"%d/%m/%Y")}'

    def plot_background_image(self, options):
        self.ax.imshow(
            self.img, extent=[-0.7, options["qtd_apps"], 0, self.y_lim], aspect="auto"
        )

    def plot_bars(self, df):
        bars = self.ax.bar(
            df["app_name"],
            df["daily_usage_seconds"],
            color=Constants.BUTTON_ACTIVE_COLOR,
        )
        return bars

    def configure_y_ticks(self, max_value):
        self.ax.yaxis.set_major_formatter(ticker.FuncFormatter(self.format_hours))

        rounded_max_value = np.ceil(max_value / 900) * 900
        num_ticks = 5
        tick_interval = rounded_max_value / (num_ticks - 1)
        desired_ticks = [i * tick_interval for i in range(num_ticks)]
        self.ax.set_yticks(desired_ticks)

    def configure_x_ticks(self):
        formated_labels = [
            self.limit_text(label.get_text()) for label in self.ax.get_xticklabels()
        ]
        self.ax.set_xticks(self.ax.get_xticks())
        self.ax.set_xticklabels(formated_labels)

    def limit_text(self, text):
        max_length = 18
        if len(text) > max_length:
            return text[: max_length - 3] + "..."
        else:
            return text

    def add_value_labels(self, bars):
        for bar in bars:
            yval = bar.get_height()
            self.ax.text(
                bar.get_x() + bar.get_width() / 2,
                yval,
                self.format_hours(yval, 0),
                ha="center",
                va="bottom",
                color="black",
                fontsize=9,
            )

    def format_hours(self, x, _):
        hours = int(x // 3600)
        minutes = int((x % 3600) // 60)
        if hours == 0:
            return f"{minutes:02d}m"
        elif minutes == 0:
            return f"{hours:02d}h"
        else:
            return f"{hours:02d}h {minutes:02d}m"
