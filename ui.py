# ui.py

import tkinter as tk
from tkinter import scrolledtext
from npc.npc import NPC
from traits.hair_colour import generate_hair_colour

class NPCGeneratorApp(tk.Tk):
    """Encapsulates the entire Tkinter-based UI for NPC generation."""

    def __init__(self):
        super().__init__()
        # ── Window setup ───────────────────────────────────────────
        self.title("D&D NPC Generator")
        self.geometry("500x450")

        # ── Prepare storage for override controls ───────────────────
        # We'll track one IntVar & StringVar per trait in these dicts
        self.override_vars = {}  
        self.entry_vars    = {}

        # ── Frame to hold override checkboxes & entries ────────────
        override_frame = tk.Frame(self)
        override_frame.pack(fill=tk.X, padx=10, pady=(10, 0))

        # ── List the traits you want overrides for ─────────────────
        traits = ["race", "gender"]
        for idx, trait in enumerate(traits):
            self._add_override_field(override_frame, trait, row=idx)

        # ── Generate button ───────────────────────────────────────
        self.generate_btn = tk.Button(
            self,
            text="Generate NPC",
            command=self.on_generate
        )
        self.generate_btn.pack(pady=15)

        # ── Output text area ──────────────────────────────────────
        self.text_area = scrolledtext.ScrolledText(
            self,
            wrap=tk.WORD,
            height=12,
            state=tk.DISABLED
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0,10))


    def _add_override_field(self, parent, trait, row):
        """
        Create a Checkbutton + Entry for a given trait.
        Stores the IntVar and StringVar, and saves the Entry widget.
        """
        # 1) Create the variables
        ov_var = tk.IntVar(value=0)
        en_var = tk.StringVar()

        # 2) Store them for later use
        self.override_vars[trait] = ov_var
        self.entry_vars[trait]    = en_var

        # 3) Checkbutton to toggle the override
        cb = tk.Checkbutton(
            parent,
            text=f"Override {trait.capitalize()}",
            variable=ov_var,
            command=lambda t=trait: self._toggle_entry(t)
        )
        cb.grid(row=row, column=0, sticky=tk.W)

        # 4) Entry for custom value (starts disabled)
        entry = tk.Entry(
            parent,
            textvariable=en_var,
            state=tk.DISABLED,
            width=20
        )
        entry.grid(row=row, column=1, padx=5)

        # 5) Save the Entry widget for enabling/disabling
        setattr(self, f"{trait}_entry_widget", entry)


    def _toggle_entry(self, trait):
        """
        Enable or disable the Entry associated with 'trait'
        based on the Checkbutton’s IntVar.
        """
        var = self.override_vars[trait]
        widget = getattr(self, f"{trait}_entry_widget")

        if var.get():  
            widget.config(state=tk.NORMAL)
        else:
            # Clear the entry when disabling
            self.entry_vars[trait].set("")
            widget.config(state=tk.DISABLED)


    def on_generate(self):
        """
        1) Instantiate NPC
        2) Apply any checked overrides
        3) Recompute hair colour if race changed
        4) Build and display the formatted text block
        """
        npc = NPC()

        # Apply overrides dynamically
        for trait, ov_var in self.override_vars.items():
            if ov_var.get():  # if override is checked
                custom_val = self.entry_vars[trait].get().strip()
                if custom_val:
                    setattr(npc, trait, custom_val)
                    # If race changed, refresh hair colour
                    if trait == "race" and npc.hair_length != "Bald":
                        npc.hair_colour = generate_hair_colour(npc.race)

        # Build the hair line
        if npc.hair_length == "Bald":
            hair_line = "Bald"
        else:
            hair_line = f"{npc.hair_length} {npc.hair_colour} {npc.hair_style}"

        # Compose the final output block
        output = (
            f"Name: {npc.name}\n"
            f"Race: {npc.race}\n"
            f"Gender: {npc.gender}\n"
            f"Hair: {hair_line}\n"
            "Description:\n"
            f"{npc.description}\n"
        )

        # Display in the read-only text area
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, output)
        self.text_area.config(state=tk.DISABLED)

