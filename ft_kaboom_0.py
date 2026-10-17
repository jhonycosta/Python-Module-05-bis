"""Kaboom 0: Accessing grimoire module directly."""

from alchemy import grimoire


def main() -> None:
    """Test recording a light spell without explosion."""
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(
        f"Testing record light spell: "
        f"{grimoire.light_spell_record('Fantasy', 'Earth, wind and fire')}"
    )


if __name__ == "__main__":
    main()
