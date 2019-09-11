# SrtTranslator
Simple tool for automatically translating "srt" subtitles for your movies using the Microsoft translate API service.

This is a command line tool written in <strong>Python 3</strong> to translate your subtitles for your series or movies and tested on Windows Platform.

###  Microsoft API 
Before using this script, you need to have a Azure account and create a TextTranslation of cognitiveservices.
Then you will get a subscription key with a specific location (Region).

please fill them in <b>Translator.py</b>.

### Dependencies
This tool uses os, sys, requests, uuid and json , so you will need to install it in order to run the tool.

<strong>Installing packages is really easy, just run this:</strong>
```
pip install requests
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

part of tranlated result：
```
1
00:00:03,005 --> 00:00:05,008
- 看的人
你的事业，他们说
- People who look at
your career and they say

2
00:00:05,008 --> 00:00:07,003
你知道我想成为马克
ya know I want to be Marc.
...
5
00:00:11,003 --> 00:00:13,001
最好的营销人员和销售人员
The best marketers and salespeople

6
00:00:13,001 --> 00:00:15,000
了解他们的客户，他们是谁，
know their customers, who they are,

7
00:00:15,000 --> 00:00:16,004
以及他们如何购买。
and how they buy.

8
00:00:16,004 --> 00:00:17,009
有些人甚至更了解他们的客户
Some even know their customers better
...

```
### Known Issue
When some character in the files such as =, <, <, *. it will be caused an error.
```
145
00:17:24,006 --> 00:17:26,009
That's going to be Option > Function.

146
00:17:26,009 --> 00:17:32,000
=NOW, open close parens, and hit Enter.
```

### Available Languages
Checkout <a href="https://docs.microsoft.com/zh-cn/azure/cognitive-services/Translator/language-support#translation">here</a> for more information.

### Compatibility
As mentioned above, in order to run this script you need to run the tool with <strong>Python 3.x</strong>
### Author
This tool was written by and is maintained by aryamo.

