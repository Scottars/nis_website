import subprocess
# subprocess.call('du -hs $HOME', shell=True)
child=subprocess.check_output(['python3','proxy.py'],shell=True)
# child=subprocess.Popen(['python3','zmq_sub_2.py'],shell=True)

print(child)