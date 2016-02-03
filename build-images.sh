#!/bin/bash

echo "Working catalog is: `pwd`"
echo "I will build One frontend container, and One backend container"
echo "Stop me in 3 seconds if needed..."
sleep 3


cd DockFront
echo "######################################################################################"
echo "#                           Building frontend container                               "
echo "######################################################################################"
docker build --no-cache -t frontend -f Dockerfile ..
#docker run -t -i mephidude/frontend:v1 /bin/bash


cd ../DockBack/

echo "######################################################################################"
echo "#                           Building backend container                                "
echo "######################################################################################"

docker build --no-cache -t backend -f Dockerfile ..

#echo "Building $1 backend containers"
#for (( c = 0; c <= ${1}; c++ )); do
#   docker build -t backend${c} -f Dockerfile ..
#done

