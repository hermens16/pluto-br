Set WshShell = CreateObject("WScript.Shell")

WshShell.CurrentDirectory = "C:\Users\User\Dev\pluto-tv"

' atualiza a playlist
WshShell.Run "cmd /c atualizar_pluto.bat", 0, True

' organiza a playlist
WshShell.Run "py organizar_pluto.py", 0, True