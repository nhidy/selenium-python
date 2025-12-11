@echo off
setlocal

echo ---------------------------
echo Setting up JCodeGen...
echo ---------------------------

:: Lấy thư mục hiện tại
set CURRENT_DIR=%~dp0
set CURRENT_DIR=%CURRENT_DIR:~0,-1%
echo Current directory: %CURRENT_DIR%

:: Thêm CURRENT_DIR vào PATH nếu chưa có
echo Checking PATH...
echo %PATH% | findstr /C:"%CURRENT_DIR%" >nul
if errorlevel 1 (
    echo Adding %CURRENT_DIR% to PATH...
    setx PATH "%PATH%;%CURRENT_DIR%"
) else (
    echo PATH already contains %CURRENT_DIR%.
)

:: Chuẩn bị đường dẫn tuyệt đối tới JCodeGen.exe
set JCODEGEN_EXE=%CURRENT_DIR%\JCodeGen.exe

:: Tạo file .reg tạm thời
set REG_FILE=%TEMP%\add_jcodegen_context.reg
(
echo Windows Registry Editor Version 5.00
echo.
echo [HKEY_CLASSES_ROOT\*\shell\Build with JCodeGen]
echo @="Build with JCodeGen"
echo.
echo [HKEY_CLASSES_ROOT\*\shell\Build with JCodeGen\command]
echo @="cmd.exe /c JCodeGen.exe --input \"%%1\""
) > "%REG_FILE%"

:: Import .reg vào Registry
echo Importing registry keys...
reg import "%REG_FILE%"

:: Xóa file .reg tạm
del "%REG_FILE%"

echo ---------------------------
echo Setup completed successfully!
echo - PATH updated with %CURRENT_DIR%
echo - Context menu added for *.jcodegen.json (click right and Build)
echo ---------------------------

pause
endlocal
