"""from git import Repo

repo=Repo('https:\\github.com\Harshitha-Butta\Autoupdate_versions')

p=repo.remotes.origin"""
import git 

g = git.cmd.Git('https:\\github.com\Harshitha-Butta\Autoupdate_versions')
g.pull()
