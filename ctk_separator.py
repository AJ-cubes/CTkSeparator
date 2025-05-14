from typing import Any, Union, Optional, Tuple

import customtkinter
import customtkinter as ctk


class CTkSeparator(ctk.CTkBaseClass):
    def __init__(self,
                 master: Any,
                 length: int = 0,
                 line_weight: int = 4,
                 dashes: int = 1,
                 fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                 corner_radius: int = 10,
                 orientation: str = "horizontal",
                 gap: float = 0.0,
                 dash_length: float = 0.0):

        if dashes < 1:
            raise ValueError("Dashes must be at least 1")
        if gap < 0:
            raise ValueError("Gap cannot be negative")
        if dash_length < 0:
            raise ValueError("Dash Length cannot be negative")
        if orientation not in ["horizontal", "vertical"]:
            raise ValueError("Orientation must be 'horizontal' or 'vertical'")
        if gap != 0.0 and dash_length != 0:
            raise ValueError("Both Gap and Dash Length cannot be used together")

        self._dashes = dashes
        self._master = master
        self._line_weight = line_weight
        self._fg_color = customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"] if fg_color is None else fg_color
        self._corner_radius = corner_radius
        self._orientation = orientation
        self._gap = gap
        self._length = 0
        self._separators = []
        self._config_length = length
        self._dash_length = dash_length
        self._draw = True

        if self._gap > 0:
            self._type = "gap"
        elif self._dash_length > 0:
            self._type = "dash_length"

        self._separator_frame = ctk.CTkFrame(master=master,
                                             border_color=master.cget('fg_color'),
                                             bg_color=master.cget('fg_color'),
                                             fg_color=master.cget('fg_color'))
        super().__init__(master=master)

        if self._draw:
            self._draw_dashes()

    def _draw_dashes(self):
        self._length = int((self._config_length - ((self._dashes - 1) * self._gap)) / self._dashes) \
            if self._type == "gap" else self._dash_length if self._type == "dash_length" else 0
        self._gap = int((self._config_length - (self._dash_length * self._dashes)) / (self._dashes - 1)) \
            if self._type == "dash_length" else self._gap if self._type == "gap" else 0
        for separator in self._separators:
            separator.destroy()
        self._separators = []

        for i in range(self._dashes):
            params = {
                "master": self._separator_frame,
                "fg_color": self._fg_color,
                "corner_radius": self._corner_radius,
                "progress_color": self._fg_color,
            }

            if self._orientation == "horizontal":
                params.update({"width": self._length, "height": self._line_weight})
            else:
                params.update({"height": self._length, "width": self._line_weight})

            separator = ctk.CTkProgressBar(**params)
            self._separators.append(separator)

            self._padding = (0, self._gap) if i != (self._dashes - 1) else (0, 0)

            grid_args = {"column": i, "row": 0, "padx": self._padding, "pady": 0} if self._orientation == "horizontal" \
                else {"column": 0, "row": i, "padx": 0, "pady": self._padding}

            separator.grid(**grid_args)

    def pack(self,
             **kwargs):
        self._separator_frame.pack(**kwargs)

    def grid(self,
             **kwargs):
        self._separator_frame.grid(**kwargs)

    def place(self,
              **kwargs):
        self._separator_frame.place(**kwargs)

    def pack_forget(self):
        self._separator_frame.pack_forget()

    def grid_forget(self):
        self._separator_frame.grid_forget()

    def place_forget(self):
        self._separator_frame.place_forget()

    def destroy(self):
        self._separator_frame.destroy()

    def configure(self, **kwargs):
        if "dashes" in kwargs and kwargs["dashes"] < 1:
            raise ValueError("Dashes must be at least 1")
        if "gap" in kwargs and kwargs["gap"] < 0:
            raise ValueError("Gap cannot be negative")
        if "dash_length" in kwargs and kwargs["dash_length"] < 0:
            raise ValueError("Dash Length cannot be negative")
        if "orientation" in kwargs and kwargs["orientation"] not in ["horizontal", "vertical"]:
            raise ValueError("Orientation must be 'horizontal' or 'vertical'")
        if "gap" in kwargs and "dash_length" in kwargs:
            raise ValueError("Both Gap and Dash Length cannot be used together")

        if "length" in kwargs:
            self._config_length = kwargs.pop("length")
            self._draw = True

        if "line_weight" in kwargs:
            self._line_weight = kwargs.pop("line_weight")
            if self._orientation == "horizontal":
                for separator in self._separators:
                    separator.configure(height=self._line_weight)
            elif self._orientation == "vertical":
                for separator in self._separators:
                    separator.configure(width=self._line_weight)

        if "dashes" in kwargs:
            self._dashes = kwargs.pop("dashes")
            self._draw = True

        if "fg_color" in kwargs:
            self._fg_color = kwargs.pop("fg_color")
            for separator in self._separators:
                separator.configure(fg_color=self._fg_color, progress_color=self._fg_color)

        if "corner_radius" in kwargs:
            self._corner_radius = kwargs.pop("corner_radius")
            for separator in self._separators:
                separator.configure(corner_radius=self._corner_radius)

        if "orientation" in kwargs:
            self._orientation = kwargs.pop("orientation")
            self._draw = True

        if "gap" in kwargs:
            self._gap = kwargs.pop("gap")
            self._dash_length = 0
            self._type = "gap"
            self._draw = True

        if "dash_length" in kwargs:
            self._dash_length = kwargs.pop("dash_length")
            self._gap = 0
            self._type = "dash_length"
            self._draw = True

        if len(kwargs) > 0:
            raise ValueError(
                f"{list(kwargs.keys())} are not supported argument(s)")

        if self._draw:
            self._draw_dashes()


if __name__ == '__main__':
    def test_configure():
        test_separator.configure(fg_color="#0000FF",
                                 line_weight=10,
                                 corner_radius=1,
                                 length=250,
                                 dashes=5,
                                 orientation="vertical",
                                 gap=50)


    app = ctk.CTk()
    test_separator = CTkSeparator(master=app,
                                  length=500,
                                  line_weight=4,
                                  dashes=10,
                                  fg_color="#FFFFFF",
                                  corner_radius=10,
                                  orientation='horizontal',
                                  dash_length=45)
    test_separator.grid(row=1, column=1, pady=12, padx=10)
    app.after(1000, test_configure)
    app.mainloop()
