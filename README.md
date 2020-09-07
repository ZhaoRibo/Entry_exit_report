# Entry_exit_report
某世一大物院某人由于不想每天实验时都要花上几分钟进行千篇一律的报备而搞。

不知道什么原因，打包后每天第一次运行可能会卡在进入门户时的页面，解决方法就是终止第一次运行而后再运行一次就好了。

另外，据观察，报备时的时间栏网站会直接读取设备的时间，如果出现设备时间慢了一天可能会出现'报备时间不合法'这种网页提示，这是把设备时间调整正常即可。

## 依赖
### python3
### selenium 包
可通过pip直接安装
```
pip install selenium
```
### pyinstaller 包
如果愿意将python脚本打包成.exe文件以方便后续每日使用，可以安装此包。（非必须）
```
pip install pyinstaller
```
### WebDriver
不同浏览器对应不同webdriver。以chrome为例，先打开 chrome设置->关于chrome 获得当前版本号，而后在镜像站`<http://npm.taobao.org/mirrors/chromedriver/>`找到对应版本的chromedriver下载，并解压

## 使用
两个.py文件均是可单独运行的，在参数输入方式上稍有不同。
### Report.py
第一次使用前，先打开文件，将个人信息部分以字符串形式填写完整，并将`<driver=webdriver.Chrome("chromedriver实际路径")>`修改为自身电脑中的.exe文件路径，并保存。
其他参数设定默认按照最基本的去物院做实验所需内容填写，如需修改，可在.py文件中自行查找对应区域修改，大部分都有注释标注。
而后每次使用即可直接运行.py文件，或者将其打包成.exe文件更方便使用。
### Report_i.py
与Report.py不同在于个人信息输入方式为每次运行时于终端中输入，而非记录到.py文件中。
相同的是在第一次运行前需要依前述修改webdriver路径并保存。
## 打包
采用pyinstaller模块对.py文件进行打包。在文件存储位置打开cmd/terminal，输入
```
pyinstaller -F Report.py
```
或
```
pyinstaller -F Report_i.py
```
进行打包.
