from directory import Directory
from file import File


class FileSystem:
    def __init__(self):
        self._root = Directory('')

    def add_file(self, file_path):
        self._add_file(file_path)

    def add_directory(self, dir_path):
        self._add_file(dir_path, add_file=False)

    def _add_file(self, file_path, add_file=True):
        """A helper function to add a file or directory"""
        paths = file_path.split('/')
        curr = self._root
        for i, path in enumerate(paths):
            next = curr._children.get(path)
            if next is None:
                if i == len(path) - 1 and add_file:
                    next = curr._children[path] = File(path)
                else:
                    next = curr._children[path] = Directory(path)
            curr = next

    def remove(self, file_path):
        paths = file_path.split('/')
        curr = self._root
        i = 0
        while i < len(paths) - 1:
            path = paths[i]
            next = curr._children.get(path)
            if next is None:
                print("File not found")
                return
            curr = next
            i += 1
        if paths[-1] in curr._children:
            curr._children.pop(paths[-1])
        else:
            print("File not found")

    def list_dir(self):
        pass


if __name__ == '__main__':
    fs = FileSystem()
    fs.add_directory('c')
    fs.add_directory('d')
    fs.add_directory('c/tmp/ha/1')
    fs.add_directory('c/tmp/ha/2')
    fs.remove('c/tmp/ha/2')
    pass
