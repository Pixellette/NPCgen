# ui.py

import tkinter as tk
from tkinter import ttk, scrolledtext
from npc.npc import NPC
from traits.hair_colour import generate_hair_colour, FALLBACK
from traits.race import RACE_OPTIONS
from traits.gender import GENDER_OPTIONS

class NPCGeneratorApp(tk.Tk):
    """All UI code separated out—dropdown + typing overrides for each trait."""

    def __init__(self):
        super().__init__()
        self.title("D&D NPC Generator")
        self.geometry("500x800")

        # Store our override & entry variables by trait name
        self.override_vars = {}  # e.g. {'race': IntVar, 'gender': IntVar}
        self.entry_vars    = {}  # e.g. {'race': StringVar, 'gender': StringVar}

        # ── Build override controls frame ──────────────────────────
        override_frame = tk.Frame(self)
        override_frame.pack(fill=tk.X, padx=10, pady=10)

        # Map each trait to its valid dropdown options
        fallback_colors = [color for color, _ in FALLBACK]
        trait_options = {
            "race":   RACE_OPTIONS,
            "gender": GENDER_OPTIONS,
            "hair_colour": fallback_colors
        }

        # Loop & create one row per trait
        for row, (trait, options) in enumerate(trait_options.items()):
            self._add_override_field(override_frame, trait, options, row)

        # ── Generate button ───────────────────────────────────────
        self.generate_btn = tk.Button(
            self,
            text="Generate NPC",
            command=self.on_generate
        )
        self.generate_btn.pack(pady=15)

        # ── Output area ───────────────────────────────────────────
        self.text_area = scrolledtext.ScrolledText(
            self,
            wrap=tk.WORD,
            height=12,
            state=tk.DISABLED
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0,10))


    def _add_override_field(self, parent, trait, options, row):
        """
        Creates:
          - A Checkbutton to toggle override for `trait`
          - A Combobox populated with `options` that also allows typing
        Stores the IntVar & StringVar and the widget itself on self.
        """
        # 1) Vars to track the checkbox & combobox contents
        ov_var = tk.IntVar(value=0)
        en_var = tk.StringVar()

        self.override_vars[trait] = ov_var
        self.entry_vars[trait]    = en_var

        # 2) Checkbox to enable override
        cb = tk.Checkbutton(
            parent,
            text=f"Override {trait.capitalize()}",
            variable=ov_var,
            command=lambda t=trait: self._toggle_entry(t)
        )
        cb.grid(row=row, column=0, sticky=tk.W)

        # 3) Combobox for picking or typing a custom value
        combo = ttk.Combobox(
            parent,
            textvariable=en_var,
            values=options,
            state="disabled"  # start disabled
        )
        combo.grid(row=row, column=1, padx=5)

        # 4) Save the widget for later enable/disable
        setattr(self, f"{trait}_entry_widget", combo)


    def _toggle_entry(self, trait):
        """
        Called when the override checkbox changes.
        Enables/disables the corresponding Combobox widget.
        """
        widget = getattr(self, f"{trait}_entry_widget")
        if self.override_vars[trait].get():
            # Allow both selecting from dropdown and typing new text
            widget.config(state="normal")
        else:
            # Clear & disable
            self.entry_vars[trait].set("")
            widget.config(state="disabled")


    def on_generate(self):
        """
        1) Make a new NPC()
        2) Apply any overrides (via setattr)
        3) If race changed, recalc hair_colour
        4) Format and display the final block
        """
        npc = NPC()

        # 2) Loop through each overridable trait
        for trait, var in self.override_vars.items():
            if var.get():  # checkbox is ticked
                custom = self.entry_vars[trait].get().strip()
                if custom:
                    setattr(npc, trait, custom)
                    # ensure hair colour matches a custom race
                    if trait == "race" and npc.hair_length != "Bald":
                        npc.hair_colour = generate_hair_colour(npc.race)

        # 3) Build the hair line
        if npc.hair_length == "Bald":
            hair_line = "Bald"
        else:
            hair_line = f"{npc.hair_length} {npc.hair_colour} {npc.hair_style}"

        # 4) Compose the output
        output = (
            f"Name: {npc.name}\n"
            f"Race: {npc.race}\n"
            f"Gender: {npc.gender}\n"
            f"Hair: {hair_line}\n"
            "Description:\n"
            f"{npc.description}\n"
        )

        # Show it in our read-only text area
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, output)
        self.text_area.config(state=tk.DISABLED)

