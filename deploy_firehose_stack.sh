#!/bin/bash

# Comprimir el archivo Lambda
zip index.zip index.py

# Obtener el ID de la cuenta AWS
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

# Crear bucket S3 para el código Lambda
aws s3 mb s3://aws-firehose-lambda-code-$ACCOUNT_ID

# Subir el archivo comprimido a S3
aws s3 cp index.zip s3://aws-firehose-lambda-code-$ACCOUNT_ID/

# Crear el stack CloudFormation
aws cloudformation deploy \
  --template-file Firehose.yaml \
  --stack-name StackWorkshopFirehose \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides pNameBucket=aws-firehose
