from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("calculo_eta.py", base=base)]

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": ["unittest"],
    "zip_include_packages": ["tkinter","encodings", "PySide6", "shiboken6"],
}

setup(
    name="calculo_eta",
    version="0.1",
    description="Programa para calcular o ETA das embarcações!",
    options={"build_exe": build_exe_options},
    executables=executables
)