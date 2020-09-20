import MeCab

wakati = MeCab.Tagger("-Owakati")
yomi = MeCab.Tagger("-Oyomi")
text = "一週間ばかり、ニューヨークを取材した。"

wakati_list = wakati.parse(text).split()
yomi_list = []
for each_wakati in wakati_list:
    yomi_list.append(yomi.parse(each_wakati))
