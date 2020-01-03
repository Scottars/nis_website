import subprocess

p=subprocess.Popen(['python3', './proxy.py', '1', '2'], stdin = subprocess.PIPE, stdout=subprocess.PIPE)

out=p.stdout.readlines()

print(out)