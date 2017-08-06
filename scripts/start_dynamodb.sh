#!/usr/bin/env bash

current_dir="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"

cd "$current_dir"/../dynamodb
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
