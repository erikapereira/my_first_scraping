from time import sleep
import requests
from bs4 import BeautifulSoup
import re


parameters = ['manager', 'product owner']
limit = 10
job_keys = []
count = 0

# limit : number of results 10/20/30/50
# count : limiter on number of job_key urls


for parameter in parameters:

    for page in range (0, 40, limit):
        # range function! page number starts at 0 and increases by limit
        payload = {'q': parameter, 'limit': limit, 'start': page}
        url = "https://www.indeed.co.uk/jobs"
        r = requests.get(url, params=payload)
        results = re.findall(r"jobKeysWithInfo\['([0-9a-f]+)'\]", r.text)
        job_keys.extend(results)
        # extend adds to job_keys []
        print(job_keys)


for job_key in job_keys:

    url = 'https://www.indeed.co.uk/viewjob?jk=' + job_key
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    job_title = soup.find('h3')

    count += 1
    if count > 3:
        break
        # will only generate upto x urls & stop
    sleep(0.5)

    print(job_title.text)
    print(url)