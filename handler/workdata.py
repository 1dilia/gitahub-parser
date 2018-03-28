from abc import abstractmethod
import argparse
from datetime import datetime, timezone

class WorkData(object):
    def __init__(self, data):
        self.data = self.create_result(data)

    @abstractmethod
    def do_type(self, issue):
        ...

    @abstractmethod
    def create_result(self, data):
        ...
    #
    # @abstractmethod
    # def output_terminal(self, result):
    #     ...
    #
    # @abstractmethod
    # def output_file(self, result, filename):
        ...

    def get_datetime(date_time):
        format_date = "%Y-%m-%dT%H:%M:%SZ"
        return datetime.strptime(date_time, format_date)

    def utc_to_local(utc_dt):
        return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

    def format_datetime(date_time):
        new_format = "%H:%M:%S %d.%m.%Y"
        return date_time.replace(tzinfo=None).__format__(new_format)

    # @staticmethod
    # def get_sys_argv():
    #     parser = argparse.ArgumentParser(description="""This program parses repositories in the github.\n
    #                                                        Enter owner/name_repository for show in terminal .\n
    #                                                        Output data can be in xml format (--xml
    #                                                         or written to a file""")
    #     parser.add_argument('repository', help='path to the repository')
    #     parser.add_argument('--xml', help='--xml - show in xml', action='store_true')
    #     parser.add_argument('--file', nargs='?', help='--file=filename - write to file')
    #     return parser
    #
    # def get_url_for_request(sys_argv_repository):
    #     return 'https://api.github.com/repos/' + str(sys_argv_repository) + '/issues?state=open'


