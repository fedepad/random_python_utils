__author__ = 'Federico G. Padua'

import subprocess
import platform


def check_mount_debugfs(host_name):
    print("Now checking if debugfs is mounted. This is required to run blktrace!")
    subsub = subprocess.Popen(["mount", "-t", "debugfs"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #subsub.wait()
    output = subsub.communicate()[0]
    debugfspath = None
    lista = output.split()
    if not lista:
        print("OUTPUT is empty, probably will mount debugfs!")
        #pass
    else:
        if lista[1] == 'on' and lista[3] == 'type' and lista[4] == 'debugfs':
            debugfspath = lista[2]
    print("")
    print("***************    OUTCOME   *********************")
    print("")
    if not debugfspath:
        print("Mounting debugfs on host %s at /sys/kernel/debug" % (host_name))
        mount_proc = subprocess.Popen(["mount", "-t", "debugfs", "debugfs", "/sys/kernel/debug"])
        mount_proc.wait()
        print("now debugfs is mounted on host %s at /sys/kernel/debug" % (host_name))
    else:
        print("debugfs is already mounted on host %s at %s" % (host_name, debugfspath))

if __name__ == "__main__":

    print("**************************************************")
    print("*** This program checks if debugfs is mounted! ***")
    print("*** If it's not mounted, it will mount it!     ***")
    print("*** Then, blktrace will be run!                ***")
    print("**************************************************")
    print("")
    #print("This program run blktrace on the current host on a given device")
    # device
    # output_trace
    host_computer = platform.node()
    print("running on host: %s" % (host_computer))
    check_mount_debugfs(host_computer)
    retcode = subprocess.Popen(["blktrace", "-d", "/dev/dm-0", "-o", "dm-0_tailoredconfig"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("blktrace PID: %d" % retcode.pid)
    #retcode.kill()
    print("kill graciously blktrace (kill -15 PID or using SIGTERM signal)")
    #retcode.send_signal(signal.SIGTERM)
    retcode.terminate() # this sends a SIGTERM signal to the child process opened. Ok from python 2.6