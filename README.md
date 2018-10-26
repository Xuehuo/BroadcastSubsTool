# 直播字幕生成工具
Live Broadcast SubTitle Genarate Tool

## 下载
Git
* `git clone https://github.com/Xuehuo/BroadcastSubsTool.git`

Http
* <a href='https://github.com/Xuehuo/BroadcastSubsTool/archive/master.zip'>Download</a>

## 运行环境
* python3,cv2
* `pip install opencv-python`

## 使用说明
```
python SubsTool.py -s <sourceTXT> [ -f <fontfile> ]
```
* sourceTXT (必须) : 字幕源文件
* fontfile  (可选) : 自定义字体（默认MFShangYa_Noncommercial-Regular.otf）

## 样例
```
python SubsTool.py -s Sample.txt
```

## License 
MIT
