import os
pypath = []
for dirpath, dirnames, filenames in os.walk("main"):
    pypath = (dirpath for filename in filenames if filename.endswith('py'))
with open('pypath.txt', 'w') as f:
    f.write('\n'.join(pypath))
