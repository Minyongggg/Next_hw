import requests
from bs4 import BeautifulSoup
import csv
from movie import movie_crawling

#영화 사이트 url
MOVIE_URL = f"https://movie.naver.com/movie/running/current.nhn"
movie_get = requests.get(MOVIE_URL)
movie_html = BeautifulSoup(movie_get.text, "html.parser")

#영화 제목, 평점, 이미지 주소, 감독, 출연자, 개봉일자

movie_wrap = movie_html.find('ul', {'class':'lst_detail_t1'})
movie_list = movie_wrap.find_all('li')

final_result = movie_crawling(movie_list)


file = open('movie.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["영화 제목", "영화 평점", "이미지 주소", "감독", "출연자", "개봉일자"])

for result in final_result:
    row = []
    row.append(result["title"])
    row.append(result["star"])
    row.append(result["img_url"])
    row.append(result["director"])
    row.append(result["actors"])
    row.append(result["opening"])
    writer.writerow(row)
