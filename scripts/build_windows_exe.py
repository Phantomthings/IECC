"""Build a Windows executable for IE Charge Dashboard using PyInstaller.

This script packages the FastAPI application with its static assets so the
generated `.exe` can be executed from any directory. Run it on a Windows
machine with Python and PyInstaller installed.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DIST_NAME = "IEChargeDashboard"


def build() -> None:
    """Generate the PyInstaller build for Windows.

    The build uses the `onedir` mode so assets remain accessible without
    extraction delays, and includes the templates, static files and assets
    directories that the application needs at runtime.
    """

    dist_dir = PROJECT_ROOT / "dist"
    build_dir = PROJECT_ROOT / "build"

    # Start from a clean slate to avoid stale assets.
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    if build_dir.exists():
        shutil.rmtree(build_dir)

    add_data_args = []
    for folder in ("templates", "static", "assets"):
        source = PROJECT_ROOT / folder
        if not source.exists():
            raise FileNotFoundError(f"Resource directory missing: {source}")
        add_data_args.extend([
            "--add-data",
            f"{source}{os.pathsep}{folder}",
        ])

    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--onedir",
        "--name",
        DIST_NAME,
        *add_data_args,
        str(PROJECT_ROOT / "main.py"),
    ]

    print("Running PyInstaller to build Windows executable...\n")
    subprocess.run(command, check=True)

    print(
        "\nBuild complete. The executable folder is available at:",
        dist_dir / DIST_NAME,
    )
    print(
        "\nTo launch the app:",
        f"\n  {dist_dir / DIST_NAME / (DIST_NAME + '.exe')}\n",
        "The server will start on http://127.0.0.1:8000/ by default.",
        sep="",
    )


if __name__ == "__main__":
    build()
