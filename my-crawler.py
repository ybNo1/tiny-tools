from bs4 import BeautifulSoup
import urllib
import requests
import shutil, os
import datetime
import threading


URL_H = "https://arxiv.org"
URL_T = "https://arxiv.org/list/{}/pastweek?skip=0&show=50"
FIELD = {
    "cs.CL": "NLP", 
    "cs.SD": "音频语音", 
    "q-fin": "量化金融", 
    "cs.AI": "人工智能", 
    "cs.LG": "机器学习",
    "cs.CV": "计算机视觉", 
    }

DATE = str(datetime.date.today())
# PATH = os.path.join('pdfs', DATE)
# if not os.path.exists(PATH):
#     os.makedirs(PATH)

def run(url="", th_name="default"):
    print("线程:{} 开始运行\n".format(th_name))
    path = os.path.join('pdfs', th_name)
    if not os.path.exists(path):
        os.makedirs(path)
    page = requests.get(url)
    # html = url.read().decode('utf-8')
    # print(page.content.decode('utf-8'))
    soup = BeautifulSoup(page.content.decode('utf-8'), 'html.parser')
    # rec_lst = soup.find('span',)
    soup = soup.find('dl')
    soup = soup.find_all('a', {"title": "Download PDF"})
    for s in soup:
        file_name = s.get('href') + ".pdf"
        link = URL_H + file_name
        print(link)
        save_path = os.path.join(path, DATE + "-" + file_name.split('/')[-1])
        print(save_path)
        if os.path.exists(save_path):
            continue
        pdf_data = requests.get(link)
        # print(type(pdf_data.content))
        with open(save_path, 'wb') as f:
            f.write(pdf_data.content)


if __name__ == "__main__":
    # print(URL.format(FIELD[1]))
    print("开始下载日期为: {} 的arxiv文章\n".format(DATE))
    th_lst = []
    for i, th_name in FIELD.items():
        url = URL_T.format(i)
        th = threading.Thread(target=run, args=[url, th_name])
        th.start()
        th_lst.append(th)
    for i in th_lst:
        i.join()
    print("所有日期为: {} 的文章下载完毕".format(DATE))