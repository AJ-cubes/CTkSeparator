from typing import Any, Union, Optional, Tuple

import customtkinter
import customtkinter as ctk
from PIL import ImageColor


class CTkSeparator(ctk.CTkBaseClass):
    def __init__(self,
                 master: Any,
                 length: int = 0,
                 line_weight: int = 4,
                 dashes: int = 1,
                 fg_color: Optional[Union[str, Tuple[str, ...]]] = None,
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
        if length < 0:
            raise ValueError("Length cannot be negative")
        if line_weight < 0:
            raise ValueError("Line Weight cannot be negative")
        if corner_radius < 0:
            raise ValueError("Corner Radius cannot be negative")
        if orientation.lower() not in ["horizontal", "vertical"]:
            raise ValueError("Orientation must be 'horizontal' or 'vertical'")
        if gap != 0.0 and dash_length != 0:
            raise ValueError("Both Gap and Dash Length cannot be used together")

        self._dashes = dashes
        self._master = master
        self._line_weight = line_weight
        self._fg_color = customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"] if fg_color is None else fg_color
        self._corner_radius = corner_radius
        self._orientation = orientation.lower()
        self._gap = gap
        self._length = 0
        self._separators = []
        self._config_length = length
        self._dash_length = dash_length
        self._draw = True
        self._tuple = True if isinstance(self._fg_color, tuple) else False
        self._colors = []

        if self._gap >= 0:
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
        if self._tuple:
            def hex_to_rgb(color):
                if not color.startswith("#"):
                    color = ImageColor.getrgb(color)
                else:
                    color = tuple(int(color[y:y + 2], 16) for y in (1, 3, 5))
                return color
            self._colors = []
            num_segments = len(self._fg_color) - 1
            steps_per_segment = self._dashes // num_segments

            for seg_index in range(num_segments):
                start_rgb = hex_to_rgb(self._fg_color[seg_index])
                end_rgb = hex_to_rgb(self._fg_color[seg_index + 1])

                for i in range(steps_per_segment):
                    ratio = i / (steps_per_segment - 1)
                    interpolated_rgb = tuple(
                        int(start_rgb[channel] + (end_rgb[channel] - start_rgb[channel]) * ratio)
                        for channel in range(3)
                    )
                    self._colors.append("#{:02X}{:02X}{:02X}".format(*interpolated_rgb))
        else:
            self._colors = [self._fg_color for _ in range(self._dashes)]

        self._length = int((self._config_length - ((self._dashes - 1) * self._gap)) / self._dashes) \
            if self._type == "gap" else self._dash_length if self._type == "dash_length" else 0
        self._gap = int((self._config_length - (self._dash_length * self._dashes)) / (self._dashes - 1)) \
            if self._type == "dash_length" else self._gap if self._type == "gap" else 0
        for separator in self._separators:
            separator.destroy()
        self._separators = []

        for x in range(self._dashes):
            params = {
                "master": self._separator_frame,
                "fg_color": self._colors[x],
                "corner_radius": self._corner_radius,
                "progress_color": self._colors[x],
            }

            if self._orientation == "horizontal":
                params.update({"width": self._length, "height": self._line_weight})
            else:
                params.update({"height": self._length, "width": self._line_weight})

            separator = ctk.CTkProgressBar(**params)
            self._separators.append(separator)

            self._padding = (0, self._gap) if x != (self._dashes - 1) else (0, 0)

            grid_args = {"column": x, "row": 0, "padx": self._padding, "pady": 0} if self._orientation == "horizontal" \
                else {"column": 0, "row": x, "padx": 0, "pady": self._padding}

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
        if "length" in kwargs and kwargs["length"] < 0:
            raise ValueError("Length cannot be negative")
        if "line_weight" in kwargs and kwargs["line_weight"] < 0:
            raise ValueError("Line Weight cannot be negative")
        if "corner_radius" in kwargs and kwargs["corner_radius"] < 0:
            raise ValueError("Corner Radius cannot be negative")
        if "orientation" in kwargs and kwargs["orientation"].lower() not in ["horizontal", "vertical"]:
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
            self._tuple = True if isinstance(self._fg_color, tuple) else False
            self._draw = True

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

    def bind(self, sequence=None, command=None, add="+"):
        return self._separator_frame.bind(sequence, command, add)


if __name__ == '__main__':
    def test_configure():
        test_separator.configure(orientation='vertical',
                                 length=700,
                                 dashes=70,
                                 corner_radius=0)


    app = ctk.CTk()
    test_separator = CTkSeparator(master=app,
                                  length=1300,
                                  line_weight=4,
                                  dashes=130,
                                  fg_color=("#0000FF", "#00FFFF", "#0000FF"),
                                  corner_radius=10,
                                  orientation='horizontal',
                                  gap=0.0)
    test_separator.grid(row=1, column=1, pady=12, padx=10)
    app.after(1000, test_configure)
    app.mainloop()
