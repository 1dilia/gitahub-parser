from handler.workdata import WorkData

class WorkFile(WorkData):

    def do_type(self, issue):
        return issue

    def create_result(self, data):
        f = open('handler//plaintext.txt', 'w')
        for issue in data:
            f.write(
                "%d. %s (User: %s Created: %s)\n" % (issue['number'], issue['title'], issue['user']['login'],
                                                     WorkData.format_datetime(WorkData.utc_to_local(WorkData.get_datetime(issue['created_at']))))
                )
        f.close()
        return f
    #
    # def output_terminal(self):
    #     with open(self.data.name, 'r') as text:
    #         print(text.read())
    #
    # def output_file(self, filename):
    #     f = open(str('outcom//' + filename) + '.txt', 'w')
    #     with open(self.data.name, 'r') as text:
    #         for line in text:
    #             f.write(line)
    #     f.close()