"""Laboratory sealing detector and environment inspector."""

import os
import site
import sys


def is_virtual_environment() -> bool:
    """Check if the current script is running within a virtual environment."""
    return (
        sys.prefix != getattr(sys, "base_prefix", sys.prefix)
        or "VIRTUAL_ENV" in os.environ
    )


def get_reagent_path() -> str:
    """Retrieve the primary site-packages directory for installed reagents."""
    if hasattr(site, "getsitepackages"):
        packages: list[str] = site.getsitepackages()
        if packages:
            return packages[0]
    return os.path.join(
        sys.prefix,
        "lib",
        f"python{sys.version_info.major}.{sys.version_info.minor}",
        "site-packages",
    )


def main() -> None:
    """Inspect and display laboratory isolation status."""
    python_exec: str = sys.executable

    if not is_virtual_environment():
        print("LABORATORY STATUS: You are working in the open\n")
        print(f"Current Python: {python_exec}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print(r"lab_env\Scripts\activate # On Windows")
        print("\nThen run this program again.")
    else:
        env_path: str = sys.prefix
        env_name: str = os.path.basename(env_path)
        pkg_path: str = get_reagent_path()

        print("LABORATORY STATUS: The laboratory is sealed\n")
        print(f"Current Python: {python_exec}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}\n")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.\n")
        print("Reagent installation path:")
        print(pkg_path)


if __name__ == "__main__":
    main()
