from cx_Freeze import setup, Executable
from sys import platform
from os import environ

environ['TCL_LIBRARY'] = r'.\venv_win\Lib\tcl8.6'
environ['TK_LIBRARY'] = r'.\venv_win\Lib\tcl8.6'

base = None
if platform == 'win32':
    base = 'Win32GUI'

build_options = {
    'packages': ('pygame', 'pyautogui')
}

executable = [Executable('__main__.py', base=base, icon='./res/icon.ico', targetName='Kreylin.exe')]

setup(
    name='Kreylin',
    version='1.0',
    author='NOA "Sch" M. Canepina I',
    options={'build_exe': build_options},
    executables=executable
)
