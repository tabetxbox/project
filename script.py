#this script compresse and save files 
#os:linux
#you should run this script on root
import os
import time
# 1. The files and directories to be backed up are specified in a list
source=['/home/parrot/Downloads/']#remmeber to change this by waht you need
#where the  files that should be backup
target_dir='/mnt/backup.zip'
target=target_dir
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
#runing the backup
if os.system(zip_command) == 0:
    print 'succesfully backup to',target
else:
    print'sorry something is wrong'    
