#
# SubTranslate Simple tool that translates subtitles.
#
# NAME:
#    SubTranslate - quickly translate subtitles from any language
#
# SYNOPSIS:
#!/usr/bin/python
#    python main.py [srt file | folder contains srts] [desired sub lang] [original sub lang]
#
#    For default english to simple chinese language:
#    python main.py [srt file | folder contains srts]
#
# Notes:
#   Avoid lines with spaces in the sub
#
#   *******************************************************
#   ***** Make sure your srt file encoding is in UTF8 *****
#   *******************************************************

#pip install requests

import sys
#introduce python Enum Class
from enum import Enum
#introduce utils.py
from Utils import Utils
#introduce Translator.py
from Translator import Translator

import os


## MAIN ##
#make sure we have the correct number of args
if len(sys.argv) == 2 or len(sys.argv) == 3 or len(sys.argv) == 4:
    desiredSubLang = sys.argv[2] if len(sys.argv) == 3 else u'zh-Hans'
    originalSubLang = sys.argv[3] if len(sys.argv) == 4 else u'en'
    #print(desiredSubLang,'\n')
    #print(originalSubLang,'\n')
    
    #print(sys.argv[1],'\n')
    
    if (sys.argv[1].endswith('.srt')):
        (filepath,filename) = os.path.split(sys.argv[1])
        dict = Utils.ParseSRTFile(sys.argv[1])
        #print(dict, '\n')
        translatedSubInfo = []
        for key, parsedSubInfoList in dict.items():
            if len(parsedSubInfoList) != 0:#make sure the srt file was correctly translated
                subTranslator = Translator(parsedSubInfoList, originalSubLang, desiredSubLang)
            
                print("Translating...")
                transTemp = subTranslator.Translate()
                translatedSubInfo.extend(transTemp)
        
        
        #print(type(translatedSubInfo))
        #print(translatedSubInfo)
        print("Writing file to: " + filepath + "\\" + os.path.splitext(filename)[0] +"_" + desiredSubLang.upper() + os.path.splitext(filename)[-1] + "...")
        Utils.WriteSRTFile(filepath + "\\" + os.path.splitext(filename)[0] +"_" + desiredSubLang.upper() + os.path.splitext(filename)[-1], translatedSubInfo)

        print("Done!") 
    else:
        #"""Batch translte SRT files in a folder"""
        for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
            for filepath in filenames:
                translatedSubInfo = []
                tempPath = os.path.join(dirpath, filepath)
                #print(tempPath,'\n')
                if filepath[-4:]=='.srt' or filepath[-4:]=='.SRT':
                    dict = Utils.ParseSRTFile(tempPath) 
                    print("Translating...")
                    for key, parsedSubInfoList in dict.items():
                        subTranslator = Translator(parsedSubInfoList, originalSubLang, desiredSubLang)
                        transTemp = subTranslator.Translate()
                        translatedSubInfo.extend(transTemp)

                    print("Writing file to: " + dirpath + "\\" + os.path.splitext(filepath)[0] +"_" + desiredSubLang.upper() + os.path.splitext(filepath)[-1] + "...")
                    Utils.WriteSRTFile(dirpath + "\\" + os.path.splitext(filepath)[0] +"_" + desiredSubLang.upper() + os.path.splitext(filepath)[-1], translatedSubInfo)
                    print("Done!")  
                translatedSubInfo[:] = []
				
else:
    print("""\nERROR: wrong on arguments, try:\n
      python main.py [srt file | folder contains srts] [desired sub lang] [original sub lang]\n
      or for For default english to simple chinese language:\n
      python main.py [srt file | folder contains srts]\n""")
      
