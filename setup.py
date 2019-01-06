from cx_Freeze import setup, Executable

setup(name="Mygame",
      version="1.0",
      description="my game",
      options={"build.exe":{"packages":["pygame"],
                            "included_files":["vivi.png","anastasia.png","Bird.png"]}},
      executables=[Executable("george_abc.py")])
