# Delete Cloudflare Access Applications
A simple Python script for deleting Cloudflare access applications that may face the problem "There was an error deleting your application" by using the Cloudflare API instead of the default delete button. It allows for a more specific and informative deletion process.

## Installation
Make sure you have python and internet connection installed on your system. 

## Usage
1. Clone this project or download the script.py file. 
1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using the following command: python script.py
3. Enter the account email, account key and API key when prompted.
4. Enter the Application IDs one by one or "c" once you entered all application iDs to continue.
5. The script will process each Application ID and will display a success message or an error message for each deletion process.

## Dependencies
- Python 3
- http.client, json (part of python standard library)

## Note
- This script uses the Cloudflare API and requires a valid API key.
- This script requires internet connection to run
- Please be cautious while using this script as it will delete the application from your cloudflare account.
