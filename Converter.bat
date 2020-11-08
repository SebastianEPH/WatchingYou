echo off
color 5f
title Run script - Py to EXE [DEBUG]
pyinstaller --clean   --distpath "[Compile DEBUG] EXE"  main.py
:cmd
pause null 
