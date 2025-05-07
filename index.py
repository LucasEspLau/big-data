import json
import boto3

# Inicializa el cliente de Kinesis Firehose
firehose = boto3.client('firehose', region_name='us-east-1')  # Asegúrate de poner la región correcta

def lambda_handler(event, context):
    # Recuperar el cuerpo del evento POST
    body = json.loads(event['body'])
    
    # Procesar los datos del sensor (por ejemplo, tomar valores de 'body')
    sensor_data = json.dumps(body)  # Este es el dato que enviarás a Firehose

    # Enviar datos a Kinesis Firehose
    response = firehose.put_record(
        DeliveryStreamName='StreamSensorIoT',
        Record={'Data': sensor_data}
    )
    
    # Responder al API Gateway con éxito
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Data received and sent to Firehose', 'response': response})
    }
