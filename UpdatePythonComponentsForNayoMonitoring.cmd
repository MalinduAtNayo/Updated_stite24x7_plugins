@echo off

REM !!!!!!! DO NOT EDIT ANYTHING BELOW THIS LINE !!!!!!!

title Update Python Components for %computername%
echo =====================================================================================================
echo - Nayo Managed Services - Update Python Components to support Nayo Monitoring
echo -
echo - Version: 1.1.0
echo -
echo - Use this tool to update Python components to support Nayo Monitoring.
echo - 
echo - IMPORTANT:  You must be logged into a Windows account that has local admin privelages!
echo -
echo - Press any key to update the Python components; otherwise, close this window to cancel this setup.
echo ======================================================================================================
pause

set CURR_DIR=%~dp0

cd /d %CURR_DIR%

python -m pip install requests
python -m pip install --upgrade pip
python -m pip install oracledb --upgrade
python -m pip install cx_Oracle --upgrade
pause
exit
