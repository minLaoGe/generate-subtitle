import whisper
from datetime import timedelta
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage



# 字幕的目标语言
object_subtitle="中文"
#openAI_key
openai_key=''


#原文本翻译路径
srtFilename = "./subtitle.srt"
# 翻译之后保存的文本路径
translation_content_filepath= './subtitle_trans.srt'

# 视频文件的语言，提高识别的准确度, 配置见Wishper 的配置，指定的话可以提高识别精度，如果源视频是多国语言，可以为空
language = 'Japanese'

# 将提取音频转换为srt字幕
def transcribe_audio_file(file_path):
    #模型精确排名： tiny < base < small <medium < large
    model = whisper.load_model("large")
    if language:
        result = model.transcribe(file_path,language=language)
    else:
        result = model.transcribe(file_path)

    segments = result['segments']
    print(segments)
    sum_text = ''
    for idx,segment in  enumerate(segments):
        # 如果当前段不是最后一个段，并且下一个段的开始时间等于当前段的结束时间
        if idx - 1 < len(segments) and idx > 0 and segments[idx - 1]['end'] == segment['start']:
            startTime = str(0) + str(timedelta(seconds=int(segment['start']))) + ',100'
        else:
            startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'

        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"
        sum_text = sum_text+segment


    with open(srtFilename, 'a', encoding='utf-8') as srtFile:
       srtFile.write(sum_text)
    chat_model = ChatOpenAI(openai_api_key=openai_key)
    chat_model.model_name='gpt-3.5-turbo-16k'
    temp = f"""下面我让你来充当翻译家,你的目标是把任何语言翻译成{object_subtitle},请翻译时不要带翻译腔，而是要翻译得自然、流畅和地道，使用优美和高雅的表达方式。并且保留时间线,下面保留时间线开始翻译成{object_subtitle}:'{sum_text}'"""
    print(temp)
    messages = [HumanMessage(content=temp)]
    result = chat_model(messages).content
    with open(translation_content_filepath, 'a', encoding='utf-8') as srtFile2:
       srtFile2.write(result)




# 调用函数
transcribe_audio_file("/Users/minfengyu/Movies/Mac Video Library/YOASOBI「祝福」Official Music Video (『機動戦士ガンダム 水星の魔女』オープニングテーマ).mp4")
