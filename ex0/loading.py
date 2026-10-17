"""Dynamic reagent loader and dependency management demonstrator."""

import importlib


def check_reagent(name: str, purpose: str) -> tuple[bool, str]:
    """Dynamically import a module and report its status."""
    try:
        mod: object = importlib.import_module(name)
        version: str = str(getattr(mod, "__version__", "unknown"))
        return True, f"[OK] {name} ({version}) - {purpose}"
    except (ImportError, ModuleNotFoundError):
        return False, f"[MISSING] {name} - Not installed"


def main() -> None:
    """Inspect reagent availability and explain dependency workflows."""
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")

    pd_ok, pd_msg = check_reagent("pandas", "Data manipulation ready")
    np_ok, np_msg = check_reagent("numpy", "Numerical computation ready")

    print(pd_msg)
    print(np_msg)

    print("\npip vs Poetry:")
    print(
        "requirements.txt declares what to install; pip resolves it "
        "at install time."
    )
    print(
        "pyproject.toml declares the same constraints, and Poetry pins "
        "the resolved"
    )
    print("versions in poetry.lock so every install is identical.\n")

    if pd_ok and np_ok:
        print("All reagents present and accounted for.")
    else:
        print("Missing reagents detected. To install them, run:")
        print("With pip:")
        print("pip install -r ex0/requirements.txt\n")
        print("With Poetry:")
        print("poetry install")
        print("poetry run python ex0/loading.py")


if __name__ == "__main__":
    main()
