"""Core workflow for Multiomics Network Explorer by Red@."""

PROJECT_NAME = "Multiomics Network Explorer"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
