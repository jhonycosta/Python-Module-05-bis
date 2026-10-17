"""Light spell validator verifying ingredients against the light spellbook."""

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Validate ingredients case-insensitively for light spells."""
    allowed: list[str] = light_spell_allowed_ingredients()
    ingredients_lower: str = ingredients.lower()
    for item in allowed:
        if item.lower() in ingredients_lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
