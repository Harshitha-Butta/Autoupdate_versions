#import git
import json


repo=git.Repo('https://github.com/ncr-swt-hospitality/chef-cfc-databag')
p=repo.remotes.origin
p.pull()


def add_version(data, filename='versions_hyd_host2.json'):
    with open(filename,'w') as f:
        json.dump(data, f,indent=4)
        

version=input()
with open('versions_hyd_host2.json') as f:
    data=json.load(f)
    data['configuration']['cfc_versions'][version]=True
    data['configuration']['standalone_latest_general_release']=version
    data['configuration']['standalone_latest_controlled_release']=version
    data['configuration']['hosted_installers_latest']=version
    data['configuration']['aem_host_last_version']=version
    f.seek(0)
    #json.dump(data, f,indent=4)
    #f.truncate()

add_version(data)

