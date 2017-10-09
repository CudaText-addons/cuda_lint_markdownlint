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
from cuda_lint import Linter, util

_node = 'node' if os.name=='nt' else 'nodejs'
_js = os.path.join(os.path.dirname(__file__), 'node_modules', '.bin', 'markdownlint')


class Markdownlint(Linter):
    """Provides an interface to markdownlint."""

    syntax = 'Markdown'
    cmd = (_node, _js)
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = (r'.+?:\s'
             r'(?P<line>\d+):\s'
             r'(?P<error>MD\d+)\s'
             r'(?P<message>.+)')
    multiline = False
    line_col_base = (0, 1)
    tempfile_suffix = 'md'
    error_stream = util.STREAM_STDERR
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'
    config_file = ('--config', '.markdownlintrc', '~')
