#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016, Configr Inc. <hello@configr.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# On Debian systems, you can find the full text of the license in
# /usr/share/common-licenses/GPL-2

from fabric.api import *
import time
import os


##
## available environments
##

def production():
    env.hosts = ['root@cloud419.configrapp.com']
    env.app_root = '/srv/clinicameitan.com.br/www/clinicameitan'
    env.git_origin = 'git@github.com:pazzamello/clinicameitan.git'
    env.git_branch = 'master'
    env.virtual = '/var/www/.virtualenvs/clinicameitan.com.br/bin/activate'
    env.manage = '/srv/clinicameitan.com.br/www/clinicameitan/manage.py'

def development():
    env.hosts = ['root@cloud419.configrapp.com']
    env.app_root = '/srv/dev.clinicameitan.com.br/www/clinicameitan'
    env.git_origin = 'git@github.com:pazzamello/clinicameitan.git'
    env.git_branch = 'master'
    env.virtual = '/var/www/.virtualenvs/dev.clinicameitan.com.br/bin/activate'
    env.manage = '/srv/dev.clinicameitan.com.br/www/clinicameitan/manage.py'



##
## available commands
##

def deploy():
    start = time.time()

    ## validate environment
    if not hasattr(env, 'app_root'):
        print 'ERROR: unknown environment.'
        os.sys.exit(1)

    ## clone repository
    command = 'test -d %s/.git || git clone %s %s -b %s'
    run(command % (env.app_root, env.git_origin, env.app_root, env.git_branch))

    ## update repository
    command = 'cd "%s" && git reset --hard && git pull && git checkout -B %s origin/%s && git pull'
    run(command % (env.app_root, env.git_branch, env.git_branch))


    final = time.time()
    puts('execution finished in %.2fs' % (final - start))

    ## update python package
    #print env.virtual
    command = 'source %s; cd %s; pip install -r requirements.txt' % (env.virtual, env.app_root)
    sudo(command, user='www-data')

    ## update static media
    command = 'source %s; python %s' % (env.virtual, env.manage)
    run(command + ' collectstatic --noinput')

    ## update database schema
    command = 'source %s; python %s' % (env.virtual, env.manage)
    run(command + ' migrate --noinput')

    ## restart uwsgi service
    run('find %s -name "*.pyc" -delete' % env.app_root)
    run('/etc/init.d/uwsgi reload dev.clinicameitan.com.br')


