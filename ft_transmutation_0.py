"""Transmutation 0: Accessing transmutation recipes directly."""

import alchemy.transmutation.recipes


def main() -> None:
    """Demonstrate direct access to transmutation recipes."""
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(
        f"Testing lead to gold: "
        f"{alchemy.transmutation.recipes.lead_to_gold()}"
    )


if __name__ == "__main__":
    main()
