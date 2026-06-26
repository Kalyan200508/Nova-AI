import os
import shutil
import subprocess


class FileSystemSkill:

    def create_folder(self, name):

        try:

            os.makedirs(name, exist_ok=True)

            return f"Folder '{name}' created."

        except Exception as e:

            return str(e)

    def delete_folder(self, name):

        try:

            shutil.rmtree(name)

            return f"Folder '{name}' deleted."

        except Exception as e:

            return str(e)

    def create_file(self, filename):

        try:

            with open(filename, "w", encoding="utf-8"):
                pass

            return f"File '{filename}' created."

        except Exception as e:

            return str(e)

    def delete_file(self, filename):

        try:

            os.remove(filename)

            return f"File '{filename}' deleted."

        except Exception as e:

            return str(e)

    def rename(self, source, destination):

        try:

            os.rename(source, destination)

            return f"Renamed '{source}' to '{destination}'."

        except Exception as e:

            return str(e)

    def open_folder(self, path="."):

        try:

            subprocess.Popen(f'explorer "{os.path.abspath(path)}"')

            return f"Opening folder '{os.path.abspath(path)}'."

        except Exception as e:

            return str(e)


filesystem = FileSystemSkill()