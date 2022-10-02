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

# https://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


_node = 'node' if os.name=='nt' else 'node' if which('node') else 'nodejs'
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
