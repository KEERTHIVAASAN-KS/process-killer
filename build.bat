@echo off
pyinstaller processkiller.py --onefile
copy dist\processkiller.exe processkiller.exe
del dist
del build\processkiller\localpycs
del build\processkiller
rmdir dist
rmdir build\processkiller\localpycs
rmdir build\processkiller
rmdir build
del processkiller.spec

