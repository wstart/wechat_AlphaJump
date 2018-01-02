## 简介
wechat_AlphaJump 是借助于微信小游戏 跳一跳
用于机器学习训练和研究实用，请勿作非法用途

## 环境
- 安卓 屏幕 1920*1080
- adb
- python 3（理论上2也行 只要装了PIl）
	- PIL

## 使用介绍

- 安卓机插入电脑 adb devices 查看是否有设备
- 运行 adb shell screencap -p /sdcard/screenshot.png
- 运行  adb pull /sdcard/screenshot.png ./screenshot.png
- 查看当前目录是否有屏幕截图
- 打开微信跳一跳界面
- 运行 pyhton main.py 即可

