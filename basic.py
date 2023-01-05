import git
#from git import Repo
import json

#from git import repo
from git import Repo

g = git.cmd.Git('https:\\github.com\Harshitha-Butta\Autoupdate_versions')
g.pull()


def add_version(data, filename='versions_hyd_host2.json'):
    with open(filename,'w') as f:
        json.dump(data, f,indent=4)
        

#version=input()
version = '21.9.0.42'
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

#repo=Repo('https:\\github.com\Harshitha-Butta\Autoupdate_versions\')

g.add('--all')
g.commit('-m', 'commit message from python script', author='harshitha.butta@gmail.com')
origin = repo.remote(name="origin")
origin.push()