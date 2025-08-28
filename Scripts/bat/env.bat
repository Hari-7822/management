@echo off
setlocal enabledelayedexpansion

for /f "usebackq delims=" %%A in ("D:\code\New\management\.env") do (
    set line=%%A
    set key=!line:~0,!
    set value=!line:~!
    echo !key! = !value!
)

endlocal
