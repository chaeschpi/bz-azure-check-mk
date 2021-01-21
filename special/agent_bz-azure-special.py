

import argparse 
import requests
import json


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    required_param_group = arg_parser.add_argument_group('required arguments') 
    required_param_group.add_argument('-k', '--key', required=True, help="Azure Function Key")
    required_param_group.add_argument('-s', '--subscription', required=True, help='')
    args = arg_parser.parse_args()

query = '?code=' + args.key + '&subscriptionId='+ args.subscription 
print(query)
r = requests.get('https://bzmonitorapi-prd.azurewebsites.net/api/Function1'+ query )



if r.status_code == 200:
    json = json.loads(r.text)
    print(json); 
else: 
    print("Request Error "+r.reason)