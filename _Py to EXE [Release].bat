echo off
color a0
Run script - Py to EXE [Release]
pyinstaller --clean   --distpath "[RELEASE] EXE" -F --windowed --icon "icon.ico" --version-file dataEXE.txt Antiplagiarism.py
:cmd
pause null 
