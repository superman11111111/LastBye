from subprocess import check_output

DUMP_FILE = 'lastb.dump'
dmp = open(DUMP_FILE, 'w+')
old_ips = dmp.read().split('\n')
ips = [line.split()[2] for line in check_output(['lastb']).decode().split("\n")[:-3] if len(line.split()) == 10]
dmp.write('\n'.join(sorted(set(old_ips + ips))))
dmp.close()
