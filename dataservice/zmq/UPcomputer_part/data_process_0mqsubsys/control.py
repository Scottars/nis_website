import os, signal

def kill(pid):
    print('pid', pid)
    a = os.kill(pid, signal.SIGKILL)
    print('pid is :%s,　return is:%s' % (pid, a))


def kill_target(target):
    cmd_run = "ps aux | grep {}".format(target)
    out = os.popen(cmd_run).read()
    pid = int(out.split()[1])
    print(pid)
    kill(pid)

kill_target('run.py')