from pymongo import MongoClient
from lib import connect, find_key
import ssl

# Create empty string to store text
strs_functionality = ""
strs_body = ""
strs_other = ""

# Connect to database
client = MongoClient(connect(), 27017,ssl_cert_reqs=ssl.CERT_NONE)
db_out = client['FYP_result']
col_out_functionality = db_out['FYP_2021_result_functionality']
col_out_body = db_out['FYP_2021_result_body']
col_out_other = db_out['FYP_2021_result_other']

# Add comments to the string
for x in col_out_functionality.find({}, {"_id": 0}):
    str1 = x.get("body")
    strs_functionality = strs_functionality + str1

for x in col_out_body.find({}, {"_id": 0}):
    str2 = x.get("body")
    strs_body = strs_body + str2

for x in col_out_other.find({}, {"_id": 0}):
    str3 = x.get("body")
    strs_other = strs_other + str3

# Find keywords in the collections
print("Functionality:")
print(find_key(strs_functionality), "\n")
print("Body:")
print(find_key(strs_body), "\n")
print("Other:")
print(find_key(strs_other), "\n")

