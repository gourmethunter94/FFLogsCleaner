from os.path import isfile, isdir
from os import listdir, remove
from constants import PATH, AGE, SAFE, BASE_VALUE_PATH, BASE_VALUE_AGE, BASE_VALUE_SAFE, SEPARATOR
import time, os, stat

class FileLoader:
    def remove_file(self, path):
        remove(path)

    def file_as_list(self, path):
        self._secure_file(path)
        text_file = open(path, "r")
        return text_file.readlines()

    def directory_tree(self, path):
        files = []
        for candidate in listdir(path):
            path_to_candidate = path+"/"+candidate
            if isdir(path_to_candidate):
                candidate_files = self.directory_tree(path_to_candidate)
                files = files + candidate_files
            elif isfile(path_to_candidate):
                files.append(path_to_candidate)
        return files

    def file_age_in_seconds(self, pathname):
        return time.time() - os.stat(pathname)[stat.ST_MTIME]

    def list_as_file(self, path, list_to_file):
        file_to_write = open(path, "w")
        for line in list_to_file:
            file_to_write.write(line + "\n")
        file_to_write.close()

    def _secure_file(self, path):
        if not isfile(path):
            text_file = open(path, "w")
            text_file.write(PATH + SEPARATOR + BASE_VALUE_PATH + "\n")
            text_file.write(AGE + SEPARATOR + BASE_VALUE_AGE + "\n")
            text_file.write(SAFE + SEPARATOR + BASE_VALUE_SAFE + "\n")
            text_file.close()

