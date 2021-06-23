import argparse 
import requests
import json
######## variables declaration ###################
args= "null"
r = "null" 
baseurl = 'https://bzmonitorapi-prd.azurewebsites.net/api/getStatus'
Query = "null"
####### function declaration ####################

def process_json_response(text):
    _json = json.loads(text)
    for k ,v  in _json.items():
        if (k == 'advisorRecommendationsSummary'): 
            advisorRecommendationsSummary(v)
        elif k == 'backupJobsSummary':
                backupjob(v)
        elif k == 'resourceHealthSummary': 
            healthSummary(v)
        elif (k == 'serviceHealthSummary'):
                serviceHealthSummary(v)



def advisorRecommendationsSummary(json): 
    summary = json.get('advisorSummary')
    print ('<<<az-bz_Advisor>>>')
    for k,v in summary.items():
        if k == 'totalItems':
            continue
        printstr = ''
        for e in v.values():
            printstr = printstr + str(e) + ' '
        print(k, printstr)
# advisor (high, mid, low, suppression)    

def backupjob(json): 
    summary = json.get('backupSummary')
    print ('<<<az-bz_Backup>>>')
    for k,v in summary.items():
        print('backup'+k,v)
    return 

def healthSummary(json): 
    summary = json.get('healthSummary')
    print ('<<<az-bz_Health>>>')
    for k,v in summary.items():
        print(k,v)

def serviceHealthSummary(json): 
    summary = json.get('serviceSummary')
    print ('<<<az-bz_Service>>>')
    for k,v in summary.items():
        print(k,v)
    

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

