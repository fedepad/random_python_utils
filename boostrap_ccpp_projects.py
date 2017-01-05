#!/usr/bin/env python

__author__ = 'Federico G. Padua'

import os
import shutil
import subprocess


# add possibility for the project dir to be a git directory: remote....as
# add COPYRIGHT file
# add LICENSE file


def build_root_proj_dir(root_dir_name):
    """
    @build_root_proj_dir Create a directory
    @root_dir_name Project directory name

    """
    try:
        os.makedirs(root_dir_name)
    except OSError:
        if not os.path.isdir(root_dir_name):
            raise


def copy_files(src, dst):
    """
    @copy_files just copy file from src to dst
    @src file to be copied/origin
    @dst destination file


    """
    #shutil.copyfile(src, dst)
    # fix copy to copyfiles because the check is on dst and it's a dir, not a file....!!!!
    try:
        with open(dst) as f: print("file %s exists..." % dst)
    except IOError as e:
        print("Error: %s not found." % dst)
        print("Creating %s file..." % dst)
        shutil.copyfile(src, dst)


if __name__ == "__main__":

    dirs_to_build = ['src', 'lib', 'bin', 'include', 'tests', 'doc']
    #makefile_dir = '/Users/Federico/.vim/bundle/c-support/codesnippets'
    #makefile_one = 'Makefile'
    #makefile_more = 'Makefile.multi-target.template'

    #makefile_single = os.path.join(makefile_dir, makefile_one)
    #makefile_multi = os.path.join(makefile_dir, makefile_more)

    print("Creating folders for C/C++ project...")
    cwd = os.getcwd()
    print("CWD is %s" % cwd)
    project_name = raw_input("Please type the name of your project: ")

    print("Project name will be: %s" % project_name)
    project_name_dir = os.path.join(os.path.abspath(cwd), project_name)
    print("Project path is %s" % project_name_dir)
    build_root_proj_dir(project_name_dir)

    readme_file = os.path.join(project_name_dir, 'README')


    ### src/ dir
    print("Now constructing subdirs inside %s" % project_name_dir)
    #for directory in dirs_to_build:
    #print("Now constructing %s dir inside %s" % (directory, project_name_dir))

    for h in dirs_to_build:
        build_root_proj_dir(os.path.join(project_name_dir, h))



    print("Checking if a build directory exists...")
    if os.path.isdir(os.path.join(project_name_dir, 'build')):
        print("Build directory exists, pass...")
    else:
        print("Build dir doesn't exists!")

        build_yn = raw_input("Do you want to create a build directory right now? yes[y]/no[n] ")
        if build_yn == "yes" or build_yn == "y":
            build_dir = os.path.join(project_name_dir, 'build')
            build_root_proj_dir(build_dir)
        elif build_yn == "no" or build_yn == "n":
            print("No build dir will be created, exiting...")

    #print("Copying Makefiles templates into project dir...")
    #copy_files(makefile_single, os.path.join(project_name_dir, makefile_one))
    #copy_files(makefile_multi, os.path.join(project_name_dir, makefile_more))
    print("Checking if a README file exists, eventually creating an empty one...")
    #os.system("touch README")
    try:
        with open(readme_file) as f:
            print("README file exists...")
    except IOError as e:
        print("Error: %s not found." % readme_file)
        print("Creating an empty README file...please update it!")
        create_readme = subprocess.Popen(['touch', readme_file])
        create_readme.wait()

    print("Main project directory tree created...now extra stuff...")
    git_local_yn = raw_input("Do you want to create a local GIT repository for this project? yes[y]/no[n] ")
    if git_local_yn == "yes" or git_local_yn == "y":

        os.system('git init %s' % project_name_dir)
        print("Local GIT repository initialized...")
        print("")

    elif git_local_yn == "no" or git_local_yn == "n":
        print("No local GIT repository created...")
    print("*******************************************")
    print("*                                         *")
    print("*  Please remember to add a remote git    *")
    print("*  origin for the project for backup      *")
    print("*  if initialized a local git repository  *")
    print("*                                         *")
    print("*******************************************")
    print(" ")
    print("Now you are ready to start coding!!!")

