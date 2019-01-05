#!/usr/bin/env python3

import os
import sys
import shutil
from timeit import default_timer as timer

if len(sys.argv) != 4:
	print('Usage: render_spp.py mitsuba_bin scene.xml "1 2 4 8..."')
	exit(0)

mitsuba_bin = sys.argv[1]
scene_file = sys.argv[2]
spps = sys.argv[3].split()

if not os.path.exists(mitsuba_bin) and not shutil.which(mitsuba_bin):
	print('Mitsuba binary file does not exist: ' + mitsuba_bin)
	exit(1)

if os.path.exists(scene_file):
	with open(scene_file, 'r') as f:
		scene_xml = f.read()
else:
	print('Scene file does not exist: ' + scene_file)
	exit(1)

def StrIsInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

for spp in spps:
	if not StrIsInt(spp):
		print('Invalid SPP count: ' + spp)
		exit(1)

pos0 = scene_xml.find('sampleCount')
pos0 = scene_xml.find('value', pos0)
pos0 = scene_xml.find('"', pos0) + 1
pos1 = scene_xml.find('"', pos0)

pos = scene_file.rfind('.')
scene_file_stem = scene_file[:pos]

start = timer()
for spp in spps:
	scene_file_new = scene_file_stem + '_' + spp + '.xml'
	scene_xml_new = scene_xml[:pos0] + spp + scene_xml[pos1:]
	with open(scene_file_new, 'w') as f:
		f.write(scene_xml_new)
	os.system(mitsuba_bin + ' ' + scene_file_new)
	os.remove(scene_file_new)
end = timer()

duration = int(end - start)
ss = end - start - duration
s = duration % 60
m = duration / 60 % 60
h = duration / 3600
print('\nTotal Time: %02d:%02d:%05.2f' % (h, m, s + ss))
