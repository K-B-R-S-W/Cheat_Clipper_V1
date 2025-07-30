@echo off

:: Run the Python script with pythonw.exe in hidden mode
powershell -WindowStyle Hidden -Command "Start-Process pythonw.exe -ArgumentList '"%~dp0main.py"' -WindowStyle Hidden"