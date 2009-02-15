@echo off
for /f %%a IN ('dir /b test*.py') do call run_test.bat %%a