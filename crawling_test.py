# 프로젝트 완성 시 파일 삭제

import requests
from bs4 import BeautifulSoup
import math
import datetime as dt
from multiprocessing import Pool

# 인천광역시(searchHopeArea1=6280000) 연수구(searchHopeArea2=3520000) 선택 / cPage는 페이지 관련 데이터 (ex: cPage=2는 2페이지)
data = requests.get(
    'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?searchHopeArea1=6280000&searchHopeArea2=3520000&cPage=1')
soup = BeautifulSoup(data.text, 'html.parser')

# 봉사활동 리스트 개수
page_count = int(soup.select_one("#content > div.content_view > div.search_form > div > p > em:nth-child(1)").text)
# 페이지 개수(한 페이지 당 10개 출력 시)
page_count = math.ceil(page_count / 10)

volunteers_list = []
# 각 페이지에서 가져온 데이터가 담긴 리스트를 담는 용도
lis_temp_list = []
for i in range(1, page_count + 1):
    # 인천광역시(searchHopeArea1=6280000) 연수구(searchHopeArea2=3520000) 선택 / cPage는 페이지 관련 데이터 (ex: cPage=2는 2페이지)
    data = requests.get(
        'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?searchHopeArea1=6280000&searchHopeArea2=3520000&cPage=' + str(i))
    soup = BeautifulSoup(data.text, 'html.parser')
    # 현재 페이지에 있는 봉사활동 모두 가져오기
    lis = soup.select("#content > div.content_view > div.board_list.board_list2.non_sub > ul > li")
    lis_temp_list.append(lis)

# 2차원 리스트를 1차원 리스트로 바꾸기
lis_list = sum(lis_temp_list, [])

for li in lis_list:
    # 봉사번호
    volunteer_no = li.select("li > input")[0]["value"]
    # 상세 내용 페이지
    href = "https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=" + volunteer_no
    # 제목
    subject = li.select_one("a > dl > dt").text.strip()
    # 모집기간 리스트 [시작일,마감일]
    recruit_period_list = li.select_one("a > dl > dd > dl:nth-child(2) > dd").text.strip().replace("\r\n", "").replace(
        "\t", "").replace(" ", "").split("~")
    # 모집기간
    recruit_period = recruit_period_list[0] + " ~ " + recruit_period_list[1]
    # 마감일로부터 남은 기간
    before_deadline = li.select_one("a > div.close_dDay > div > span").text

    # 봉사시간 가져오기
    data1 = requests.get(href)
    soup1 = BeautifulSoup(data1.text, 'html.parser')
    # 봉사시간
    time_tag = "#content > div.content_view > div > div.board_view.type2 > div.board_data.type2 > div:nth-child(1) > dl:nth-child(2) > dd"
    time = soup1.select_one(time_tag).text.replace(" ", "").split("~")
    start_time = dt.datetime.strptime(time[0], "%H시%M분")
    end_time = dt.datetime.strptime(time[1], "%H시%M분")
    hour = str(end_time - start_time)

    volunteer_dict = {"volunteer_no": volunteer_no, "href": href, "subject": subject, "hour": hour,
                      "recruit_period": recruit_period, "before_deadline": before_deadline}
    volunteers_list.append(volunteer_dict)

print(volunteers_list)
# print(len(volunteers_list))
