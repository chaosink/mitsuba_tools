#!/usr/bin/env python3

from lxml import etree as et
# import xml.etree.ElementTree as et
import sys

if len(sys.argv) < 3:
	print("Usage: python3 rm_instance.py input_xml output_xml")
	sys.exit()

input_xml = sys.argv[1]
output_xml = sys.argv[2]

tree = et.parse(input_xml)
root = tree.getroot()

shapegroups = {}
for shape in root.iter('shape'):
	if shape.get('type') == 'shapegroup':
		shapegroups[shape.get('id')] = shape

instances = []
for shape in root.iter('shape'):
	if shape.get('type') == 'instance':
		instances.append(shape)

for shape in shapegroups.values():
	p = shape.getparent()
	p.remove(shape)

for shape in instances:
	p = shape.getparent()
	p.remove(shape)
	id = shape.find('ref').get('id')
	transform = shape.find('transform')
	for s in shapegroups[id]:
		s.append(transform)
	root.append(s)

tree.write(output_xml, pretty_print=True)
print("Instance-removed XML saved to " + output_xml)
sys.exit()
