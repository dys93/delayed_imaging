# 项目内容
这是一个使用python2.7 opencv的延迟摄影项目.
项目中使用了树莓派raspbian作为开发平台,顺便测试了下树莓派的效果.
后期的修正处理用的是ubuntu 14.04
直接生成的avi视频文件过大,所以没有上传.
使用了两个摄像机,因为彩色受到光照的影响,晚上的情况无法记录,所以之后的视频使用的是自带特殊光源摄像头拍摄的结果

## 摄像机获取结果
<img alt="西红柿植株" src="https://github.com/dys93/delayed_imaging/blob/master/frame/00000360.jpg" width="30%" height="30%">

## 制作的gif文件
<img alt="gif" src="https://github.com/dys93/delayed_imaging/blob/master/big.gif" width="50%" height="50%">

## github的markdown暂时不支持mp4文件播放
continue
## 文件结构
* camera.py -- 定时摄像机,拍摄图片并录制视频
* clean_video.py -- 清洗数据,删除无效的视频帧,拼接成新的avi文件,在转成mp4文件(才能上传微信)
* frame -- 文件夹 保存视频转换过程中生成的视频帧
* lapse -- 文件夹 保存camera捕捉到的图像
* video -- 文件夹 保存视频






