# Imports for XML EndPoints
from xml.etree import ElementTree
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

def create_xml(project,projectcategory,project_list):

	# Parent Top Element
	top = Element("PROJECTS")
	comment = Comment('Generated for FullStack ND Project Catalog')
	top.append(comment)

	# First Child Element
	child = SubElement(top, project)


	child_with_tail = SubElement(child, 'projectcategory')
	child_with_tail.text = projectcategory

	for i in project_list:
		# Child's Child Element
		child_with_tail2 = SubElement(child_with_tail,'url')
		child_with_tail2.text = i.project_url

		child_with_tail2 = SubElement(child_with_tail,'description')
		child_with_tail2.text = "i.project_description"

		child_with_tail2 = SubElement(child_with_tail,'author')
		child_with_tail2.text = "santi"

		child_with_tail2 = SubElement(child_with_tail,'date_create')
		child_with_tail2.text = str(i.createdTime)

	return prettify(top)
	
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    code source: http://pymotw.com/2/xml/etree/ElementTree/create.html
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")  