# PoEPythonLoadTimer

Script to monitor load times in Path of Exile

### Usage

Run via python, i.e. `python load_times.py`.

When an area change occurs, the script will print a console message that shows the area that was loaded and the time it took to load.

### Requirements

Python. I tested in Python 3.7.3, but older versions should work as well.

### Troubleshooting

The default log file path is hardcoded. If you didn't install PoE to the default location, you'll need to change `LOG_FILE` in the code to reflect this. If your Path of Exile language is not English, you may need to change `LOAD_AREA_TEXT` and `AREA_CHANGE_TEXT`.
