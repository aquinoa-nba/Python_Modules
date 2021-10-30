#!/bin/sh

rm -rf local_lib intsall_python_py.log
pip3 -V
pip3 install -t local_lib git+https://github.com/jaraco/path.git --log intsall_python_py.log
python3 my_program.py
