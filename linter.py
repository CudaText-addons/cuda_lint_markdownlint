#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jon LaBelle
# Copyright (c) 2017 Jon LaBelle
#
# License: MIT
# Ported to CudaLint by Alexey T.
#

"""This module exports the Markdownlint plugin class."""

import os
from shutil import which
from cuda_lint import Linter, util

if os.name=='nt':
    _node = 'node'
else:
    _node = which('node') or which('nodejs')

_js = os.path.join(os.path.dirname(__file__), 'node_modules', '.bin', 'markdownlint')

#print('node exists:', os.path.isfile(_node))
#print('script exists:', os.path.isfile(_js))


class Markdownlint(Linter):
    """Provides an interface to markdownlint."""

    syntax = 'Markdown'
    cmd = (_node, _js)
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = (r'.+?:'
             r'(?P<line>\d+)'
             r'(:(?P<col>\d+))?\s'
             r'(?P<error>MD\d+/[\w\-]+)\s'
             r'(?P<message>.+)')
    multiline = False
    line_col_base = (0, 0)
    tempfile_suffix = 'md'
    error_stream = util.STREAM_STDERR
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'
    config_file = ('--config', '.markdownlintrc', '~')
