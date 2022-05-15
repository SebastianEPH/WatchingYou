echo off
title Run script - Py to EXE [Release]
pyinstaller ^
--clean   ^
--onefile  ^
--distpath "[RELEASE]"  ^
--windowed  ^
--icon "logo.ico"  ^
--name "Watching You" ^
--version-file "information_exe.txt"  ^
main.py
:cmd
pause null 
