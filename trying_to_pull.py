from git import Repo

repo=Repo('versions_hyd_host2.json')

p=repo.remotes.origin

p.pull()