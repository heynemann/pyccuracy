@echo off
rd /s /q .\build\lib
setup.py sdist upload