# 图书馆预约工具

## 简介 
一个简单的用来预约图书馆座位的工具。

## 使用

### Windows用户
已打包成exe，直接双击打开即可。（打开速度可能比较慢，请耐心等待）
查看[最新版本](https://github.com/nailu0/LibraryReservation/releases)

### 命令行使用
```
python3 src/run.py
```

## 自行打包
```
pyinstaller -F -w gui.py -p checker.py -p helper.py -p loginer.py -p reserver.py -p seatgetter.py --hidden-import Helper --hidden-import Loginer --hidden-import SeatGetter
```
