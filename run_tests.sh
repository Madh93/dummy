#!/bin/bash

case $1 in
    --unit)
        PYTHONPATH=$PYTHONPATH:./ pytest --cov=yadummy --disable-warnings ${CI_ARGS}
        ;;
    *)
        ;;
 esac
