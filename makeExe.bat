cd %~dp0
del dist /F /Q
rmdir /S /Q build
python setup.py build && start makeSetup.iss
pause