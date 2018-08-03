#coding:utf-8
__author__ = 'hang'
 
import warnings
warnings.filterwarnings("ignore")
import jieba    #�ִʰ�
import numpy    #numpy�����
import codecs   #codecs�ṩ��open������ָ���򿪵��ļ������Ա��룬�����ڶ�ȡ��ʱ���Զ�ת��Ϊ�ڲ�unicode 
import re
import pandas as pd  
import matplotlib.pyplot as plt
from urllib import request
from bs4 import BeautifulSoup as bs
%matplotlib inline
 
import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud#���ư�
 
#������ҳ����
def getNowPlayingMovie_list():   
    resp = request.urlopen('https://movie.douban.com/nowplaying/hangzhou/')        
    html_data = resp.read().decode('utf-8')    
    soup = bs(html_data, 'html.parser')    
    nowplaying_movie = soup.find_all('div', id='nowplaying')        
    nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')    
    nowplaying_list = []    
    for item in nowplaying_movie_list:        
        nowplaying_dict = {}        
        nowplaying_dict['id'] = item['data-subject']       
        for tag_img_item in item.find_all('img'):            
            nowplaying_dict['name'] = tag_img_item['alt']            
            nowplaying_list.append(nowplaying_dict)    
    return nowplaying_list
 
#��ȡ���ۺ���
def getCommentsById(movieId, pageNum): 
    eachCommentList = []; 
    if pageNum>0: 
         start = (pageNum-1) * 20 
    else: 
        return False 
    requrl = 'https://movie.douban.com/subject/' + movieId + '/comments' +'?' +'start=' + str(start) + '&limit=20' 
    print(requrl)
    resp = request.urlopen(requrl) 
    html_data = resp.read().decode('utf-8') 
    soup = bs(html_data, 'html.parser') 
    comment_div_lits = soup.find_all('div', class_='comment') 
    for item in comment_div_lits: 
        if item.find_all('p')[0].string is not None:     
            eachCommentList.append(item.find_all('p')[0].string)
    return eachCommentList
 
def main():
    #ѭ����ȡ��һ����Ӱ��ǰ10ҳ����
    commentList = []
    NowPlayingMovie_list = getNowPlayingMovie_list()
    for i in range(10):    
        num = i + 1 
        commentList_temp = getCommentsById(NowPlayingMovie_list[0]['id'], num)
        commentList.append(commentList_temp)
 
    #���б��е�����ת��Ϊ�ַ���
    comments = ''
    for k in range(len(commentList)):
        comments = comments + (str(commentList[k])).strip()
 
    #ʹ��������ʽȥ��������
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)
    cleaned_comments = ''.join(filterdata)
 
    #ʹ�ý�ͷִʽ������ķִ�
    segment = jieba.lcut(cleaned_comments)
    words_df=pd.DataFrame({'segment':segment})
 
    #ȥ��ͣ�ô�
    stopwords=pd.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')#quoting=3ȫ������
    words_df=words_df[~words_df.segment.isin(stopwords.stopword)]
 
    #ͳ�ƴ�Ƶ
    words_stat=words_df.groupby(by=['segment'])['segment'].agg({"����":numpy.size})
    words_stat=words_stat.reset_index().sort_values(by=["����"],ascending=False)
 
    #�ô��ƽ�����ʾ
    wordcloud=WordCloud(font_path="simhei.ttf",background_color="white",max_font_size=80)
    word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}
 
    word_frequence_list = []
    for key in word_frequence:
        temp = (key,word_frequence[key])
        word_frequence_list.append(temp)
 
    wordcloud=wordcloud.fit_words(word_frequence_list)
    plt.imshow(wordcloud)
 
#������
main()