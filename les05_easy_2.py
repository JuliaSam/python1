# easy 2
# Напишите скрипт, отображающий папки текущей директории.

import os
allFiles = os.listdir()
for i in enumerate(allFiles, 1):
    print(i)
