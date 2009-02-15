@echo off
rd /s /q .\build\lib
setup.py bdist_egg upload
rd /s /q .\build\lib
setup.py bdist upload
rd /s /q .\build\lib
setup.py sdist upload