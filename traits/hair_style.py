import random

def generate_hair_style():
    # Styles grouped by category; each entry fits after "[length] [colour]"
    hair_styles = [
        # ─── Loose ──────────────────────────────────────────
        "loose straight hair",
        "loose wavy hair",
        "loose curly hair",
        "loose frizzy hair",
        "loose coiled hair",

        # ─── Ponytails ───────────────────────────────────────
        "in a high ponytail",
        "in a low ponytail",
        "in a side ponytail",
        "in a braided ponytail",

        # ─── Buns ────────────────────────────────────────────
        "in a tight bun",
        "in a messy bun",
        "in a low bun",
        "in a top knot bun",
        "in double buns",

        # ─── Updos ───────────────────────────────────────────
        "in a classic updo",
        "in a twisted updo",
        "in a half updo",
        "in a chignon updo",

        # ─── Braids ──────────────────────────────────────────
        "in a single braid",
        "in double braids",
        "in a French braid",
        "in a Dutch braid",
        "in a fishtail braid",
        "in a waterfall braid",

        # ─── Half-up / swept ─────────────────────────────────
        "half up, half down",
        "side-swept hair",
        "pulled-back hair",

        # ─── Textured & natural ─────────────────────────────
        "defined ringlets",
        "loose ringlets",
        "natural afro",
        "in a twist-out",
    ]

    return random.choice(hair_styles)
