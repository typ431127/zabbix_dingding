### 环境要求

#### python2.x python3.x zabbix 2.x 版本以上 dingding
##### 我刚刚学习python没多久，写的不是很好大神勿喷 😶😶😶
### 个人博客
https://www.aityp.com

---
### 效果图🐐

![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/1.png)

### 版本选择
|文件|说明
|---|---|
|zabbix_dingding.py| 机器人安全配置为网段
|zabbix_dingding_sign.py|机器人安全配置为加签(推荐) 使用python3
推荐使用签名验证版本,更安全
### python配置
你的python3最好在`/usr/bin`下面，否则会找不到
```
ln -s python3 /usr/bin/python3
```
### 安装configparser requests模块(需要PIP没有可以看下面安装)
```
#python2.x
pip install configparser
pip install requests

#python3.x
pip3 install configparser
pip3 install requests
```
### 安装pip
```
cd pip_install
python get-pip.py
```
### 钉钉配置
需要新建一个钉钉群，群里面添加一个机器人即可。
#### 点击加入一个机器人
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/11.png)

#### 添加自定义机器人
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/3.png)
#### 设置机器人,记住`webhook`后面会用到
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/4.png)
#### webhook后面配置文件会用到! ! ! 安全配置选择加签
![](https://ddn-md.oss-cn-beijing.aliyuncs.com/images/md/2019/12/27/20191227163140.png)
----

#### pull代码
```
git clone git@github.com:typ431127/zabbix_dingding.git
```

#### 配置报警配置文件
```
cd zabbix_dingding
mkdir -p /etc/zabbix/
mv dingding.conf /etc/zabbix/
```
#### 编辑配置文件
`/etc/zabbix/dingding.conf`
![](https://ddn-md.oss-cn-beijing.aliyuncs.com/images/md/2019/12/27/20191227165920.png)
```
[config]
#此文件注意权限
log_dir=/data/logs/zabbix/
log_file=zabbix_dingding.log
#配置图片实例,https://img.alicdn.com/top/i1/LB1lIUlPFXXXXbGXFXXXXXXXXXX
webhook=https://oapi.dingtalk.com/robot/send?access_token=
secret=
```
- `webhook`是你新建机器人webhook，复制粘贴即可,这一步很重要.
- `secret`是安全设置里面加签的key,复制粘贴即可

#### 配置报警脚本
把`zabbix_dingding.py`放到你`zabbix_server`的`scripts`目录下面即可.

#### 配置权限
```
chown zabbix:zabbix zabbix_dingding.py
chmod +x zabbix_dingding.py
touch /tmp/zabbix_dingding.log
chown zabbix:zabbix /tmp/zabbix_dingding.log
```

### zabbix web配置
`管理`---`报警媒介类型`---`创建媒体类型`   
**配置如下**
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/6.png)
#### 用户添加报警媒介---`添加`
![image](http://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/7.png)

**收件人是你的钉钉手机号**
![image](http://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/8.png)
**动作配置**
![image](http://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/9.png)

### 手动触发报警
![image](http://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/10.png)

### 日志调试
```
cat /data/logs/zabbix/zabbix_dingding.log
```
![](https://ddn-md.oss-cn-beijing.aliyuncs.com/images/md/2019/12/27/20191227170123.png)
图中所示错误为签名验证key错误,这个时候自行检查dingding.conf中secret配置是否与钉钉机器人中的key一样。

### QQ:1500698928
### 个人微信
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/14.jpg?x-oss-process=image/resize,h_600)

### 问题调试方法
如果你的钉钉收不到消息可以使用以下方法进行调试
命令行调试脚本
```
python3 zabbix_dingding.py 1 2 3
```
