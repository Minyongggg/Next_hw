def movie_crawling(movie_list):
    final_result = []
    for i in range(len(movie_list)):
        title = movie_list[i].find('dt', {'class':'tit'}).find('a').text
        star = movie_list[i].find('div', {'class':'star_t1'}).find('span', {'class':'num'}).text
        img_url = movie_list[i].find('img')['src']
        
        temp1 = movie_list[i].find('dl', {'class':'info_txt1'}).find_all('span', {'class':'link_txt'})
        directors = temp1[1].find_all('a')
        for j in range(len(directors)):
            directors[j] = directors[j].text

        if len(temp1) == 3:
            actors = temp1[2].find_all('a')
            for j in range(len(actors)):
                actors[j] = actors[j].text
        else:
            actors = [] #출연자가 적혀있지 않은 경우
        
        temp2 = movie_list[i].find('dl', {'class':'info_txt1'}).find('dd').text
        opening = temp2.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')[-12:-2]

        result = {
            'title' : title,
            'star' : star,
            'img_url' : img_url,
            'director' : directors, #list
            'actors' : actors, #list
            'opening' : opening
        }
        final_result.append(result)

    return final_result