from time import sleep
import requests
from bs4 import BeautifulSoup
import re


payload1 = {'key1': 'value1', 'key2': 'value2'}
parameters = ['product owner']

# ,'product manager', 'business analyst']

job_keys = []
count = 0

for parameter in parameters:

    payload = {'q': parameter, 'l': 'remote'}
    url = "https://www.indeed.co.uk/jobs"
    r = requests.get(url, params=payload)
    results = re.findall(r"jobKeysWithInfo\['([0-9a-f]+)'\]", r.text)
    job_keys.extend(results)



for job_key in job_keys:

    url = 'https://www.indeed.co.uk/viewjob?jk=' + job_key
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    job_title = soup.find('h3')


    count += 1
    if count > 20:
        break

    sleep(0.5)

    print(job_title.text)
    print(url)
    # i also want to update db with this url












