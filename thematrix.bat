@echo off
color b
title The Matrix available at www.diberism.weebly.com , Last viewed %date% %time%
echo 	!--------------------!
echo 	!		     !
echo 	!   Start ( y or n ) !
echo 	!		     !
echo 	!--------------------!
set /p start=":"
IF %start%==y ( color a && goto :run ) else ( echo Exiting... && pause && exit )
pause

:run
echo %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random%
goto :run
pause