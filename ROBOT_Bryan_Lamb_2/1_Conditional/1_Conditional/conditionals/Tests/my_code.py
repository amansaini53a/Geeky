import tkinter as tk
from tkinter import ttk


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(DistanceConverter, self).__init__(*args, **kwargs)
        self.title("Distance Converter")
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        feet_to_meters = FeetToMeters(container, self)
        feet_to_meters.grid(padx=60, pady=30, sticky="NSEW")

        meters_to_feet = MetersToFeet(container, self)
        meters_to_feet.grid(padx=60, pady=30, sticky="NSEW")

        self.frames[MetersToFeet] = meters_to_feet
        self.frames[FeetToMeters] = feet_to_meters


        # self.bind("<Return>", frame.calculate)
        # self.bind("<KP_Enter>", frame.calculate)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class MetersToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super(MetersToFeet, self).__init__(container, **kwargs)

        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar()

        meters_label = ttk.Label(self, text="Meters")
        meters_input = ttk.Entry(self, width=10, textvariable=self.meters_value)
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(
            self,
            text="Switch to Feet Conversion",
            command=lambda: controller.show_frame(FeetToMeters)
        )

        meters_label.grid(column=0, row=0, sticky="W")
        meters_input.grid(column=1, row=1, sticky="EW")
        meters_input.focus()
        feet_label.grid(row=0, column=0, sticky="W")
        feet_display.grid(row=0, column=1, sticky="EW")
        calc_button.grid(row=2, column=0, sticky="EW", columnspan=2)
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def calculate(self, *args):
        try:
            meters = float(self.meters_value.get())
            feet = meters * 3.28084
            self.feet_value.set(f"{feet: .3f}")
        except ValueError:
            pass


class FeetToMeters(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super(FeetToMeters, self).__init__(container, **kwargs)

        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar()

        feet_label = ttk.Label(self, text="Feet")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value)
        meters_label = ttk.Label(self, text="Meters:")
        meters_display = ttk.Label(self, textvariable=self.meters_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(
            self,
            text="Switch to meters Conversion",
            command=lambda: controller.show_frame(MetersToFeet)
        )

        feet_label.grid(row=0, column=0, sticky="W")
        feet_input.grid(row=0, column=1, sticky="EW")
        feet_input.focus()
        meters_label.grid(row=1, column=0, sticky="W")
        meters_display.grid(row=1, column=1, sticky="EW")
        calc_button.grid(row=0, column=2, sticky="EW", columnspan=2)
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            meters = feet / 3.28084
            self.meters_value.set(f"{meters: .3f}")
        except ValueError:
            pass


root = DistanceConverter()
root.columnconfigure(0, weight=1)
root.mainloop()
