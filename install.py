#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys 

path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)

import settings
import utils

utils.prepare_dir()
