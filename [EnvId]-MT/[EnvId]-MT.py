
import json 
import argparse
import kubernetes.client
from kubernetes import client, config
 
PLUGIN_VERSION = 1 ###Mandatory -If any changes in the plugin metrics, increment the version number.    
HEARTBEAT="true"  ###Mandatory -Set this to true to receive alerts when there is no data from the plugin within the poll interval
#METRIC_UNITS = { "CPU":"%","Memory":"%"} ###OPTIONAL - The unit defined here will be displayed in the Dashboard.

KUBE_CONFIG_PATH = "R:/DEV/ifsroot/config/kube/config"      #Edit this value with the kube config file path in ifsroot

class Plugin():
    def __init__(self):
        self.data = {}
        self.data["plugin_version"]  = PLUGIN_VERSION
        self.data["heartbeat_required"]  = HEARTBEAT
        self.data["Pods not running"] = 0
        self.data["Containers not ready"] = 0
        #self.data["units"] = METRIC_UNITS   ###Comment this line, if you haven't defined METRIC_UNITS
        
    def getData(self):  ### The getData method contains Sample data. User can enhance the code to fetch Original data
        try: ##set the data object based on the requirement
            
            config.load_kube_config(KUBE_CONFIG_PATH)  

            v1 = kubernetes.client.CoreV1Api()
            #print("Listing pods with their IPs:")
            ret = v1.list_pod_for_all_namespaces(watch=False)
            for i in ret.items:
                #print(i.status.container_statuses)
                for j in i.status.container_statuses:
                    if j.ready is False:
                        if j.name == 'ifs-db-init':
                            continue
                        #print(j.ready)
                        self.data["Containers not ready"] += 1
                if (i.status.phase != 'Running') :
                    if (i.status.phase =='Succeeded'):
                        continue
                    print(i.status.phase)
                    self.data["Pods not running"] += 1 

                #print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        except Exception as e:
            self.data['status']=0    ###OPTIONAL-In case of any errors,Set 'status'=0 to mark the plugin as down.
            self.data['msg'] = str(e)  ###OPTIONAL- Set the custom message to be displayed in the "Errors" field of Log Report
        return self.data
      
if __name__ == '__main__':
    plugin = Plugin()
    data = plugin.getData()
    parser = argparse.ArgumentParser()
    parser.add_argument("param", nargs='?', default="dummy")
    args = parser.parse_args()
    print(json.dumps(data, indent=4, sort_keys=True))  ###Print the output in JSON format