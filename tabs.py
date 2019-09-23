import subprocess

def bash_command(cmd):
    subprocess.Popen(cmd, shell=True, executable='/bin/bash')


bash_command('echo "oi"')







#import os


#os.system("gnome-terminal -e 'sudo apt-get update; read -p \"Hit ENTER to exit\"'")





# import subprocess


# var1 = "f0"

# subprocess.run(["./bbla {}".format(var1)], shell=True)





















#from subprocess import call

#with open('bbla', 'rb') as file:
#    script = file.read()
#rc = call(script, shell=True)
