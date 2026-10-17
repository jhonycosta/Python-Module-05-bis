"""Alembic 0: Accessing root modules directly."""

import elements


def main() -> None:
    """Demonstrate direct module access with import elements."""
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
