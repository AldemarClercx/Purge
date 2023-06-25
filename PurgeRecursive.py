#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
from datetime import datetime, timedelta
import shutil
import logging
import re

Path = "D:/Projets/Recette/Logs"
DateRetention = (datetime.now() - timedelta(days=7))

for EachFolder in os.listdir(Path):
    FullPath = Path + "/" + EachFolder
    if os.path.isdir(FullPath)==True:
        print (EachFolder)
        print (" ")

    for EachFile in os.listdir(FullPath):
        if os.path.isfile(FullPath + "/" + EachFile)==True:
            FullPathFile = os.path.join(FullPath + "/" + EachFile)
            print (EachFile)
            DateCreation = datetime.fromtimestamp(os.stat(FullPathFile).st_ctime) ## Récuperation de la date de création (full time, YYYY-mm-dd HH:mm:ss.sssss)
            DateCreationYYYYmmdd = re.search('(\d+-\d+-\d+)', str(DateCreation)).group(0) ## Récuperation de la date sous le format YYYY-mm-dd
            DateRetentionYYYYmmdd = re.search('(\d+-\d+-\d+)', str(DateRetention)).group(0) ## Récuperation de la date de retention sous le format YYYY-mm-dd
            RetentionRetenu = DateCreation - timedelta(days=7) ## Récuperation de la date de retention retenu
            RetentionRetenuYYYYmmdd = re.search('(\d+-\d+-\d+)', str(RetentionRetenu)).group(0) ## Récuperation de la retention retenu sous le format YYYY-mm-dd

            print ("Date de création du fichier : " + str(DateCreationYYYYmmdd))
            print ("Date de rentention : " + str(DateRetentionYYYYmmdd))
            print ("Date de retention retenu : " + str(RetentionRetenuYYYYmmdd))
            print (" ")


if RetentionRetenuYYYYmmdd == DateRetentionYYYYmmdd:
    print (" ")
    print ("Il y a des fichiers à supprimés.")

else:
    print (" ")
    print ("il n'y a rien à supprimés.")
                

