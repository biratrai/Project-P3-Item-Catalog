# Imports for XML EndPoints
from xml.etree import ElementTree
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from flask import Response

def create_xml(project,projectcategory,project_list):
	top = Element("PROJECTS")
	comment = Comment('Generated for PyMOTW')
	top.append(comment)

	# print project,projectcategory, project_list
	for i in project_list:
		print i.project_url
		print i.project_description
		print i.createdTime

	child = SubElement(top, project)


	child_with_tail = SubElement(child, 'projectcategory')
	child_with_tail.text = projectcategory

	for i in project_list:
		print i.project_url
		print i.project_description
		print i.createdTime

		child_with_tail2 = SubElement(child,'url')
		child_with_tail2.text = i.project_url

		child_with_tail2 = SubElement(child,'description')
		child_with_tail2.text = i.project_description

		child_with_tail2 = SubElement(child,'author')
		child_with_tail2.text = "santi"

		child_with_tail2 = SubElement(child,'date_create')
		child_with_tail2.text = str(i.createdTime)

	return prettify(top)
	
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    code source: http://pymotw.com/2/xml/etree/ElementTree/create.html
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")  