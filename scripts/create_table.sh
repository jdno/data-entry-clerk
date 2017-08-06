#!/usr/bin/env bash

tables=$(aws dynamodb list-tables --endpoint-url http://localhost:8000)

if ! echo "$tables" | grep "automatiqa-dec"
then
    aws dynamodb create-table \
    --endpoint-url "http://localhost:8000" \
    --attribute-definitions "AttributeName=dec_id,AttributeType=S" \
    --table-name "automatiqa-dec" \
    --key-schema "AttributeName=dec_id,KeyType=HASH" \
    --provisioned-throughput "ReadCapacityUnits=1,WriteCapacityUnits=1"
fi
