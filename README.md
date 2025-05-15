# CTkSeparator
A customizable separator for `CustomTkinter`.

## Installation
```sh
pip install CTkSeparator
```

## Usages
Here are the parameters in CTkSeparator:

| Parameter      | Description |
|---------------|-------------|
| `length`      | **Must be positive.** Defines how long the CTkSeparator is, regardless of orientation. |
| `line_weight` | **Must be positive.** Determines the thickness of the CTkSeparator. Defaults to 4 if not set. |
| `dashes`      | **Must be positive.** Specifies the number of dashes. If set to 1, it becomes a single solid line. |
| `fg_color`    | **Must be a string or tuple of strings.** Sets the color of the dashes. Accepts a tuple to create a gradient effect, transitioning smoothly between colors. |
| `corner_radius` | **Must be positive.** Defines the corner radius for each dash. |
| `orientation` | **Must be either `'horizontal'` or `'vertical'`.** Determines the direction of the CTkSeparator. |
| `gap`        | **Must be positive.** Controls the spacing between dashes. **Cannot be used with `dash_length`.** |
| `dash_length` | **Must be positive.** Specifies the width of the dashes. **Cannot be used with `gap`.** |


## Arguments
1. `configure` It is your normal configure function. It can configure any of your parameters in CTkSeparator.
2. `bind` The bind function attaches events to the separator, though behavior may vary depending on CustomTkinter's widget handling.


## Examples
Here's a preview of how the CTkSeparator works in action:

![CTkSeparator Example](https://raw.githubusercontent.com/AJ-cubes/CTkSeparator/refs/heads/main/examples/CTkSeparator%20Example.png "CTkSeparator Example")

### Code Example

[Demo.py](https://github.com/AJ-cubes/CTkSeparator/blob/main/examples/demo.py)

```python
import customtkinter as ctk
from CTkSeparator import CTkSeparator


app = ctk.CTk()

above = ctk.CTkLabel(master=app,
                     text="Above the CTkSeparator")
above.pack(pady=12, padx=10)
test_separator = CTkSeparator(master=app,
                              length=500,
                              line_weight=4,
                              dashes=10,
                              fg_color=("#FFFFFF", "#000000", "#FFFFFF"),
                              corner_radius=10,
                              orientation='horizontal',
                              gap=5)
test_separator.pack(pady=12, padx=10)
below = ctk.CTkLabel(master=app,
                     text="Below the CTkSeparator")
below.pack(pady=12, padx=10)
app.mainloop()

```

## License
MIT License

Copyright (c) 2025 AJ-cubes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Thanks
I want to give a huge thanks to everyone using this library. Cheers!