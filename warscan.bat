@echo off
color a
:findnum
set /a one=%random% %%255
set /a two=%random% %%255
set /a three=%random% %%255
set /a four=%random% %%255
set ip=%one%.%two%.%three%.%four%
echo %ip%
ping -n 1 -w 600 %ip%>ping.txt && goto :ipfound
goto :findnum
pause

:ipfound
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do     rem"') do (
  set "DEL=%%a"
)

call :colorEcho a0 "IP found - %ip%"
:colorEcho
echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1i
echo.
echo %ip%>>iplist.txt
goto :findnum
pause

