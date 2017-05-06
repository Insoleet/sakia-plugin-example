import zipfile
import sys


PLUGIN_NAME = "plugin_example"


if "build" in sys.argv:
    zf = zipfile.PyZipFile(PLUGIN_NAME+ '.zip', mode='w')
    try:
        zf.writepy(PLUGIN_NAME)
    finally:
        zf.close()
    for name in zf.namelist():
        print(name)
