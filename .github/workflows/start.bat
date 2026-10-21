@echo off

echo starting...
python start.py

mode con:cols=120 lines=1000

python main.py
pause
EXIT /b 0
