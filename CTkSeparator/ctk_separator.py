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
                 gap: float = 0.0):

        if dashes < 1:
            raise ValueError("Dashes must be at least 1")
        if gap < 0:
            raise ValueError("Gap cannot be negative")

        self._dashes = dashes
        self._master = master
        self._line_weight = line_weight
        self._fg_color = customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"] if fg_color is None else fg_color
        self._corner_radius = corner_radius
        self._orientation = orientation
        self._gap = gap
        self._length = int((length - ((self._dashes - 1) * self._gap)) / self._dashes)
        self._separators = []
        self._config_length = length

        self._separator_frame = ctk.CTkFrame(master=master,
                                             border_color=master.cget('fg_color'),
                                             bg_color=master.cget('fg_color'),
                                             fg_color=master.cget('fg_color'))
        if self._orientation == "horizontal":
            super().__init__(master=master, width=self._length, height=self._line_weight)
        elif self._orientation == "vertical":
            super().__init__(master=master, width=self._line_weight, height=self._length)

        self._draw_dashes()

    def _draw_dashes(self):
        self._length = int((self._config_length - ((self._dashes - 1) * self._gap)) / self._dashes)
        for separator in self._separators:
            separator.destroy()
        self._separators = []
        if self._orientation == "horizontal":
            for i in range(self._dashes):
                self._separators.append(ctk.CTkProgressBar(master=self._separator_frame,
                                                           width=self._length,
                                                           height=self._line_weight))
                self._separators[i].configure(fg_color=self._fg_color,
                                              corner_radius=self._corner_radius,
                                              progress_color=self._fg_color)
                if i != (self._dashes - 1):
                    self._separators[i].grid(column=i, row=0, padx=(0, self._gap), pady=0)
                else:
                    self._separators[i].grid(column=i, row=0, padx=0, pady=0)
        elif self._orientation == "vertical":
            for i in range(self._dashes):
                self._separators.append(ctk.CTkProgressBar(master=self._separator_frame,
                                                           height=self._length,
                                                           width=self._line_weight))
                self._separators[i].configure(fg_color=self._fg_color,
                                              corner_radius=self._corner_radius,
                                              progress_color=self._fg_color)
                if i != (self._dashes - 1):
                    self._separators[i].grid(column=0, row=i, padx=0, pady=(0, self._gap))
                else:
                    self._separators[i].grid(column=0, row=i, padx=0, pady=0)
        else:
            raise ValueError('Error: Make sure orientation is either horizontal or vertical')

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

        if "length" in kwargs:
            self._config_length = kwargs.pop("length")
            self._draw_dashes()

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
            self._draw_dashes()

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
            self._draw_dashes()

        if "gap" in kwargs:
            self._gap = kwargs.pop("gap")
            self._draw_dashes()

        if len(kwargs) > 0:
            raise ValueError(
                f"{list(kwargs.keys())} are not supported argument(s).")


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
                                  gap=5)
    test_separator.grid(row=1, column=1, pady=12, padx=10)
    app.after(1000, test_configure)
    app.mainloop()
