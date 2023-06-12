from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import os
from collections import Counter

plt.rcParams['font.family'] = 'Malgun Gothic'

def show_data(categories,id):
    p = []
    for row in categories:
        if row is not None:
            category_name = row.replace("/", "")  # Remove special characters
            p.append(category_name)
        else:
            p.append(None)

    # 카테고리 별 개수를 세기 위해 Counter 객체 생성
    category_counter = Counter(p)

    # 그래프 생성을 위한 데이터
    labels = []
    sizes = []
    for category, count in category_counter.items():
        labels.append(category)
        sizes.append(count)

    # 그래프 생성
    plt.title("{}님의 책 대출 현황".format(id))
    plt.pie(sizes, labels=labels, autopct='%.2f')

    # 사용자별 데이터 저장 폴더 생성
    data_folder = os.path.join(os.getcwd(), 'static/show_data')  # 데이터 폴더 경로 생성
    os.makedirs(data_folder, exist_ok=True)  # 데이터 폴더 생성

    #아이디를 받아와야함
    tag = '.png'
    filename =  f"{id}{tag}"
    
    # 이미지 파일 저장 경로 생성
    save_path = os.path.join(data_folder, filename)

    # 그래프를 이미지 파일로 저장
    plt.savefig(save_path)