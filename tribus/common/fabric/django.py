#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013-2014 Tribus Developers
#
# This file is part of Tribus.
#
# Tribus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tribus is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from contextlib import nested
from fabric.api import env, run, cd, shell_env, hide

from tribus.common.fabric.docker import docker_check_container


def django_syncdb():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('bash %(tribus_django_syncdb_script)s' % env)


def django_runserver():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('bash %(tribus_django_runserver_script)s' % env)


def django_shell():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('python manage.py shell')


def celery_purge_tasks():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('python manage.py celery purge')


def haystack_rebuild_index():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('python manage.py rebuild_index')


def get_selected():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('python manage.py get_selected')


def install_repository():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('python manage.py install_repository')


def get_sample_packages():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('python manage.py get_sample_packages')


def select_sample_packages():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('python manage.py select_sample_packages')


def index_selected():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('python manage.py index_selected')


def index_sample_packages():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('python manage.py index_sample_packages')


def wipe_repo():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('python manage.py wipe_repo')


def filldb_from_remote():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('python manage.py filldb_from_remote')


def filldb_from_local():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('python manage.py filldb_from_local')


def create_cache_from_remote():
    """
    """

    docker_check_container()

    with nested(hide('warnings', 'stderr', 'running'),
                shell_env(**env.fvars), cd(env.basedir)):
        run('python manage.py create_cache_from_remote')
