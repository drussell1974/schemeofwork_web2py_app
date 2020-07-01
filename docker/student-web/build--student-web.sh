#!/bin/bash

# install dependencies

cd build
yarn install

# run web server

yarn start --host $STUDENT_WEB__WEB_SERVER_IP --disable-host-check 

