from cloudant import Cloudant
from cloudant.document import Document
import os
import json
from dateutil import parser
import numpy as np

stats_db_name = 'statsdbohiodev'

client = None
statsdb = None

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        statsdb = client.create_database(stats_db_name, throw_on_exists=False)
elif os.path.isfile('D:/dash/vcap-local.json'):
    with open('D:/dash/vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        statsdb = client.create_database(stats_db_name, throw_on_exists=False)
else:
    print('error')
        

def get_stats():
    statlist = list(map(lambda x: x['doc'], statsdb.all_docs(include_docs=True)['rows']))
    statsorted = sorted(list(map(lambda doc: {'count':str(doc['count']),'sa':str(doc['sucess_all']), 'ss':str(doc['sucess_subcategory']), 'sc':str(doc['sucess_category']), 'su':str(doc['sucess_u_type']), 'sn':str(doc['sucess_normal']), 'sp':str(doc['sucess_priority']), 'so':str(doc['sucess_others']),  'date':doc['date'], 'label':str(parser.parse(doc['date'])).split(' ')[0]}, statlist)), key=lambda k: k['label'])
    return(statsorted)