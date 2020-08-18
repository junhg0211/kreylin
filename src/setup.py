from os import environ
from sys import platform

from cx_Freeze import setup, Executable

from constants import PROJECT_VERSION, PROJECT_NAME

environ['TCL_LIBRARY'] = r'.\venv_win\Lib\tcl8.6'
environ['TK_LIBRARY'] = r'.\venv_win\Lib\tcl8.6'

base = None
if platform == 'win32':
    base = 'Win32GUI'

# noinspection SpellCheckingInspection
build_options = {
    'packages': ('pygame', 'pyautogui', 'pyaudio', 'wave')
}

executable = [Executable('./__main__.py', base=base, icon='./res/icon.ico', targetName='Kreylin.exe')]

# noinspection SpellCheckingInspection
setup(
    name=PROJECT_NAME,
    version=PROJECT_VERSION,
    description='Good Timer™',
    author='Sch Jeon',
    options={'build_exe': build_options},
    executables=executable,
    requires=['pygame', 'pyautogui', 'pyaudio', 'wave']
)
