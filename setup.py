#!/usr/bin/env python3
# -*- Python -*-
# -*- coding: utf-8 -*-

import setuptools
from distutils.command.build import build
from distutils.command.install import install

build.sub_commands.append(('build_idl', None))
install.sub_commands.append(('install_idl', None))

setuptools.setup()

