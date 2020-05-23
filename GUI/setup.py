from cx_Freeze import setup, Executable
#from setuptools import setup
import matplotlib
import mpl_toolkits
base='Win32GUI'
executable = [
    Executable("V1_1.py", base = base)
]
build_options = {"packages": ["tkinter", "tkinter.filedialog", "numpy"]}
setup(
    name = "Projectiles Calculator",
    options = {"build_exe": build_options},
    version = "1.1",
    executables = executable
      )