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

### Compatibility
As mentioned above, in order to run this script you need to run the tool with <strong>Python 3.x</strong>
### Author
This tool was written by and is maintained by aryamo.

