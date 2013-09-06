from fabric.api import env
from fabric.operations import run, sudo
from fabric.context_managers import cd, hide

env.roledefs = {
    "production": ["ec2-54-200-2-174.us-west-2.compute.amazonaws.com"],
}
env.user = "ec2-user"
env.key_filename = ["hashtime.pem",]
env.roles = ["production"]

def deploy():
    with cd('/var/www/html'):
        run('git pull --rebase origin master')