from cx_Freeze import setup, Executable
from distutils.core import setup
import matplotlib
base='Win32GUI'
executable = [
    Executable("V1_2.py", base = base)
]
build_options = {'includes': ['matplotlib.backends.backend_tkagg'],
                 "packages": ["tkinter", "tkinter.filedialog"]}
setup(
    name = "ProjectilesCalculator",
    options = {"build_exe": build_options},
    version = "1.2",
    executables = executable
      )
