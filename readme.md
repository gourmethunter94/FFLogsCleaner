## FFLogs Cleaner

FFLogs Cleaner's purpose is to remove old log files automatically on windows launch.

Setup on windows:
```
Press windows button + r and run "shell:startup".
Move 'fflogs_cleaner_launcher.bat', 'app.py', 'constants.py', and 'file_loader.py' in to the opened 'Startup' folder.
Open 'fflogs_cleaner_launcher.bat' and edit the 'absolute/path/to/logs' value after --path to root of your fflogs archive which can probably be found from %appdata%.
In the same 'fflogs_cleaner_launcher.bat' file edit the 'absolute/path/to/app.py' to point at the 'app.py' file you have downloaded from this repository.
```

You must also have setup python for windows.