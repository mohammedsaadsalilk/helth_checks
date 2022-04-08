import os
import sys
import shutil

def check_reboot():
    ''' Return True if the computer has a pending reboot.'''
    return os.path.exist("/run/reboot-required")
def check_disc_full(disk, main_gb, main_percent):
    '''Return True if there isn't enough disk space, Faise otherwise.'''
    du= shutil.disc_usage(disk)
    #Calculate the percentag of free space
    percent_free= 100 * du.free / du.total
    #Calculate how many free gigabytes
    gigabytes_free= du.free/ 2**30
    if percent_free < main_percent or gigabytes_free < main_gb:
        return True
    return False

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exis(1)
    if check_disc_full(disk= '/', main_gb= 2, main_percent= 10):
        print("Disk full.")
        sys.exis(0)
