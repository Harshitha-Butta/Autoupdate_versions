from git import Repo

repo=Repo('https:\\github.com\Harshitha-Butta\Autoupdate_versions\blob\main\versions_hyd_host2.json')

p=repo.remotes.origin

p.pull()
