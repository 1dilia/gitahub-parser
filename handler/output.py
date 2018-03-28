class FileOutput():
    def __init__(self, filename, args_xml):
        self.filename = filename
        # self.data = data
        self.is_xml = args_xml
        # self.work_file = 'handler/plaintext.txt'
        # self.data = WorkData.data

    def xml_output_file(self, filename):
        self.data.write(str('outcom//' + filename) + '.xml', encoding='utf-8', xml_declaration=True)

    def txt_output_file(self, filename):
        f = open(str('outcom//' + filename) + '.txt', 'w')
        with open(self.work_file, 'r') as text:
            for line in text:
                f.write(line)
        f.close()

    def printt(self, is_xml):
        if is_xml:
            return self.xml_output_file(self.filename)
        else:
            return self.txt_output_file(self.filename)


class TerminalOutput():
    def __init__(self, args_xml):
        self.data =  WorkData.data
        self.is_xml = args_xml
        # self.work_file = 'handler/plaintext.txt'

    def xml_output_terminal(self):
        print(str(ET.tostring(self.data.getroot(), encoding='utf-8').decode('utf-8')))

    def txt_output_terminal(self):
        with open(self.data, 'r') as text:
            print(text.read())

    def printt(self, is_xml):
        if is_xml:
            return self.xml_output_terminal()
        else:
            return self.txt_output_terminal()