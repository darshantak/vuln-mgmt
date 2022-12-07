import requests

assetName=str(input())
url = "https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch="+assetName+"&keywordExactMatch"

payload={}
headers = {
  'x-api-key': 'e2d226a5-8c6d-4b94-b96f-e6694ab6de6d'
}

response = requests.request("GET", url, headers=headers, data=payload)
response_json = response.json()
totalVulns = len(response_json["vulnerabilities"])
cveArray= []
versionArray=[]
for i in range(totalVulns):
    key = list((response_json["vulnerabilities"][i]["cve"]["metrics"]).keys())
    # print(key)
    for j in key:
        cveArray.append(response_json["vulnerabilities"][i]["cve"]["metrics"][j])
        
for i in range(len(cveArray)):
    versionArray.append(cveArray[i][0]["cvssData"]["version"])
versionArray=set(versionArray)
print("Vulnerable versions are " , *versionArray)
# key=list((response_json["vulnerabilities"][-1]["cve"]["metrics"]).keys())
# print(cveArray[0][0]["cvssData"]["version"])


#from vulnerabilites array get the versions of the vulns versions and then process it.
#what if i can search for that particular version in nvd db might have to work around this.
#