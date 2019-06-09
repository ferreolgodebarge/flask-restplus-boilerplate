# -*- mode: python -*-

from PyInstaller.building.build_main import (
    Analysis,
    PYZ,
    EXE,
    COLLECT,
    TOC,
)
import os
import flask_restplus


pkg_data = TOC()


def get_folder_path(dirpath, folder):
    return os.path.join(dirpath, folder)


def add_file_to_pkg(pkg, dest_folder, src_folder, f):
    pkg.append((
        'flask_restplus/{}/{}'.format(dest_folder, f),
        os.path.join(src_folder, f),
        'DATA',
    ))


def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path:
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts


def get_file_dir(src, target):
    src_len = len(splitall(src)) - 1
    res = ''
    for s in splitall(target)[src_len:]:
        res = res + s + '/'
    return res[:-1]


def add_folder_to_pkg(src_folder):
    for root, directories, files in os.walk(src_folder):
        for f in files:
            dest_dir = get_file_dir(src_folder, root)
            add_file_to_pkg(pkg_data, dest_dir, root, f)


flask_lib_folder = os.path.dirname(flask_restplus.__file__)
flask_template_folder = get_folder_path(flask_lib_folder, 'templates')
flask_static_folder = get_folder_path(flask_lib_folder, 'static')

add_folder_to_pkg(flask_template_folder)
add_folder_to_pkg(flask_static_folder)

block_cipher = None

pathex = os.path.abspath(os.path.join(__name__, os.pardir))

a = Analysis(
    ['application\\app.py'],
    pathex=[pathex],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    pkg_data,
    strip=False,
    upx=True,
    name='app',
)
