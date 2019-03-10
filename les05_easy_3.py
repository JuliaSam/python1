# easy 3
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
import shutil

shutil.copyfile(sys.argv[0], sys.argv[0] + ".copy")
