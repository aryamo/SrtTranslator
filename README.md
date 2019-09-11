# SrtTranslator
Simple tool for automatically translating "srt" subtitles for your movies using the Microsoft translate API service.

This is a command line tool written in <strong>Python 3</strong> to translate your subtitles for your series or movies.

##### Dependencies
This tool uses os, sys, requests, uuid and json , so you will need to install it in order to run the tool.

<strong>Installing goslate is really easy, just run this:</strong>
```
pip install requests, uuid, json, os
```
### Running the tool
Just open your terminal and type:
```
python main.py [sub.srt] [desired sub lang] [original sub lang]
```
or for auto detecting the sub language:
```
python main.py [sub.srt] [desired sub lang]
```
Finally the tool will create for you a file with an upper case postfix for your desired language. e.g:
```
python main2.py "C:\Users\zhangwx\Desktop\test\Test1.en.srt"
```
will output: ```Test1.en_ES.srt```

Final Run example:
This is for whole folder that contains all srt files.
```
python main2.py "C:\Users\zhangwx\Desktop\test"
```
This for single srt file.
```
python main2.py "C:\Users\zhangwx\Desktop\test\806161_03_01 - AKS storage overview.en.srt"
```

<strong>Note:</strong> Make sure your srt subtitle files have an UTF8 encoding, else you will have errors.
Checkout <a href="http://redhotwords.com/unicode.html">here</a> to how to set the encoding in case you have a different encoding than UTF8
### Available Languages
Checkout <a href="https://docs.microsoft.com/zh-cn/azure/cognitive-services/Translator/language-support#translation">here</a> for more information.
|  |  | | |
|:---------------------------|:-------------------------|:---------------------------|:-----------------|
|pt   : Portuguese           |de   : German           |kn   : Kannada             |be   : Belarusian|  
|hi   : Hindi                |iw   : Hebrew           |ny   : Chichewa            |lo   : Lao       |   
|mk   : Macedonian           |ta   : Tamil            |tr   : Turkish             |pl   : Polish    |
|hr   : Croatian             |zu   : Zulu             |ga   : Irish               |pa   : Punjabi   |
|ca   : Catalan              |te   : Telugu           |mr   : Marathi             |es   : Spanish   |
|ur   : Urdu                 |uk   : Ukrainian        |ka   : Georgian            |km   : Khmer     |
|no   : Norwegian            |tg   : Tajik            |my   : Myanmar (Burmese)   |ar   : Arabic    |
|ig   : Igbo                 |ml   : Malayalam        |it   : Italian             |mt   : Maltese   |
|gu   : Gujarati             |sv   : Swedish          |so   : Somali              |bg   : Bulgarian |
|az   : Azerbaijani          |ko   : Korean           |gl   : Galician            |fil  : Filipino  |
|kk   : Kazakh               |sk   : Slovak           |ne   : Nepali              |la   : Latin     |
|fi   : Finnish              |vi   : Vietnamese       |sw   : Swahili             |nl   : Dutch     |
|af   : Afrikaans            |id   : Indonesian       |cs   : Czech               |ha   : Hausa     |
|fr   : French               |si   : Sinhala          |su   : Sundanese           |hy   : Armenian  |
|ja   : Japanese             |lt   : Lithuanian       |ht   : Haitian Creole      |lv   : Latvian   |
|fa   : Persian              |en   : English          |sr   : Serbian             |mg   : Malagasy  |
|zh   : Chinese              |bn   : Bengali          |th   : Thai                |el   : Greek     |
|eo   : Esperanto            |st   : Sesotho          |mn   : Mongolian           |yi   : Yiddish   |
|da   : Danish               |ms   : Malay            |ru   : Russian             |cy   : Welsh     |
|sl   : Slovenian            |mi   : Maori            |yo   : Yoruba              |ro   : Romanian  |
|bs   : Bosnian              |sq   : Albanian         |zh-Hans: Chinese (Simplified)|jw   : Javanese  |
|et   : Estonian             |eu   : Basque           |is   : Icelandic           |mww  : Hmong     |
|zh-Hant: Chinese (Traditional)|ceb  : Cebuano          |uz   : Uzbek               |hu   : Hungarian |

### Compatibility
As mentioned above, in order to run this script you need to run the tool with <strong>Python 3.x</strong>
### Author
This tool was written by and is maintained by aryamo.

