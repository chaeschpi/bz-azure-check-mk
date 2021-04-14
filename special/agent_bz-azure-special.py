import argparse 
import requests
import json
######## variables declaration ###################
args= "null"
r = "null" 
baseurl = 'https://bzmonitorapi-prd.azurewebsites.net/api/Function1'
Query = "null"
####### function declaration ####################

def process_json_response(text):
    _json = json.loads(text)

    for k ,v  in _json.items():
        print (f"<<<{k}>>>")
        print(v)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    required_param_group = arg_parser.add_argument_group('required arguments') 
    required_param_group.add_argument('-k', '--key', required=True, help="Azure Function Key")
    required_param_group.add_argument('-s', '--subscription', required=True, help='Azure Subscription Id')
    args = arg_parser.parse_args()
    query = '?code=' + args.key + '&subscriptionId='+ args.subscription 
try:
    r = requests.get(baseurl+ query )
except():
    print("Request not possible")

if r.status_code == 200:
   process_json_response(r.text)
else: 
    print("Request Error "+r.reason)



