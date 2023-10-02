from cx_Freeze import Executable, setup

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {'packages': ['tkinter', 'string', 'random']}

base = None
setup(
    name="Password Generator",
    version='1.0',
    description="Password Generator!",
    options={'build_exe': build_exe_options},
    executables=[Executable('gui.py', base=base, icon='./password-icon.ico')],
)