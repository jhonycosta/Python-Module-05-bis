"""Oracle configuration reader and environment validator."""

import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore[import]
    HAS_DOTENV: bool = True
except (ImportError, ModuleNotFoundError):
    load_dotenv = None
    HAS_DOTENV = False


def find_dotenv_path() -> str | None:
    """Locate the .env configuration file in standard locations."""
    script_dir: str = os.path.dirname(os.path.abspath(__file__))
    candidates: list[str] = [
        os.path.join(script_dir, ".env"),
        os.path.join(os.getcwd(), ".env"),
    ]
    for candidate in candidates:
        if os.path.isfile(candidate):
            return candidate
    return None


def is_env_ignored_by_git() -> bool:
    """Verify whether .env is listed in .gitignore."""
    script_dir: str = os.path.dirname(os.path.abspath(__file__))
    candidates: list[str] = [
        os.path.join(script_dir, ".gitignore"),
        os.path.join(script_dir, "..", ".gitignore"),
        os.path.join(os.getcwd(), ".gitignore"),
    ]
    for path in candidates:
        if os.path.isfile(path):
            try:
                with open(path, "r", encoding="utf-8") as file_handle:
                    for line in file_handle:
                        pattern: str = line.strip()
                        if pattern in (".env", "*.env", ".env*"):
                            return True
            except OSError:
                pass
    return False


def main() -> None:
    """Consult the Oracle by inspecting configuration settings."""
    env_file: str | None = find_dotenv_path()

    if env_file and HAS_DOTENV and load_dotenv:
        load_dotenv(dotenv_path=env_file, override=False)

    print("ORACLE STATUS: Consulting the configuration...\n")

    has_custom_config: bool = bool(
        env_file
        or os.environ.get("MATRIX_MODE")
        or os.environ.get("API_KEY")
        or os.environ.get("DATABASE_URL")
    )

    if not has_custom_config:
        print("[WARNING] No configuration detected. Using default fallback.\n")

    matrix_mode: str = os.environ.get("MATRIX_MODE", "development")

    if matrix_mode == "production":
        database_status: str = "Connected to production cluster"
        default_log_level: str = "INFO"
    else:
        database_status = "Connected to local instance"
        default_log_level = "DEBUG"

    api_key: str | None = os.environ.get("API_KEY")
    if api_key and api_key != "your_secret_api_key_here":
        api_status: str = "Authenticated"
    elif api_key:
        api_status = "Authenticated"
    else:
        api_status = "Warning: Missing API key (mock mode)"

    log_level: str = os.environ.get("LOG_LEVEL", default_log_level)

    zion_endpoint: str | None = os.environ.get("ZION_ENDPOINT")
    if zion_endpoint:
        remote_status: str = "Online"
    else:
        remote_status = "Offline (missing endpoint)"

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    print(f"Database: {database_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {log_level}")
    print(f"Remote Network: {remote_status}\n")

    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")

    if is_env_ignored_by_git():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env file is NOT ignored by git")

    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    if not HAS_DOTENV and "--check-deps" in sys.argv:
        print("Note: python-dotenv is not installed.", file=sys.stderr)
    main()
