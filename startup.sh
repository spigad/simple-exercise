#!/usr/bin/env bash

export ENVIRONMENT=${ENVIRONMENT:-'production'}

python ./app.py ${PORT}
