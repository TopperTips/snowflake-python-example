'''

Step-1: Create a project direcgtor
-------------------------
mkdir sf-python

Step-2:Create a requirement file (you can name it anything like pip_requirement.txt) inside the folder
-------------------------
snowflake-connector-python
pandas
Pyarrow


Step-3: Run following environment comments (you can have any name like sfenv  or my_env)
---------------------------
$python3 -m venv sfenv
$source sfenv/bin/activate
$pip install -r pip_requirements.txt


Step-4: Now run your python code with having sf code
----------------------------
$python example_02.py
'''

#import the snowflake connector
import snowflake.connector as sf
import pandas

#define snowflake connection parameters & default warehouse/db/schema/role details

sf_user='user01'                #user id
sf_password='1nputPa88w0rd'     #The password to access the account
sf_account='xy123456'           #example xy123456 or mycompany (https://mycompany.snowflakecomputing.com/)

#following parameters may come as default too if your user account 
# is setup with default configuration.

sf_role='sysadmin'    # sysadmin or myrole as per the access you have, your user might have default roles
sf_warehouse='test_wh', 
sf_database='util_db',
sf_schema='public'

print("User id :" + sf_user)
print("Password id :" + sf_password)
print("Account :" + sf_user)
print("Role :" + sf_role)
print("Warehouse :" + sf_warehouse)
print("Database :" + sf_database)
print("Schema :" + sf_schema)

#create the context file
ctx = sf.connect(
    user=sf_user,
    password=sf_password,
    account=sf_account,
    role=sf_role,
    warehouse=sf_warehouse,
    database=sf_database,
    schema=sf_schema
    )
cs = ctx.cursor()
print("----The cursor object-----")
print(cs)

try:
	cs.execute("select current_version(), current_region(), current_user")
	df = cs.fetch_pandas_all()
	df.info()
    for ind in df.index:
        print(ind)
finally:
	cs.close()
    print("successfully done...")

ctx.close()