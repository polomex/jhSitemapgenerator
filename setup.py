#!/usr/bin/python3
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='jhSitemapgenerator',
      version='0.1.3',
      description='A multithreaded commandline tool to create sitemap.xml|.gz|.txt files from a website.',
      license='GPL3+',
      author='Jan Helbling',
      author_email='jan.helbling@gmail.com',
      url='http://www.jan-helbling.ch/~jhelbling/linux.py?gpl3-opensource-programm=jhSitemapgenerator-a-multithreaded-tool-to-create-sitemap.xml-from-shell',
      platforms=['linux','freebsd','netbsd','unixware7' , 'openbsd' , 'windows'],
      scripts=['bin/jhSitemapgenerator.py'],
)
