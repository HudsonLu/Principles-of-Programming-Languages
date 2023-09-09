from os import chdir, getcwd

current_dir = getcwd()
print('Current working directory is', 
      current_dir)
if current_dir.rindex('/'):
    chdir('..')
    current_dir = getcwd()
print('Working directory is now', 
      current_dir)


