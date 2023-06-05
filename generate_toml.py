#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path

cwd = os.getcwd()
read_path = Path('pyproject.toml.in')
write_path = Path('pyproject.toml')

content = read_path.read_text()
content = content.replace('PROJECT_PATH', cwd)

write_path.write_text(content)


