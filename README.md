# ImageProfileCropper 自動頭像剪輯
偵測照片中的一個人臉並裁剪成方形的頭像。

![](https://github.com/baby03201/ImageProfileCropper/blob/master/cropSample.png?raw=true)

## Installation

### Requirements

  * Python 3.3+ or Python 2.7
  * macOS or Linux (Windows not officially supported, but might work)

### Libraries
安裝 Pillow 、 Face_Recognition 等套件：
```bash
pip install Pillow
pip install face_recognition
```

若安裝face_recognition的時候遇到scipy問題的時候，建議可使用以下方法：
```bash
pip install --ignore-installed face_recognition
```

使用 python3 安裝
```bash
pip3 install Pillow
pip3 install face_recognition
```

### Run
先把未裁減的照片兒放到photos資料夾，然後執行以下指令：
#### Python2
```bash
python caddiePhotoCropper.py
```
#### Python3
```bash
python3 caddiePhotoCropper.py
```
