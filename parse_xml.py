import xml.etree.ElementTree as ET

def parse_and_remove(filename, path):
   path_parts = path.split('/')
   doc = ET.iterparse(filename, ('start', 'end'))
   # Skip root element
   next(doc)
   tag_stack = []
   elem_stack = []
   for event, elem in doc:
    if event == 'start':
      tag_stack.append(elem.tag)
      elem_stack.append(elem)
    elif event == 'end':
                if tag_stack == path_parts:
                    yield elem
                try:
                    tag_stack.pop()
                    elem_stack.pop()
                except IndexError:
                    pass


country_government = []
countries = parse_and_remove('mondial-3.0.xml', 'country')
for country in countries:
    government = country.attrib['government']
    name = country.attrib['name']
    if ' ' in name and government not in country_government:
        country_government.append(government.strip(' '))
print(country_government)
