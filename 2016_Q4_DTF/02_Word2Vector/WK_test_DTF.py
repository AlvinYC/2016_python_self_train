#encoding=utf-8
import gensim
import codecs
model=gensim.models.Word2Vec.load_word2vec_format('mobile01_ptt.bin',binary=True)#mobile01+ptt model
#model=gensim.models.Word2Vec.load_word2vec_format('mobile01.bin',binary=True)#mobile01 model
#model=gensim.models.Word2Vec.load_word2vec_format('res_article.bin',binary=True)#PTT model


#####for DTF 130 sentence test#######
inputFile=codecs.open("test_sentence_after_cut.txt", "r", "utf-8")
output=codecs.open("result_dtf_mobile01_ptt.txt", "w", "utf-8")
for line in inputFile:
    data_array=line.strip().split(',')
    output.write(line)
    for i in data_array:
        try:
            s=model.most_similar(i)
            output.write('##'+i+'##'+'\n')
            for item in s:
                #output.write('##'+data_array[i]+'##'+'\n')
                output.write(item[0]+'\n')
        except:
            output.write('##'+i+'not in vector'+'##'+'\n')     
    output.write('#########################################'+'\n')
"""           

#####To find similar word#####   
out_similar=codecs.open("similar_words.txt", "w", "utf-8")    
a=u'餐廳'#enter word here
s=model.most_similar(a)
out_similar.write('##'+a+'##'+'\n')
for item in s:
    print item[0],item[1]
    out_similar.write(item[0]+'\n')
"""
