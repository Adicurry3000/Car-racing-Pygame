import cx_Freeze


executables = [cx_Freeze.Executable("gaming.py")]

cx_Freeze.setup(
    name="A Bit Racey",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["car.png", "Crash.wav", "Swagger.mp3", 'caricon.png']}},
    executables=executables

)