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
