import git
import json
from git import Repo
import os

g = git.cmd.Git('https:\\github.com\\Harshitha-Butta\\Autoupdate_versions')
g.pull()

from git import Git
g1=Git()

g.checkout('cfc-hb')
g.pull()


def add_version(data, filename='versions_hyd_host2.json'):
    with open(filename,'w') as f:
        json.dump(data, f,indent=4)
        

#version=input()
version = '21.9.0.49'
#version=os.environ['version']

with open('versions_hyd_host2.json') as f:
    data=json.load(f)
    data['configuration']['cfc_versions'][version]=True
    data['configuration']['standalone_latest_general_release']=version
    data['configuration']['standalone_latest_controlled_release']=version
    data['configuration']['hosted_installers_latest']=version
    data['configuration']['aem_host_last_version']=version
    f.seek(0)

add_version(data)

repo=Repo(r'C:\git practice\checkout_branch\Autoupdate_versions')

repo.add('--all')
repo.commit('-m', 'commit message from python script', author='harshitha.butta@gmail.com')
origin = repo.remote(name="origin")
origin.push()
g.checkout('main')

master = repo.branches['main']
current = repo.branches['cfc-hb']
root = repo.merge_base(current, master)
repo.index.merge_tree(master, base=root)
repo.index.commit('merging current into master branch', parent_commits=(current.commit, master.commit))
