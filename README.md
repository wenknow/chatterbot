
##  一、获取语料

* 中文聊天语料这一块，我选择了网上大神整理的资料，选取其中一部分，小黄鸡语料
公开中文语料包：https://pan.baidu.com/s/1szmNZQrwh9y994uO8DFL_A 提取码：f2ex 中。

![](https://upload-images.jianshu.io/upload_images/21643577-f3b7f711f401a90a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600)


## 二、训练

#### 1、上传语料包 
* 上传处理好的小黄鸡语料到服务器上，有条件的可以使用 [Google colab](https://colab.research.google.com/notebooks/welcome.ipynb)进行训练

#### 2、在服务器上安装 ChatterBot
```
pip3 install chatterbot
pip3 install chatterbot-corpus
```

#### 3、试运行chatterbot
* 运行以下代码将会自动安装nltk_data，此过程可能会很久
```
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("bot")
trainer = ListTrainer(chatbot)
```

#### 4、修改chatterbot中nltk_data的目录
* 找到python的第三方包site-packages的路径下的chatterbot
```
cd /usr/local/lib/python3.6/site-packages/chatterbot/
vim utils.py
```
* 修改内容如下
```
def download_nltk_stopwords():

"""

Download required NLTK stopwords corpus if it has not already been downloaded.

"""

nltk_download_corpus('corpora/stopwords')

def download_nltk_wordnet():

"""

Download required NLTK corpora if they have not already been downloaded.

"""

nltk_download_corpus('corpora/wordnet')

def download_nltk_averaged_perceptron_tagger():

"""

Download the NLTK averaged perceptron tagger that is required for this algorithm

to run only if the corpora has not already been downloaded.

"""

nltk_download_corpus('taggers/averaged_perceptron_tagger')

def download_nltk_vader_lexicon():

"""

Download the NLTK vader lexicon for sentiment analysis

that is required for this algorithm to run.

"""
nltk_download_corpus('sentiment/vader_lexicon')
```

#### 5、创建一个 Chat Bot并进行训练
```
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("小明")
trainer = ListTrainer(chatbot)
with open('part.data', encoding='utf-8') as f:
data = f.read().replace('\t', '\n')
data = data.split("\n")

trainer.train(data)
```

#### 6、本地测试
```
from chatterbot import ChatBot
import sys

bot = ChatBot(
    '小明',
    database_uri='sqlite:///db.sqlite3'
 )
 
print('Type something to begin...')
 
while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
```


## 三、部署成服务
* 安装flask
```
pip3 install flask
```
* 安装uwsgi
```
yum install -y pcre pcre-devel pcre-static
yum install -y python3-devel
pip3 install uwsgi --no-cache-dir
```
* 新建api.py文件
```
vim api.py
```
* 添加如下内容
```
from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
 
app = Flask(__name__)
 
bot = ChatBot(
    'С˼',
    database_uri='sqlite:///db.sqlite3'
)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/api/<text>")
def get_bot_api(text):
    res = str(bot.get_response(text))
    return jsonify(res), 200


if __name__ == "__main__":
	app.run(host='0.0.0.0')
```

* 新建在项目目录下，添加uwsgi配置
```
vim uwsgi.ini
```
* 添加如下内容
```
[uwsgi]

http = 0.0.0.0:5000
chdir = /usr/share/nginx/html/chatbot/chatterbot
wsgi-file = api.py
callable = app
processes = 4
threads = 2
master = true
vacuum = true
```
* 运行uwsgi
```
uwsgi uwsgi.ini
```
* 调用
```
$url = "http://127.0.0.1:5000/api/{$word}";
$reply = $this->getData($url);
```

## 附：源码
[https://github.com/wenknow/chatterbot](https://github.com/Wc241/chatterbot)
