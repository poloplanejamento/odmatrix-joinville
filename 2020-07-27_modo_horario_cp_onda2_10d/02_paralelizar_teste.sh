#!/bin/bash
find . -iname "*fchk*py" -type f | xargs -t -r -P 10 -I FILE python3 ./FILE
