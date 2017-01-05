__author__ = 'Federico G. Padua'

import os
import subprocess
import argparse
import re


def argparse_of_program():
    parser = argparse.ArgumentParser(description='This script generates plots of different things', version='0.0')

    parser.add_argument('-i', '--input', help='directory or filename for which you want to determine on which device/vrtual-physical device lives on...', required=True)

    #parser.add_argument('-o','--output',help='Output plot name', required=True)
    args = parser.parse_args()
    return args


def determine_os():
    return os.uname()[0]

if __name__ == '__main__':
    #print("This program determines the physical device/s a directory lives on in Linux")
    arguments = argparse_of_program()
    directory_name = arguments.input
    df_subprocess = subprocess.Popen(['df', '%s' % directory_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = df_subprocess.communicate()[0]
    #print("%s" % output)
    print output
    print("NOW checking the lines in output")
    #for line in output:
    #    print line
    oper_system = determine_os()

    if oper_system == "Darwin":
        header = output.split("\n")[0].split()
        device, size, used, available, capacity, i, ii, iii, mountpoint = output.split("\n")[1].split()
    elif oper_system == "Linux":
        header = output.split("\n")[0].split()
        device, size, used, available, percent, mountpoint = output.split("\n")[1].split()

    print("%s" % oper_system)
    print("%s" % header)
    print("device: %s" % device)
    print("size (%s): %s" % (header[1], size))
    print("%s" % used)
    print("%s" % mountpoint)

    #matching_device_mapper = re.findall(r'/dev/mapper/*', device, re.MULTILINE)

    if '/device/mapper/' in device:
        print("It's a device mapper...let's find out the physical device/s behind!!!")
        check_physical_device_relative_to_dm = subprocess.Popen(['lvs', '-o', '+devices', '%s' % device], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_lvs = check_physical_device_relative_to_dm.communicate()[0]
    else:
        print("Looks like %s is a physical device" % device)

    print("Finishing the program...")
