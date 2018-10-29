#!/usr/bin/env python
"""The setup and build script for the EazeBot library."""

import codecs
import re
from os import path
from setuptools import setup as setupBase
import sys
from cx_Freeze import setup as setupFreeze
from cx_Freeze import Executable
import os.path


PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
description = "Free python/telegram bot for easy execution and surveillance of crypto trading plans on multiple exchanges"

def requirements(full=True):
    """Build the requirements list for this project"""
    requirements_list = []
    with open('requirements.txt') as requirements:
        for install in requirements:
            if full:
                requirements_list.append(install.strip())
            else:
                install = re.search('^\S+(?=\s|\Z)',install).group(0).strip()
                if install == 'python-telegram-bot':
                    install = 'telegram'
                requirements_list.append(install)
    return requirements_list

packages = ['eazebot']

with codecs.open('readme.md', 'r', 'utf-8') as fd:
    fn = path.join('eazebot/version.txt')
    with open(fn) as fh:
	    __version__ = re.search('(?<=version = ).+',str(fh.read())).group(0)
    with open(path.join('eazebot/APIs.json')) as fh:
        if '"apiKeyBinance": "YOURBINANCEKEY"' not in str(fh.read()):
            raise Exception('Modified key file! Possibly wrong folder?')
    long_description = fd.read()
			
		
if sys.argv[1] == 'build':
	base = None
	if sys.platform == 'win32':
		base = 'Win32GUI'  
	executables = [Executable("eazebot/eazebot.py", base=base)]
	includefiles = ['Link to Eazebot Wiki.url','readme.md','botLogo.png','LICENSE','LICENSE.LESSER','eazebot/botConfig.json','eazebot/APIs.json','requirements.txt','eazebot/version.txt','eazebot/updateBot.bat','eazebot/startBot.bat']
	packages.append('idna')
	packages += requirements(False)

	options = {
		'build_exe': {    
			'packages':packages,
			'include_files':includefiles,
			'excludes':["tkinter"],#, "PyQt4.QtSql", "sqlite3", 
                                  #"scipy.lib.lapack.flapack",
                                  #"PyQt4.QtNetwork",
                                  #"PyQt4.QtScript",
                                  #"numpy.core._dotblas", 
                                  #"PyQt5"],
            'optimize':2,
			},
	}
	setupFreeze(
		name = "EazeBot",
		author = 'Marcel Beining',
		author_email = 'marcel.beining@gmail.com',
		license='LGPLv3',
		keywords='python telegram bot api crypto trading',
		url = 'https://github.com/marcelbeining/eazebot',
		options = options,
		version = __version__,
		description = description,
		executables = executables
	)
elif sys.argv[1] == 'sdist':
    setupBase(name = 'eazebot',
          version=__version__,
		  author = 'Marcel Beining',
          author_email = 'marcel.beining@gmail.com',
		  url = 'https://github.com/marcelbeining/eazebot',
		  download_url = 'https://github.com/marcelbeining/cryptotrader/archive/EazeBot_%s.tar.gz'%__version__,
          license='LGPLv3',
          keywords='python telegram bot api crypto trading',
          description=description,
          long_description=long_description,
		  long_description_content_type='text/markdown',
          packages=packages,
		  include_package_data=True,
          install_requires=requirements(),
          classifiers=[
              'Development Status :: 3 - Alpha',
              'Intended Audience :: End Users/Desktop',
              'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
              'Operating System :: OS Independent',
			  'Topic :: Office/Business :: Financial',
              'Topic :: Communications :: Chat',
              'Topic :: Internet',
              'Programming Language :: Python',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6'
          ],)