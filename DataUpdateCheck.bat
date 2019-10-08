:: *****************************************************************************
:: DataUpdateCheck.bat  4/10/2019 
:: Summary: Send Email if RPZ Vote Data has changed on AGO
::
:: Description:    
:: Scheduled Task: Every day @ 7:00 am 
::
:: Path: \\geobase-win\ced\GADS\R2019\R013\DataUpdateCheck\DataUpdateCheck.bat
:: *****************************************************************************

:: Set log directory for process verification file
    SET LogDir=\\geobase-win\ced\GADS\R2019\R013\DataUpdateCheck\log\DataUpdateCheck

:: Set variable %theDate% to today's date (YYYYMMDD)
    for /f "tokens=2,3,4 delims=/ " %%a in ('date/t') do set theDate=%%c%%a%%b

:: Record starting time
    time /T > %LogDir%%theDate%.log

Echo Downloading data and updating AGO ... >> %LogDir%%theDate%.log
 ::Send standard output (1) & errors (2) to log file
    "C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" \\geobase-win\ced\GADS\R2019\R013\DataUpdateCheck\DataUpdateCheck.py 1>>%LogDir%%theDate%.log 2>&1

:: Record ending time
    time /T >> %LogDir%%theDate%.log

::For manual testing -
::pause
 
