from cx_Freeze import setup, Executable

includefiles = ["App_icon.ico", "logo.png"]


setup(name = "GUI",
      version = "2.1",
      description = "My GUI",
      options = {'build_exe': {'include_files':includefiles}},
      executables = [Executable("Main_File.py", base = "Win32GUI", icon="App_icon.ico",targetName="Travel_Fellow.exe")])
