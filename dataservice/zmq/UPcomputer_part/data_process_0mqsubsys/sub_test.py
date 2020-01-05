import subprocess

# p=subprocess.Popen(['python3', './proxy.py'])
# import os
#
# os.getpgid()
# print(p.pid)
import  psutil




def get_proc_by_name(pname):
    for proc in psutil.process_iter():
        print(proc)
        try:
            if proc.name().lower() ==pname.lower():
                return proc
        except:
            pass
    return None

if __name__ == "__main__":
    subproname='run'
    proc=get_proc_by_name(subproname)
    print(subproname,proc.pid)




# out=p.stdout.readlines()
#
# print(out)