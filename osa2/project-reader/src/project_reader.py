import tomlkit
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = tomlkit.loads(content)

        name = data.get("name", "Test name")
        description = data.get("description", "Test description")
        dependencies = data.get("dependencies", [])
        dev_dependencies = data.get("dev-dependencies", [])

        return Project(name, description, dependencies, dev_dependencies)
