from gtts import gTTS

# sample 1
tts = gTTS(text='您好，您吃早饭了吗？需要我给你推荐些吃的吗？', lang='zh-tw')
tts.save("hello.mp3")

#sample 2
with open ('news.txt', 'r', encoding="utf8") as f:
	audio = gTTS(text=f.read(), lang="zh-cn")
	audio.save("news.mp3")