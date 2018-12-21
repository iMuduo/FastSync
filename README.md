# FastSync
基于事件驱动的快速同步工具
# 安装
```
    pip install git+https://github.com/iMuduo/FastSync.git@master
```
# 同步-发送端
```
    fsnd /home/work/send http://127.0.0.1:8080/home/work/receive [screte_key]
```

# 同步-接收端
```
    nohup frcv 8080 [screte_key] > 
```
