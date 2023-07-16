#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
import datetime
from datetime import datetime, timedelta
import logging
import re


Path = "D:/Projets/Recette/Logs"
DateRetention = (datetime.now() - timedelta(days=7)) ## Date de rentention
DateRetentionYYYYmmdd = re.search('(\d+-\d+-\d+)', str(DateRetention)).group(0) ## Récuperation de la date de retention sous le format YYYY-mm-dd
TimeStamp = str(datetime.now().strftime("%Y%m%d_%H%M%S"))
LogFile = logging.basicConfig(format='%(asctime)s %(message)s', datefmt="%d-%m-%Y %I:%M:%S %p", filename="D:/Projets/Prodcution/Logs/Purge/PurgeRetention_"+TimeStamp+".log", level=logging.INFO)


def PurgeRetention():
    LogFile
    for EachFolder in os.listdir(Path):
        FullPath = Path + "/" + EachFolder
        if os.path.isdir(FullPath)==True:
            for EachFile in os.listdir(FullPath):
                if os.path.isfile(FullPath + "/" + EachFile)==True:
                    FullPathFile = os.path.join(FullPath + "/" + EachFile)
                    DateCreation = datetime.fromtimestamp(os.stat(FullPathFile).st_ctime) ## Récuperation de la date de création (full time, YYYY-mm-dd HH:mm:ss.sssss)
                    DateCreationYYYYmmdd = re.search('(\d+-\d+-\d+)', str(DateCreation)).group(0) ## Récuperation de la date sous le format YYYY-mm-dd
                    if DateCreationYYYYmmdd <= DateRetentionYYYYmmdd: ## Condition pour supprimer les fichiers de plus de x jours selon la retention
                        logging.info ("Suppression du fichier " + EachFile + " du repertoire " + EachFolder)
                        os.remove(FullPathFile)
                        if os.path.exists(FullPathFile)==False:
                            logging.info ("Le fichier " + EachFile + " n'éxiste plus. Il a été supprimé.")
                            logging.info (" ")
                        else:
                            logging.info ("Le fichier " + EachFile + " n'a pas été supprimé. Le fichier est toujours existant.")
                            logging.info (" ")


logging.info("-----")
logging.info ("Program started")
logging.info (" ")
logging.info ("Date de retention retenu : " + DateRetentionYYYYmmdd)
logging.info ("Les fichiers antérieur à cette date seront supprimés.")
logging.info (" ")
logging.info ("Début de la purge :")
PurgeRetention()
logging.info ("Program Finished")
logging.info("-----")
