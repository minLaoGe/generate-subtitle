# 万国语言字幕提取

## 目的
使用AI工具从视频文件中提取srt格式字幕，解放双手，避免重复劳动。

## 项目示范

youtube原视频链接如下：  https://www.youtube.com/watch?v=3eytpBOkOFA

采集之后的视频链接为： https://www.bilibili.com/video/BV1cj411C7dx/

## 参数说明
在`main.py`中有一下参数供调整： 

需要提取字幕的目标语言，比如原字幕是日文，想要他翻译成中文那么就配置为
> object_subtitle = '中文' 
> language = 'Japanese'

OpenAI官网的Open_key(一定要配置的):
> openai_key = 'sk-xxxxxxxxxxxx'



## 技术架构
使用Open-whisper进行语言识别，保存为原字幕文件之后，再使用ChatGPT进行翻译。


## whisper模型和语言选择

### 模型选择

[点我查看OpenAI官网说明](https://github.com/openai/whisper/blob/main/README.md?plain=1)

There are five model sizes, four with English-only versions, offering speed and accuracy tradeoffs. Below are the names of the available models and their approximate memory requirements and relative speed. 

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |


### 支持的语言

分数越高，代表识别的精度越低

![WER breakdown by language](https://raw.githubusercontent.com/openai/whisper/main/language-breakdown.svg)
