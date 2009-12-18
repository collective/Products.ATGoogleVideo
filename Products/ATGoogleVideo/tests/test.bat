@echo off

REM Invoking unit test directly doesn't work anymore on Plone 2.5.1
REM See http://plone.org/documentation/error/attributeerror-test_user_1_

set MY_PLONE_VERSION=C:\Plone-2.5.5

set PYTHON=%MY_PLONE_VERSION%\Python\python.exe
set ZOPE_HOME=%MY_PLONE_VERSION%\Zope
set INSTANCE_HOME=%MY_PLONE_VERSION%\Data
set SOFTWARE_HOME=%ZOPE_HOME%\lib\python
set CONFIG_FILE=%INSTANCE_HOME%\etc\zope.conf
set PYTHONPATH=%SOFTWARE_HOME%
set TEST_RUN=%ZOPE_HOME%\bin\test.py

"%PYTHON%" "%TEST_RUN%" --config-file="%CONFIG_FILE%" --usecompiled -vp --package-path=%INSTANCE_HOME%/Products/ATGoogleVideo Products.ATGoogleVideo
