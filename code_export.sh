#! /usr/bin/bash

rm ./code_export.txt
find . -name "*.py" -type f -not -path "./Lib/*" -not -path "./Scripts/*" -exec cat {} > code_export.txt \;