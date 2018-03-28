from json import *
from urllib import request
from handler.workdata import WorkData
from handler.work_file import WorkFile
from handler.work_XML import WorkXML
import xml.etree.ElementTree as ET
fro handler.output

import argparse


# if __name__ == '__main__':
#
#     args = WorkData.get_sys_argv().parse_args()
#     response = request.urlopen(WorkData.get_url_for_request(args.repository))
#     data = JSONDecoder().decode(response.read().decode('utf-8'))
#
#     if args.xml:
#         obg_result = WorkXML(data)
#     else:
#         obg_result = WorkFile(data)
#
#     if args.file:
#         obg_result.output_file(data, args.file)
#     else:
#         obg_result.output_terminal(data)
#






def parseJsonResponse(response):
    return JSONDecoder().decode(response.read().decode('utf-8'));

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""This program parses repositories in the github.\n
                                                                       Enter owner/name_repository for show in terminal .\n
                                                                       Output data can be in xml format (--xml
                                                                        or written to a file""")
    parser.add_argument('repository', help='path to the repository')
    parser.add_argument('--xml', help='--xml - show in xml', action='store_true')
    parser.add_argument('--file', nargs='?', help='--file=filename - write to file')
    args = parser.parse_args()

    url = 'https://api.github.com/repos/' + str(args.repository) + '/issues?state=open'

    response = request.urlopen(url)

    data = parseJsonResponse(response)

    if args.xml:
        worker = WorkXML(data)
    else:
        worker = WorkFile(data)

    if args.file:
        output = FileOutput(args.file,args.xml)
    else:
        output = TerminalOutput(args.xml)

    output.printt(args.xml)

    # worker.printt(output)