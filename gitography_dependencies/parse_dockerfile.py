import re
import query_registry


# TODO make parse a single call with a dict/tuple of queries
# TODO: Move out parse_file functionality into a seperate function
# TODO: Log if we cant build

class Dockerfile(object):
    def __init__(self, dockerfile):
        self.dockerfile = dockerfile
        self.query_result = self.__parse_file({
            'image': 'FROM (.*)',
            'repo': 'IMAGE_REPO = (.*)',
            'tag': 'IMAGE_TAG = (.*)',
            'registry': 'IMAGE_REG = (.*)'})

        self.image = self.query_result['image']
        self.repo = self.query_result['repo']
        self.tag = self.query_result['tag']
        self.registry = self.query_result['registry']
        self.built = self.__build_check()

    def __parse_file(self, patterns):
        query_results = {'image': "", 'repo': "", 'tag': "", 'registry': ""}
        with open(self.dockerfile, "r") as stream:
            for line in stream:
                for key, value in patterns.iteritems():
                    query = re.search(r'%s' % value, line)
                    if query:
                        query_results[key] = query.group(1)

        return query_results

    def __build_check(self):
        registry_connection = query_registry.DockerRegistry(self.registry)
        response = registry_connection.query(self.image)
        return response
