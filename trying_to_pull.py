from git import Repo

repo=Repo('https://github.com/Harshitha-Butta/Autoupdate_versions')

p=repo.remotes.origin

p.pull()
