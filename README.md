# Video-Compression-Tool
通过压缩视频质量使其可以在一些糟糕的硬件上正常播放而不卡顿，具体原理是将视频压缩至1920*1080分辨率，23.98fps从而降低其码率。

## 安装与使用
### 安装项目
1、克隆仓库
```
git clone https://github.com/BubbleSothoth/Video-Compression-Tool
```
2、确认自己安装了ffmpeg，安装链接如下：
```
https://ffmpeg.org/download.html
```
3、将ffmpeg添加至环境变量
4、运行“视频压缩工具.py”
```
视频压缩工具.py -i InputFile -o OutputFile
```
### 使用说明
```
视频压缩工具.py -i InputVideo -o OutputVideo"
-i InputVideo:  导入视频文件
-o OutputVideo: 输出视频文件
```

## 运行环境
### 解释器
Python 3.10.5及以上
### OS
Windows10及以上
