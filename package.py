# -*- coding: utf-8 -*-

name = 's3cmd'

version = "2.1.0"

description = ''

authors = ['Michal Ludvig']

tools = []

requires = [
    'python', 'python_dateutil',
]

build_command = "python {root}/rezbuild.py {install}"


def commands():
    env.PYTHONPATH.append("{root}")
    env.PATH.append("{root}")


format_version = 2
