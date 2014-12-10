#!/usr/bin/env python
try:
	import bz2,base64 as a,os,sys,zlib;c=sys.argv[1]
except:
	print ' [X] Usage: ./pycompressor.py script.py'
	exit()
with open(c,'rb') as d:d=d.read();e,f=bz2.compress(d),zlib.compress(d,9)
g,compalg=list(map(len,(d,e,f))),''
print ' [>] Original size:\t%s' % g[0]
print ' [>] bz2 size:\t\t%s' % g[1]
print ' [>] zlib size:\t\t%s' % g[2]
s,h,i,j,k=g.index(min(g)),'#!/usr/bin/env python\nimport base64','\nexec(','.decompress(','base64.b64decode("{1}"))'
if s==1:compalg, val = 'bz2', g[1]
elif s==2:compalg, val = 'zlib',g[2]
else:e=h+i+k
if compalg:
	d,e=f,h+','+compalg+i+compalg+j+k+')';print ' [!] Using ' + compalg + '\n [*] % of original:\t{0:.0f}%'.format(float(val)/g[0] * 100)
else:
	print ' [X] Unable to compress ' + os.path.splitext(c)[0]
	exit()

with open(os.path.splitext(c)[0] + '_packed.py','w') as f:f.write(e.format(os.path.basename(c),a.b64encode(d)))
if os.name == 'posix':
	os.system('chmod +x ' + os.path.splitext(c)[0] + '_packed.py')
print ' [*] Packed script written to ' + os.path.splitext(c)[0] + '_packed.py'