"""Distillation 0: Direct access to potions module."""

from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    """Execute Distillation 0 demonstration."""
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potion: {healing_potion()}")


if __name__ == "__main__":
    main()
