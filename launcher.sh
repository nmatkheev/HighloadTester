#!/usr/bin/env bash

# launcher.sh $1
# $1 -- number of backend nodes

echo "Starting $1 backend containers"
for (( c = 0; c < ${1}; c++ )); do
   let port=9000+$c
   docker run --name="backend${c}" -v ./hostdata:/hostdata -p 127.0.0.1:${port}:${port} -w="/backend/" -itd backend:latest python3 backend.py 0.0.0.0 ${port} ${c}
done

echo "Starting frontend container"
docker run --name="frontend0" -v ./hostdata:/hostdata -p 127.0.0.1:8000:8000 -w="/frontend/" -itd frontend:latest python3 frontend.py 0.0.0.0 8000 0

echo "Starting client container"
docker run --name="client" -v ./hostdata:/hostdata -w="/client/" -itd frontend:latest python3 client.py 127.0.0.1:8000