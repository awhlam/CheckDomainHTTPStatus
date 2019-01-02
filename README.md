# Check Domain HTTP Status
A Python script using the Requests and Pandas packages to check the HTTP status of an input spreadsheet of domain names.
[Reference of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

## Version History
* 07/30/18 - Version 1.0 - Initial release

## What it Does

1. Loads input file
2. Loops through column named "Domains"
3. Sends HTTP request to get header
4. Writes domain and HTTP status into csv file named "domains_status.csv"

## License
[MIT License](https://opensource.org/licenses/MIT)
