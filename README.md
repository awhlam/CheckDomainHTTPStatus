# CheckDomainHTTPStatus
Python script to check the HTTP status of an input spreadsheet of domain names

A Python script using the Requests and Pandas packages to check the HTTP status of an input spreadsheet of domain names.

## Details

07/30/18 - Version 1.0 - Initial release

## What it Does

1. Loads input file
2. Loops through column named "Domains"
3. Sends HTTP request to get header
4. Writes domain and HTTP status into csv file named "domains_status.csv"