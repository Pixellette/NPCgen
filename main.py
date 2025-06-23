# main.py

import tkinter as tk
from tkinter import scrolledtext
from npc.npc import NPC   # your generator

class NPCGeneratorApp(tk.Tk):
    """Main application window for the D&D NPC Generator."""
    def __init__(self):
        super().__init__()  
        # ── Window setup ───────────────────────────────────────────────
        self.title("D&D NPC Generator")
        self.geometry("500x850")   # width x height in pixels

        # ── Generate button ────────────────────────────────────────────
        # Store it on self so you could, e.g., disable it later if needed.
        self.generate_btn = tk.Button(
            self,
            text="Generate NPC",
            command=self.on_generate   # call the method below
        )
        self.generate_btn.pack(pady=10)

        # ── Output area ────────────────────────────────────────────────
        # A scrollable, read-only text widget for easy copy/paste.
        self.text_area = scrolledtext.ScrolledText(
            self,
            wrap=tk.WORD,      # wrap at word boundaries
            height=12,         # visible lines
            state=tk.DISABLED  # start read-only
        )
        # fill both directions & allow it to expand if window is resized
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0,10))

        # ── Future hooks ───────────────────────────────────────────────
        # Here is where you could add Entry/OptionMenu widgets for:
        #   - self.name_entry  = tk.Entry(self)
        #   - self.race_menu   = tk.OptionMenu(self, self.race_var, ...)
        #   - etc.
        # Then in on_generate() you’d check if the user filled them,
        # and if so override npc.name, npc.race, etc.

    def on_generate(self):
        """
        Called when the user clicks “Generate NPC”.
        Instantiates NPC(), builds a nicely formatted block of text,
        and displays it in the read-only text_area.
        """
        # 1) Generate your NPC object
        npc = NPC()

        # 2) Build the hair line: handle Bald vs styled hair
        if npc.hair_length == "Bald":
            hair_line = "Bald"
        else:
            hair_line = f"{npc.hair_length} {npc.hair_colour} {npc.hair_style}"

        # 3) Compose the full, multi-line output
        output = (
            f"Name: {npc.name}\n"
            f"Race: {npc.race}\n"
            f"Gender: {npc.gender}\n"
            f"Hair: {hair_line}\n"
            "Description:\n"
            f"{npc.description}\n"
        )

        # 4) Update the text_area
        self.text_area.config(state=tk.NORMAL)   # make editable
        self.text_area.delete("1.0", tk.END)     # clear old contents
        self.text_area.insert(tk.END, output)    # insert new block
        self.text_area.config(state=tk.DISABLED) # back to read-only

if __name__ == "__main__":
    # Entry point: create the app instance and start the event loop
    app = NPCGeneratorApp()
    app.mainloop()

    