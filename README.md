# AHNU图书馆预约工具

## 简介
只要作为一名爱学习的ANHUer，想必都遇到过图书馆预约不到位置的崩溃瞬间。学校的图书馆U座位十分有限，而来学习的人又是那么的多。学校用来管理座位的预约系统，一言难尽，比某些政府机构的网站还要卡顿迟缓。

**对此，我忍不了！**

因此，大一的时候我用Python简单地了写了一个抢座位的小工具，虽然比较简陋但完全可用。可惜后来因为我压根懒得再去图书馆了，这个项目便搁置了下来。

但是现在我决定继续维护完善这个小工具，让更多的同学不用再被迫食屎。

## 使用

为了使用此工具，你必须先安装Python3，并安装相关依赖。
```bash
pip3 install --user -r requirements.txt # 安装必要的依赖
```

### 命令行使用
```bash
python3 src/run.py
```

### GUI 使用
```bash
python3 src/gui.py
```

## 自行打包
```bash
cd src
pyinstaller -F -w gui.py -p helper.py -p loginer.py -p reserver.py -p seatgetter.py --hidden-import Helper --hidden-import Loginer --hidden-import SeatGetter
```
可执行文件将在`dist`目录下。

## 贡献
如果你发现本工具有任何的Bug或者有想要实现的功能，欢迎提交Issue或者PR :)
最后如果你觉得本工具有用的话，不妨点一个Star ~
