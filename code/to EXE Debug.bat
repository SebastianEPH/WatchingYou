echo off
title Py to EXE [DEBUG]
pyinstaller ^
--clean  ^
--onefile  ^
--distpath "[DEBUG]" ^
--icon "logo.ico" ^
--name "Watching You - DEBUG" ^
--version-file "information_exe.txt" ^
main.py
:cmd
pause null 
