### 环境要求

#### python2.x python3.x zabbix 2.x 版本以上 dingding
##### 我刚刚学习python没多久，写的不是很好大神勿喷 😶😶😶
### 个人博客
https://www.aityp.com

---
### 效果图🐐

![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/1.png)

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
#### 设置好后记住`webhook`后面会用到
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/4.png)
#### 记住webhook后面配置文件会用到! ! !
----
### zabbix配置

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
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/5.png)
```
[config]
#此文件注意权限
log=/tmp/zabbix_dingding.log
#配置图片实例,https://img.alicdn.com/top/i1/LB1lIUlPFXXXXbGXFXXXXXXXXXX
webhook=https://oapi.dingtalk.com/robot/send?access_token=
```
>log目录不用动,webhook是你新建机器人的url，复制粘贴即可,这一步很重要.

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
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/13.png)
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/29/14.png)
### 可以根据错误码解决问题,错误码说明
[错误码查询传送门](https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7386797.0.0.qt4Lrj&source=search&treeId=385&articleId=104965&docType=1)


### QQ:1500698928
### 个人微信
![image](https://typ.oss-cn-shanghai.aliyuncs.com/markdown/2017/10/14.jpg?x-oss-process=image/resize,h_600)

### 问题调试方法
如果你的微信收不到消息可以使用以下方法进行调试
命令行调试脚本
```
python3 zabbix_dingding.py 1 2 3
```
