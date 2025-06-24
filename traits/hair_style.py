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
        "hair in a high ponytail",
        "hair in a low ponytail",
        "hair in a side ponytail",
        "hair in a braided ponytail",

        # ─── Buns ────────────────────────────────────────────
        "hair in a tight bun",
        "hair in a messy bun",
        "hair in a low bun",
        "hair in a top knot bun",
        "hair in double buns",

        # ─── Updos ───────────────────────────────────────────
        "hair in a classic updo",
        "hair in a twisted updo",
        "hair in a half updo",
        "hair in a chignon updo",

        # ─── Braids ──────────────────────────────────────────
        "hair in a single braid",
        "hair in double braids",
        "hair in a French braid",
        "hair in a Dutch braid",
        "hair in a fishtail braid",
        "hair in a waterfall braid",

        # ─── Half-up / swept ─────────────────────────────────
        "hair in a half up, half down style",
        "side-swept hair",
        "pulled-back hair",

        # ─── Textured & natural ─────────────────────────────
        "hair with defined ringlets",
        "hair with loose ringlets",
        "hair in a natural afro",
        "hair in a twist-out",
    ]

    return random.choice(hair_styles)
