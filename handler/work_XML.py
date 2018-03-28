from handler.workdata import WorkData
import xml.etree.ElementTree as ET

class WorkXML(WorkData):

    def create_row_elem(self, row):
        root_row = ET.Element("issue", attrib={'number': str(row['number'])})

        title = ET.SubElement(root_row, "title")
        title.text = str(row['title'])

        user = ET.SubElement(root_row, "user")
        user.text = "{}".format(row['user']['login'])

        created_format = ET.SubElement(root_row, "created", attrib={'format': 'H:i:s d.m.Y', 'tz': '+3'})
        created_format.text = WorkData.format_datetime(
            WorkData.utc_to_local(WorkData.get_datetime(row['created_at'])))

        return root_row

    def create_result(self, data):
        root = ET.Element('issues')
        for item in data:
            root.append(self.create_row_elem(item))
        return ET.ElementTree(root)

    def do_type(self, issue):
        root = ET.Element("issue", attrib={'number': str(issue['number'])})
        title = ET.SubElement(root, "title")
        title.text = issue['title']

        user = ET.SubElement(title, "user")
        user.text = "user.{}".format(issue['user']['login'])

        created_format = ET.SubElement(root, "created")
        created_format.text = WorkData.format_datetime(
            WorkData.utc_to_local(WorkData.get_datetime(issue['created_at'])))

        ET.ElementTree(root)
        print(str(ET.tostring(root, encoding='utf-8').decode('utf-8')))
    #
    # def output_file(self, filename):
    #     self.data.write(str('outcom//' + filename) + '.xml', encoding='utf-8', xml_declaration=True)
    #
    # def output_terminal(self):
    #     print(str(ET.tostring(self.data.getroot(), encoding='utf-8').decode('utf-8')))