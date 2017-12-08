#!/root/.pyenv/shims/python
import subprocess
import os
import sys
import json
import yaml

versions_tmp = os.popen('python -V').readlines()
version = ''
for i in versions_tmp:
    version = i.strip()

name_tmp = os.popen('pyenv version-name').readlines()
name = ''
for i in name_tmp:
    name = i.strip()

exec_location = sys.executable

pip_location_tmp = os.popen('which pip').readlines()
pip_location = ''
for i in pip_location_tmp:
    pip_location = i.strip()

python_path = sys.exec_prefix

packages_tmp = os.popen('pip freeze').readlines()
packages = []
for i in packages_tmp:
    packages.append(i.strip())

site_package = sys.path[-1]

keys = ["version","name","python_execut_location","pip_location","PYTHONPATH","installed_packages","site_packages"]
values = [version, name, exec_location, pip_location, python_path, packages, site_package ]

python_d = {}

length = len(keys) -1
while (length >= 0):
	python_d[keys[length]]=values[length]
	length -= 1
json_data = json.dumps(python_d, indent=1, sort_keys=True)
file = open("json_t6", "w")
file.write(json_data)
file.close()
	

data = dict(
    A = 'a',
    B = dict(
        C = 'c',
        D = 'd',
        E = 'e',
    )
)

with open('yaml_t6', 'w') as outfile:
    yaml.dump(python_d, outfile, default_flow_style=False)


print ("Collect information complited. Results in yaml_t6 and json_t6 in current directory.")
