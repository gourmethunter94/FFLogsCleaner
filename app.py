from file_loader import FileLoader
from constants import PATH, AGE, SAFE, BASE_VALUE_PATH, BASE_VALUE_AGE, BASE_VALUE_SAFE, SETTINGS, SEPARATOR
from sys import argv as ARGS

class FFLogsCleaner:
    def __init__(self, path_to_settings, new_settings=None):
        self.file_loader = FileLoader()
        if not new_settings:
            self._load_settings(path_to_settings)
        else:
            self._load_settings(path_to_settings)
            self._write_settings(path_to_settings, new_settings)
        self._verify_settings()
        files = self.file_loader.directory_tree(self.settings.get(PATH))
        for file_path in files:
            if file_path[-len(self.settings.get(SAFE)):] == self.settings.get(SAFE):
                if self.file_loader.file_age_in_seconds(file_path) > int(self.settings.get(AGE)) * 24 * 60 * 60:
                    self.file_loader.remove_file(file_path)
                    print("Removed file: " + file_path.split("/")[-1])

    def _load_settings(self, path_to_settings):
        self.settings = {}
        for setting in self.file_loader.file_as_list(path_to_settings):
            setting, value = setting.replace("\n", "").split(SEPARATOR)
            if setting in SETTINGS:
                self.settings.update({setting:value})
            else:
                print("Invalid setting: " + setting + ": " + value)
    
    def _write_settings(self, path_to_settings, new_settings):
        for key in new_settings:
            self.settings.update({key:new_settings.get(key)})
        settings_as_list = []
        for key in self.settings:
            settings_as_list.append(key + SEPARATOR + self.settings.get(key))
        self.file_loader.list_as_file(path_to_settings, settings_as_list)

    def _verify_settings(self):
        if self.settings.get(PATH) == BASE_VALUE_PATH:
            exit(print(BASE_VALUE_PATH))
        if self.settings.get(AGE) == BASE_VALUE_AGE:
            exit(print(BASE_VALUE_AGE))
        if self.settings.get(SAFE) == BASE_VALUE_SAFE:
            exit(print(BASE_VALUE_SAFE))

PATH_TO_SETTINGS = "settings.fcs"

if len(ARGS) == 1:
    fflogs_cleaner = FFLogsCleaner(PATH_TO_SETTINGS)
else:
    new_settings = {}
    for argument_index in range(1, len(ARGS)):
        argument = ARGS[argument_index]
        if "--" in argument:
            if argument.replace("--", "") in SETTINGS:
                new_settings.update({argument.replace("--", ""):ARGS[argument_index+1]})
    fflogs_cleaner = FFLogsCleaner(PATH_TO_SETTINGS, new_settings=new_settings)