#!/bin/sh

exec pipx run --spec git+https://github.com/pomdtr/sunbeam-libraries.git sunbeam-librairies "$@"
