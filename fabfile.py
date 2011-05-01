from __future__ import with_statement

from fabric.api import cd, env, local, run, sudo

def staging():
    env.hosts = ['staging.plone.org']
    env.shell = '/bin/sh -c'
    env.sudo_prefix = "sudo -S -p '%s' -H "
    env.code_root = '/srv/staging.plone.org'
    env.code_user = 'zope'

def ls():
    with cd(env.code_root):
        run('ls')

def update():
    with cd(env.code_root):
        sudo('nice svn up', user=env.code_user)

def rebuild():
    with cd(env.code_root):
        sudo('nice bin/buildout -c buildout-staging.cfg', user=env.code_user)

def restart():
    with cd(env.code_root):
        sudo('nice bin/supervisorctl reload', user=env.code_user)

def start():
    with cd(env.code_root):
        sudo('nice bin/supervisord', user=env.code_user)
        
def stop():
    with cd(env.code_root):
        sudo('nice bin/supervisorctl shutdown', user=env.code_user)

def deploy():
    update()
    rebuild()
    restart()
