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


#test create
create = {
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

#test update
update = {
  "type": "update",
  "requestId": "e47f8835-b36b-4643-9d3c-bb52b753ffbf",
  "widgetId": "5c94f104-a9b3-4fed-a039-2cc4c631d042",
  "owner": "John Jones",
  "description": "GEDOQ",
  "otherAttributes": [
    {
      "name": "color",
      "value": "pink"
    },
    {
      "name": "size-unit",
      "value": "cm"
    },
    {
      "name": "height-unit",
      "value": "cm"
    },
    {
      "name": "width-unit",
      "value": "cm"
    },
    {
      "name": "length",
      "value": "540"
    },
    {
      "name": "rating",
      "value": "3.8907907"
    },
    {
      "name": "price",
      "value": "42.27"
    },
    {
      "name": "quantity",
      "value": "72"
    },
    {
      "name": "vendor",
      "value": "RTPRZNV"
    }
  ]
}

#test delete
delete = {
  "type": "delete",
  "requestId": "4509d06d-9d32-464a-a015-48495771c433",
  "widgetId": "5c94f104-a9b3-4fed-a039-2cc4c631d042",
  "owner": "John Jones"
}

lambda_handler(create,0)