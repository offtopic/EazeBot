cd %~dp0
del dist /F /Q
rmdir /S /Q build
python setup.py sdist bdist_wheel
python -m twine upload dist/*

pause