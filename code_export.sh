#! /usr/bin/bash

rm ./code_export.txt 2> /dev/null;
find . -name "*.py" -type f -not -path "./venv/*" -exec cat {} > code_export.txt \;