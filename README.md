# wificon
user friendly python interface for nmcli.
## Install guide:
#### get the source:
`git clone https://github.com/AmriteshKr8/wificon.git`
#### get into the directory:
`cd wificon`
#### make scripts executable:
`sudo chmod +x *`
### 1.Install for user (~/.local/bin):
`./install-user`
### 2.Install for all users (/bin/):
`./install-all`
### 3.Install on distros that don't use apt:
1. install network-manager
2. install python3
3. copy both `wificon.py` and `wificon` to a directory included in your `$PATH` (if unsure just copy files to /bin/).
### Uninstall:
#### For method 1, delete both files from ~/.local/bin/:
`sudo rm -rf ~/.local/bin/wificon*`
#### For method 2, delete both files from /bin/:
`sudo rm -rf /bin/wificon*`
#### For method 3, delete both files from where you copied:
1. find where you put the files by running: 
`which wificon` 
note the path.
3. remove the last word until the slash ie. `/home/amritesh/.local/bin/wificon` to `/home/amritesh/.local/bin/`.
4. then, remove the files using this command:
`sudo rm -rf <path from last command>/wificon*`
