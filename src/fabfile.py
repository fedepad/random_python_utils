from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
import platform
#import socket
#socket.gethostname()


#env.hosts=["argon", "kalium", "boron", "neon", "lithium", "chlorine"]
env.hosts=[platform.node()]
#env.user="root"


def hello():
    print("Executing on %(host)s as %(user)s" % env)
    print("Hello world!")


def identify_host():
    print("Executing on %(host)s as %(user)s" % env)
    host = platform.node()
    print(host)


# def pull_code_fromrepo(cmd):
#     print("Executing on %(host)s as %(user)s" % env)
#     cmd = 'git'
#     run(cmd)
#
#
# def build_repo(cmd):
#     print("Executing on %(host)s as %(user)s" % env)
#     run(cmd)
#
#
# def run_test(cmd):
#     print("Executing on %(host)s as %(user)s" % env)
#     local(cmd)
#
#
# @parallel
# def run_bkg(cmd):
#     print("Executing on %(host)s as %(user)s" % env)
#     run(cmd)
#
#
# def generate_results_summary(cmd):
#     print("Executing on %(host)s as %(user)s" % env)
#     run(cmd)
#
#
# def create_plots(cmd):
#     print("Executing on %(host)s as %(user)s" % env)
#     run(cmd)

# connect to hosts
# git pull on different hosts
# build the repo
# launch exec on one host
# launch exec on multiple hosts, parallel
# generate results/summary
# get results and put together
# script analysis data
# script plots, needs to read in directly from summary files
# create plots and save in specified directories (best name passed via command line)




