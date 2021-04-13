import boto3
import json

def lambda_handler(event, context):
    url = 'https://sqs.us-east-1.amazonaws.com/912483513202/cs5260-requests'
    client = boto3.client('sqs')
    client.send_message(QueueUrl=url,MessageBody=json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Request added to queue')
    }


#test event
event = {
  "type": "create",
  "requestId": "e80fab52-71a5-4a76-8c4d-11b66b83ca2a",
  "widgetId": "8123f304-f23f-440b-a6d3-80e979fa4cd6",
  "owner": "Mary Matthews",
  "label": "JWJYY",
  "description": "THBRNVNQPYAWNHGRGUKIOWCKXIVNDLWOIQTADHVEVMUAJWDONEPUEAXDITDSHJTDLCMHHSESFXSDZJCBLGIKKPUYAWKQAQI",
  "otherAttributes": [
    {
      "name": "width-unit",
      "value": "cm"
    },
    {
      "name": "length-unit",
      "value": "cm"
    },
    {
      "name": "rating",
      "value": "2.580677"
    },
    {
      "name": "note",
      "value": "FEGYXHIJCTYNUMNMGZBEIDLKXYFNHFLVDYZRNWUDQAKQSVFLPRJTTXARVEIFDOLTUSWZZWVERNWPPOEYSUFAKKAPAGUALGXNDOVPNKQQKYWWOUHGOJWKAJGUXXBXLWAKJCIVPJYRMRWMHRUVBGVILZRMESQQJRBLXISNFCXGGUFZCLYAVLRFMJFLTBOTLKQRLWXALLBINWALJEMUVPNJWWRWLTRIBIDEARTCSLZEDLZRCJGSMKUOZQUWDGLIVILTCXLFIJIULXIFGRCANQPITKQYAKTPBUJAMGYLSXMLVIOROSBSXTTRULFYPDFJSFOMCUGDOZCKEUIUMKMMIRKUEOMVLYJNJQSMVNRTNGH"
    }
  ]
}

lambda_handler(event,0)