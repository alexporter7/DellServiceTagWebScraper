#===============================================================================
#                                   DSTWS.py
#===============================================================================
# Gets Service tag info
# Currently used to see if aio is contained in computer name
# Can be configured to use anything
#===============================================================================
#                           Author: Alex Porter
#===============================================================================

import requests
import re
import datetime
import ServiceTagList

log = []
query_match = []

re_query = 'aio'
base_url = "http://www.dell.com/support/home/us/en/04/product-support/servicetag/@/research"

get_warranty = False

def get_warranty(req):
    text = req.text
    #not done yet


try:
    tags = ServiceTagList.Tags
    print("[!] Successfully imported [" + str(len(tags)) + "] Service Tags")
except:
    print("[X] Could not import tags")

for t in tags:
    req = requests.get(base_url.replace('@', t))
    code = req.status_code
    if req.status_code != 200:
        print("[" + t + "] returned an error status code of [" + req.status_code + "]")
        log.append("[{}] returned an error status code of [{}]".format(t, req.status_code))
    else:
        if re.search(re_query, req.text):
            if get_warranty == True: #not done yet
                print("[!] [{}] matches query of [{}]".format(t, re_query))
                log.append("[{}] matches query of [{}]".format(t, re_query))
                warranty = get_warranty(req)
                query_match.append(t)
            else:
                print("[!] [{}] matches query of [{}]".format(t, re_query))
                log.append("[{}] matches query of [{}]".format(t, re_query))
                query_match.append(t)
        else:
            print("[!] [{}] does NOT query of [{}]".format(t, re_query))
            log.append("[{}] does NOT query of [{}]".format(t, re_query))


print("[!] There were [{}] matches to query of [{}]".format(len(query_match), re_query))
log.append("There were [{}] matches to query of [{}]".format(len(query_match), re_query))

f = open('log.txt', 'a')
f.write("\n---{}---\n\n".format(datetime.datetime.now()))
for line in log:
    f.write(line + "\n")

g = open('results.txt', 'w')
g.write("\n---{}---\n\n".format(datetime.datetime.now()))
for line in query_match:
    g.write("[{}] matches query [{}]\n".format(line, re_query))
