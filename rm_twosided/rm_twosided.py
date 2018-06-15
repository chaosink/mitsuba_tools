#!/usr/bin/env python3

from lxml import etree as et
# import xml.etree.ElementTree as et
import sys

if len(sys.argv) < 3:
	print("Usage: python3 rm_twosided.py input_xml output_xml")
	sys.exit()

input_xml = sys.argv[1]
output_xml = sys.argv[2]

tree = et.parse(input_xml)
root = tree.getroot()

twosided_bsdfs = []
for bsdf in root.iter('bsdf'):
	if bsdf.get('type') == 'twosided':
		twosided_bsdfs.append(bsdf)

for bsdf in twosided_bsdfs:
	bsdf[0].set('id', str(bsdf.get('id')))
	p = bsdf.getparent()
	p.insert(0, bsdf[0])
	p.remove(bsdf)

tree.write(output_xml, pretty_print=True)
print("Twosided-removed XML saved to " + output_xml)
sys.exit()
