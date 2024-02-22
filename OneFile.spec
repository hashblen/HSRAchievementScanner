# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_dynamic_libs

binaries = []
binaries += collect_dynamic_libs('vgamepad')


a = Analysis(
    ['src\\main.py'],
    pathex=[],
    binaries=binaries,
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
a.datas += [('assets\\tesseract\\tesseract.exe', 'src\\assets\\tesseract\\tesseract.exe', 'BINARY')]
a.datas += [('assets\\tesseract\\tessdata\\DIN-Alternate.traineddata','src\\assets\\tesseract\\tessdata\\DIN-Alternate.traineddata', "DATA")]
a.datas += [('assets\\images\\app.ico','src\\assets\\images\\app.ico', "DATA")]

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='HSRAchievementScanner',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='src\\assets\\images\\app.ico'
)
