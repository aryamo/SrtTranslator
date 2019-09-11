#pip install requests
import requests, uuid, json

class Translator:
    """ This class contains all the translation logic. """
    def __init__(self, subList, fromLang, toLang):
        self._subInfoList = subList

        #fill Ocp-Apim-Subscription-Key with your subscription_key
        #fill Ocp-Apim-Subscription-Region with the Microsoft Translate API region such as Chinanoth, Chinaeast2
        #if you are using Glabla Azure please fill the right API URL instead 'https://api.translator.azure.cn/translate?api-version=3.0'

        self._constructed_url = 'https://api.translator.azure.cn/translate?api-version=3.0' + '&from='+ fromLang +'&to=' + toLang
                
        self._headers = {
            'Ocp-Apim-Subscription-Key': '0*******************************',
            'Ocp-Apim-Subscription-Region': 'Chinaeast2',
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

    def Translate(self):
        """ returns a subInfoList with the subtitles translated. """
        linesPerTranslation = 250 if 250 < len(self._subInfoList)-1 else len(self._subInfoList)-1

        separationToken = "\r" #we suggest you should use the \r or \t. if change token, make sure that the token is change after translation.
        text = ""
        counter = 0
        globCounter = 0
        translatedTexts = [] #contains the translated strings from the srt
        for subInfo in self._subInfoList:
            text = text + subInfo.GetText() + separationToken
            
            if(counter>=linesPerTranslation) or (linesPerTranslation >= ((len(self._subInfoList)-1)-globCounter) and ((globCounter+1) == len(self._subInfoList))):#we translate by batches
                text = text[:-len(separationToken)]#cut the last token
                #print(text,'\n')
                #print(len(str(text)),'\n')
                body = [{'text' : text}]
                #print(body,'\n')
                             
                if(len(str(text)) >= 5000):
                    print("Error! The subtitle more than 5000 characters.")
                    return self._subInfoList
                
                request = requests.post(self._constructed_url, headers=self._headers, json=body)
                response = request.json()             
                
                #print(response,'\n')
                
                translatedSubs = str(response[0]['translations'][0]['text'])
                
                #print(translatedSubs,'\n')
                
                translatedSubsList = translatedSubs.split(separationToken)

                translatedTexts.extend(translatedSubsList)
                counter = 0
                text = ""
            counter += 1
            globCounter += 1

        #print(str(len(self._subInfoList)) + " =? " + str(len(translatedTexts)))
        translatedSubInfoList = self._subInfoList
        i = 0
        for subInfo in translatedSubInfoList:
            subInfo.SetText(translatedTexts[i])
            i += 1

        return translatedSubInfoList
		