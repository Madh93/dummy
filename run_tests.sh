#!/bin/bash

case $1 in
    --unit)
        PYTHONPATH=$PYTHONPATH:./ pytest
        ;;
    *)
        ;;
 esac
