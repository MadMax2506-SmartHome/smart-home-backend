#!/bin/bash

registry="192.168.178.150:8811"
repository="smart-home-backend"

docker image rm $repository
docker build -t $repository .

docker images --format "{{.Repository}}:{{.ID}}" | grep $repository | while read -r line ; do
    if [[ $line != *"$registry"* ]]; then
      image_id=$(echo $line | cut -d ":" -f 2)
      docker tag "$image_id" $registry/$repository
      docker image push $registry/$repository
    fi
done

