echo off
color 5f
title Run script - Py to EXE [DEBUG]
pyinstaller --clean   --distpath "[Compile DEBUG] EXE" -F  --uac-admin --icon "icon.ico" --version-file dataEXE.txt main.py
:cmd
pause null 
