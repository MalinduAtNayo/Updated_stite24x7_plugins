=======================================================================================
=
= Nayo Managed Services - Site24x7 Monitoring Plugins for IFS Environments
=
= Nayo Managed Services provides plugins to monitor an IFS Environment Database and MWS
= using ManageEngine's Site24x7 product.
=
=
= NOTE:    This tool is meant to support a device running a Microsoft Windows Operating System.
=
=========================================================================================

=== PREREQUISITES ===
*  ManageEngine Site24x7 Monitor must be installed on the target machine to run these monitoring items.

*  Python must be installed on the server where the Site24x7 monitor is installed.
If not already installed, you can install it at <repos>\_sw\Python

NOTE:  You will need to log out and back into your windows session for the path information to be updated.

*  Make sure the file <ReposHome>\_sw\Python\UpdatePythonComponentsForNayoMonitoring.cmd was run prior to implementing the below.

=== DB STEPS ===
To install DB monitoring for an environment, follow these steps...

1. Copy the folder "[EnvId]-DB" and rename it to the correct value of the enviornment id with the -DB.
Example: "IFSPROD-DB"

2. Within your newly renamed folder, rename the file [EnvId]-DB.py and change the [EnvId] part to the correct Environment Id that matches the target enviornment.
Example IFSPROD-DB.py

3. Edit the .py file you just renamed and change the following variables.  Set the values in "" to what they should properly be for the target database, and save the file.
ORACLE_PORT = "1521"
ORACLE_SID = "<DB_ALIAS>"
ORACLE_USERNAME = "system"
ORACLE_PASSWORD = "<Password>"
RMAN_BACKUP_SCHEDULE = "09:30" 
IS_PROD = False

Example:
ORACLE_PORT = "1521"
ORACLE_SID = "IFSPROD"
ORACLE_USERNAME = "system"
ORACLE_PASSWORD = "manager"
RMAN_BACKUP_SCHEDULE = "22:30" 
IS_PROD = True


4.  Copy the renamed folder from step 1 to "C:\Program Files (x86)\Site24x7\WinAgent\monitoring\Plugins".

If done properly, in about 6 minutes you should see the monitoring item in the Site24x7 portal and it collecting information.
Make sure to associate the monitoring item with the correct Monitor group, etc. for the Customer/Monitor Group.



=== DB TABLESPACE STEPS ===
To install DB TABLESPACE monitoring for an environment, follow these steps...

1. Copy the folder "[EnvId]-DB-TABLESPACE" and rename it to the correct value of the enviornment id with the -DB.
Example: "IFSPROD-DB-TABLESPACE"

2. Within your newly renamed folder, rename the file [EnvId]-DB-TABLESPACE.py and change the [EnvId] part to the correct Environment Id that matches the target enviornment.
Example IFSPROD-DB-TABLESPACE.py

3. Edit the .py file you just renamed and change the following variables.  Set the values in "" to what they should properly be for the target database, and save the file.
ORACLE_PORT = "1521"
ORACLE_SID = "<DB_ALIAS>"
ORACLE_USERNAME = "system"
ORACLE_PASSWORD = "<Password>"
TABLESPACE_NAME = ["SYSTEM","USERS","SYSAUX"]

Example:
ORACLE_PORT = "1521"
ORACLE_SID = "IFSPROD"
ORACLE_USERNAME = "system"
ORACLE_PASSWORD = "manager"
TABLESPACE_NAME = ["IFSAPP_DATA","IFSAPP_LOB"]


4.  Copy the renamed folder from step 1 to "C:\Program Files (x86)\Site24x7\WinAgent\monitoring\Plugins".

If done properly, in about 6 minutes you should see the monitoring item in the Site24x7 portal and it collecting information.
Make sure to associate the monitoring item with the correct Monitor group, etc. for the Customer/Monitor Group.




=== MWS STEPS ===
To install MWS monitoring for an environment, follow these steps...

1. Copy the folder "[EnvId]-MWS" and rename it to the correct value of the enviornment id with the -MWS.
Example: "IFSPROD-MWS"

2. Within your newly renamed folder, rename the file [EnvId]-MWS.py and change the [EnvId] part to the correct Environment Id that matches the target enviornment.
Example IFSPROD-MWS.py

3. Edit the .py file you just renamed and change the following variables.  Set the values in "" to what they should properly be for the target database, and save the file.
WEBLOGIC_PORT = "<MWS Admin port xx090>"
WEBLOGIC_USERNAME = "ifs"
WEBLOGIC_PASSWORD = "internal123"

Example:
WEBLOGIC_PORT = "48090"
WEBLOGIC_USERNAME = "ifs"
WEBLOGIC_PASSWORD = "internal123"

NOTE:  Leave the following variable and value as-is, WEBLOGIC_HOST = "localhost"


4.  Copy the renamed folder from step 1 to "C:\Program Files (x86)\Site24x7\WinAgent\monitoring\Plugins" on the server device hosting the IFS MWS instance and where the Site24x7 Monitor is installed.

If done properly, in about 6 minutes you should see the monitoring item in the Site24x7 portal and it collecting information.
Make sure to associate the monitoring item with the correct Monitor group, etc. for the Customer/Monitor Group.



=== MT STEPS ===
To install MT monitoring for an environment, follow these steps...

1. Copy the folder "[EnvId]-MT" and rename it to the correct value of the enviornment id with the -MT.
Example: "IFSPROD-MT"

2. Within your newly renamed folder, rename the file [EnvId]-MT.py and change the [EnvId] part to the correct Environment Id that matches the target enviornment.
Example IFSPROD-MT.py

3. Edit the .py file you just renamed and change the following variables.  Set the values in "" to what they should properly be for the target database, and save the file.

You may have to copy the kube config file over to the server running the plugin.

KUBE_CONFIG_PATH = "R:/DEV/ifsroot/config/kube/config" 



4.  Copy the renamed folder from step 1 to "C:\Program Files (x86)\Site24x7\WinAgent\monitoring\Plugins" on the IFS Cloud management server device and where the Site24x7 Monitor is installed.

If done properly, in about 6 minutes you should see the monitoring item in the Site24x7 portal and it collecting information.
Make sure to associate the monitoring item with the correct Monitor group, etc. for the Customer/Monitor Group.


=== SSL STEPS ===
To install MT monitoring for an environment, follow these steps...

1. Copy the folder "[EnvId]-SSL" and rename it to the correct value of the enviornment id with the -SSL.
Example: "IFSPROD-SSL"

2. Within your newly renamed folder, rename the file [EnvId]-SSL.py and change the [EnvId] part to the correct Environment Id that matches the target enviornment.
Example IFSPROD-SSL.py

3. Edit the .py file you just renamed and change the following variables.  Set the values in "" to what they should properly be for the target database, and save the file.

You may have to copy the kube config file over to the server running the plugin.

hostname = "PROD MWS/MT host"
sni = "URL of the PROD application"
hostport = 443

eg:

hostname = "fpapp01.bfusa.com"
sni = "ifs.bfusa.com"
hostport = 443


4.  Copy the renamed folder from step 1 to "C:\Program Files (x86)\Site24x7\WinAgent\monitoring\Plugins".

If done properly, in about 6 minutes you should see the monitoring item in the Site24x7 portal and it collecting information.
Make sure to associate the monitoring item with the correct Monitor group, etc. for the Customer/Monitor Group.



=== DR DB STEPS ===
To install DR DB monitoring for an environment, follow these steps...

1. Copy the folder "[EnvId]-DB-STBY" and rename it to the correct value of the enviornment id with the -DB-STBY.
Example: "IFSPROD-DB-STBY"

2. Within your newly renamed folder, rename the file [EnvId]-DB-STBY.py and change the [EnvId] part to the correct Environment Id that matches the target enviornment.
Example IFSPROD-DB-STBY.py

3. Edit the .py file you just renamed and change the following variables.  Set the values in "" to what they should properly be for the target database, and save the file.
ORACLE_HOST = "localhost"

ORACLE_PORT = "1521"
ORACLE_SID = "<DB_ALIAS>"
ORACLE_USERNAME = "system"
ORACLE_PASSWORD = "<Password>"
SOURCE_DB_HOST = "localhost"
SOURCE_DB_PORT = "1521"
SOURCE_DB_SID = "<DB_ALIAS>"
SOURCE_DB_USERNAME = "system"
SOURCE_DB_PASSWORD = "<Password>"


4.  Copy the renamed folder from step 1 to "C:\Program Files (x86)\Site24x7\WinAgent\monitoring\Plugins".

If done properly, in about 6 minutes you should see the monitoring item in the Site24x7 portal and it collecting information.
Make sure to associate the monitoring item with the correct Monitor group, etc. for the Customer/Monitor Group.

