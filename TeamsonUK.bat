set original_dir=%CD%
set my_root_dir="C:\eCommerce Connections\EMEA\UK\Teamson UK"
cd %my_root_dir%
call %my_root_dir%\Teamson-venv\Scripts\activate.bat

python EU-TeamsonUK_Integration\StartIntegration.py 
:: Temporary fix to solve the 429 Error
python EU-TeamsonUK_Integration\StartIntegrationTracking.py 

call %my_root_dir%\Teamson-venv\Scripts\deactivate.bat
cd %original_dir%
exit /B 0