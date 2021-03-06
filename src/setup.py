# -*- coding: utf-8 -*-
#
# Created on Oct 15, 2013
# @authors: Jiri Spilka
# http://people.ciirc.cvut.cz/~spilkjir
# @2015, CIIRC, Czech Technical University in Prague
#
# Licensed under the terms of the GNU GENERAL PUBLIC LICENSE
# (see CTGViewer.py for details)

from cx_Freeze import setup, Executable
import os
import shutil

# general settings
BASE_DIR = os.path.dirname(__file__)
OUT_DIR = os.path.join(BASE_DIR, 'build')

INNO_SCRIPT = 'setup_inno.iss'  # the script with Inno setup commands for the CTGViewer
INNO_EXECUTABLE = '"c:\\Program Files\\Inno Setup 5\\ISCC.exe"'  # path to the installed Inno Setup

# delete output dir
if os.path.exists(OUT_DIR):
    shutil.rmtree(OUT_DIR)

# Process the includes, excludes and packages first
# include exe file of vcredist_x86.exe
# include _ufuncs, libifcoremd, libmmd otherwise unable to start
# info: http://stackoverflow.com/questions/19633757/using-cx-freeze-with-scipy-scipy-special-ufuncs-py
includefiles = [os.path.join(BASE_DIR, '..\\win32\\vcredist_x86.exe'),
                ('c:\\Python27\\Lib\\site-packages\\scipy\\special\\_ufuncs.pyd', '_ufuncs.pyd'),
                ('c:\\Python27\\Lib\\site-packages\\numpy\\core\\libifcoremd.dll', 'libifcoremd.dll'),
                ('c:\\Python27\\Lib\\site-packages\\numpy\\core\\libmmd.dll', 'libmmd.dll')]
includes = ["scipy.io.matlab.streams", "numpy.core.multiarray"]
excludes = ['tcl', 'Tkinter']
packages = ["reportlab", "scipy"]
path = []

exeTarget = Executable(
    script=os.path.join("CTGViewer.py"),
    base="Win32GUI",
    compress=True,
    copyDependentFiles=True,
    )

setup(
    name="CTGViewer",
    version="0.3.20",
    description="CTGViewer application",
    author="Jiri Spilka",
    author_email='jiri.spilka@ciirc.cvut.cz',
    url='http://people.ciirc.cvut.cz/~spilkjir',
    options={"build_exe": {"includes": includes,
                           "include_files": includefiles,
                           "excludes": excludes,
                           "packages": packages,
                           "path": path
                           }
             },
    executables=[exeTarget]
    )

os.system(INNO_EXECUTABLE + " " + INNO_SCRIPT)  # run the Inno Setup

print('Build complete')
