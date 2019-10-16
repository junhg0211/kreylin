from os import environ
from sys import platform

from cx_Freeze import setup, Executable

from Constants import PROJECT_VERSION, PROJECT_NAME

environ['TCL_LIBRARY'] = r'.\venv_win\Lib\tcl8.6'
environ['TK_LIBRARY'] = r'.\venv_win\Lib\tcl8.6'

base = None
if platform == 'win32':
    base = 'Win32GUI'

build_options = {
    'packages': ('pygame', 'pyautogui')
}

executable = [Executable('./__main__.py', base=base, icon='./res/icon.ico', targetName='Kreylin.exe')]

setup(
    name=PROJECT_NAME,
    version=PROJECT_VERSION,
    description='Good Timer™',
    author='NOA "Sch" M. Canepina I',
    options={'build_exe': build_options},
    executables=executable,
    requires=['pygame', 'pyautogui', 'pyaudio', 'wave']
)
