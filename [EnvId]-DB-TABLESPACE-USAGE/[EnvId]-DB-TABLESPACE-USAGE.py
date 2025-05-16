"""

Site24x7 Oracle DB Plugin

"""

import json


# if any impacting changes to this plugin kindly increment the plugin version here.
PLUGIN_VERSION = "1"

# Setting this to true will alert you when there is a communication
# problem while posting plugin data to server
HEARTBEAT = "true"

# Config Section: Enter your configuration details to connect to the oracle database
ORACLE_HOST = "localhost"

ORACLE_PORT = "1521"

ORACLE_SID = "<DB_ALIAS>"

ORACLE_USERNAME = "SYSTEM"

ORACLE_PASSWORD = "<Password>"

TABLESPACE_NAME = ["SYSTEM","USERS","SYSAUX", "TEMP"]  ####Edit this field and add the names of the tablespaces to be monitored. Names are separated by comma

# Mention the units of your metrics . If any new metrics are added, make an entry here for its unit if needed.
METRICS_UNITS = {'usage': '%'}


class Oracle(object):
    def __init__(self, config):
        self.configurations = config
        self.connection = None
        self.host = self.configurations.get('host', 'localhost')
        self.port = int(self.configurations.get('port', '1521'))
        self.sid = self.configurations.get('sid', 'XE')
        self.username = self.configurations.get('user', 'sys')
        self.password = self.configurations.get('password', 'admin')
        self.data = {'plugin_version': PLUGIN_VERSION, 'heartbeat_required': HEARTBEAT}
        units ={}
        for name in TABLESPACE_NAME:
            units[name+'_usage'] = METRICS_UNITS['usage']
            self.data['units']=units

    def metricCollector(self):
        c=None
        conn=None
        try:
            import oracledb
        except Exception as e:
            self.data['status'] = 0
            self.data['msg'] = str(e)
            return self.data

        try:
            #dsnStr = oracledb.makedsn(self.host, self.port, self.sid)
            conn = oracledb.connect(user=self.username,password=self.password,dsn=self.host+':'+str(self.port)+'/'+self.sid)
            c = conn.cursor()
            
            c=c.execute("SELECT tablespace_name, round(used_percent,0) FROM dba_tablespace_usage_metrics")

	    
            for row in c:
                name, usage= row
                if name in TABLESPACE_NAME:
                    self.data[name+'_usage'] = usage

        except Exception as e:
            self.data['msg'] = str(e)
        finally:
            if c!= None : c.close()
            if conn != None : conn.close()
            return self.data

           
if __name__ == "__main__":
    configurations = {'host': ORACLE_HOST, 'port': ORACLE_PORT,
                      'user': ORACLE_USERNAME, 'password': ORACLE_PASSWORD, 'sid': ORACLE_SID}

    oracle_plugin = Oracle(configurations)

    result = oracle_plugin.metricCollector()

print(json.dumps(result, indent=4, sort_keys=True))
