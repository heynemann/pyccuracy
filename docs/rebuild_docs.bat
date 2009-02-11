@echo off
del .\build\*.* /Q /S /F
rd /S /Q .\build
md build
cls
sphinx-build -a source build