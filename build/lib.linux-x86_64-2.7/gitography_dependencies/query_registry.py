import requests


class DockerRegistry(object):

    def __parse_search(self, search):
        return search.replace(':', '/tags/')

    def __connect(self, search):
        try:
            response = requests.get(self.registry + search)
            # Clean up below
            # if not response.status_code // 100 == 2:
            return response
        except requests.exceptions.RequestException as e:
            return e

        return response

    def __init__(self, registry):
        self.registry = registry

    def query(self, search):
        parsed_search = self.__parse_search(search)
        connection = self.__connect(parsed_search)
        self.status = connection.status_code
        if self.status == 200:
            return True
        else:
            return False

