import subprocess
def scan():
    s = "nmcli dev wifi rescan"
    subprocess.run(s, shell=True, capture_output=False, text=True)
    command = "nmcli -t -f SSID dev wifi"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        ssids = result.stdout.strip().split('\n')
        ssids_csv = ','.join(filter(None, ssids))
        ssids_csv = ssids_csv.split(',')
        if ssids_csv == ['']:
            print('no networks found, rfkill may be active.')
            return 'err'
        return ssids_csv
    else:
        z = result.stderr
        print(z)
        return 'err'
while 1:
    ssids=scan()
    if ssids == 'err':
        exit()
    for i in range(len(ssids)):
        print(i,"> "+ssids[i])
    s = int(input("scan again ?\n1:yes\n2:no\n:"))
    if s == 2:
        break
n = int(input("SSID_INDEX:"))
passwd = input("PASS:")
execr = "nmcli dev wifi connect '"+ssids[n]+"' password "+passwd
out = subprocess.run(execr, shell=True, capture_output=False, text=False)
if out.returncode == 0:
    print("Connected to "+ssids[n])
else:
    print("Incorrect password")