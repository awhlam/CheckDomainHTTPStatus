# Check HTTP status code of domains names in Excel file

import requests
import pandas as pd

# Import domains column of Excel file to list
df = pd.read_excel('Domain_View_Review_20180730.xlsx', sheet_name=0)
domains_list = df['Domain_Name'].tolist()

# Convert domains in list to strings
domains_list_string = [str(domain) for domain in domains_list]

# Add http:// in front of domain if it isn't already
domains_list_string_http = []

for domain in domains_list_string:
    domains_http = domain
    if domain[:7] != 'http://':
        domains_http = 'http://' + domain
    domains_list_string_http.append(domains_http)

# Loop through domains list and check HTTP status code
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
domains_statuses = {}
    
for idx, domain in enumerate(domains_list_string_http):
    print(idx)
    try:
        request = requests.head(domain)
    except:
        domains_statuses[domain] = 'Error'
    else:
        domains_statuses[domain] = request.status_code

# Save dictionary to Pandas dataframe
df_domains = pd.DataFrame(list(domains_statuses.items()), columns=['Domain', 'Status'])

# Write Pandas dataframe to CSV
df_domains.to_csv('domain_statuses.csv', sep=',')