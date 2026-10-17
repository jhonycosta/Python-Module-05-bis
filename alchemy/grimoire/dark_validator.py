"""Dark validator module completing naive circular dependency."""
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Validate ingredients for dark magic formulas."""
    allowed: list[str] = dark_spell_allowed_ingredients()
    ingredients_lower: str = ingredients.lower()
    for item in allowed:
        if item.lower() in ingredients_lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
