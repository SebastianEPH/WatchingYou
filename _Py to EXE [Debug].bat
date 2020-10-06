echo off
color cf
title Run script - Py to EXE [DEBUG]
pyinstaller --clean   --distpath "[DEBUG] EXE" -F --icon "icon.ico" --version-file dataEXE.txt Antiplagiarism.py
:cmd
pause null 
