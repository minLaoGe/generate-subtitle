# Multilingual Subtitle Extraction
<a href='/README_ZH.md'>中文文档 </a>
## Objective
Use AI tools to extract srt format subtitles from video files, freeing up hands and avoiding repetitive labor.

## Project Demonstration

The original YouTube video link is as follows: https://www.youtube.com/watch?v=3eytpBOkOFA

The link to the video after collection is: https://www.bilibili.com/video/BV1cj411C7dx/

## Parameter Description
In `main.py` there are parameters available for adjustment:

Target language for subtitle extraction. For example, if the original subtitle is in Japanese and you want it translated to Chinese, then set it as
> object_subtitle = 'Chinese'
>
> language = 'Japanese'

OpenAI official website's Open_key (essential to configure):
> openai_key = 'sk-xxxxxxxxxxxx'

## Technical Architecture
Use Open-whisper for language recognition, save it as the original subtitle file, and then use ChatGPT for translation.

## Whisper Model and Language Selection

### Model Selection

[Click here to view the OpenAI official description](https://github.com/openai/whisper/blob/main/README.md?plain=1)

There are five model sizes, four with English-only versions, offering speed and accuracy tradeoffs. Below are the names of the available models and their approximate memory requirements and relative speed.

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |

### Supported Languages

A higher score indicates lower recognition accuracy.

![WER breakdown by language](https://raw.githubusercontent.com/openai/whisper/main/language-breakdown.svg)
