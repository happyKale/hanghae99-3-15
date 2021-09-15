# 테스트 데이터 넣기(최초 1번만 실행)
# 프로젝트 완성 시 파일 삭제

# MongoDB에 insert 하기
from pymongo import MongoClient # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbweek1                      # 'dbsparta'라는 이름의 db를 만듭니다.


# 'volunteer'라는 collection에 넣습니다.
datas = [
    {
        'volunteer_no': '2756111',
        'subject': '2021년 전통 성년식 참여자 모집 (남성 3명)',
        'recruit_period': '2021-08-12 ~ 2021-09-17',
        'completion': 'false',
        'hour': '2:00:00',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2756111'
    },
    {
        'volunteer_no': '2786471',
        'subject': '초등학교 아동수학 학습지도',
        'recruit_period': '2021-08-12 ~ 2021-09-17',
        'completion': 'false',
        'hour': '3:00:00',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2756111'
    },
    {
        'volunteer_no': '2722261',
        'subject': '(부평역 오전근무)인천 수돗물 명칭변경 시민 선호도 현장투표소 지원 자원봉사',
        'recruit_period': '2021-06-10 ~ 2021-09-04',
        'completion': 'false',
        'hour': '5:00:00',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2756111'
    },
    {
        'volunteer_no': '2768851',
        'subject': '(검암역 오후근무)인천 수돗물 명칭변경 시민 선호도 현장투표소 지원 자원봉사',
        'recruit_period': '2021-07-29 ~ 2021-09-17',
        'completion': 'false',
        'hour': '5:00:00',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2756111'
    },
    {
        'volunteer_no': '2751221',
        'subject': '우리 함께 플로깅 자원봉사활동',
        'recruit_period': '2021-08-22 ~ 2021-09-30',
        'completion': 'false',
        'hour': '4:00:00',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2756111'
    },
    {
        'volunteer_no': '2756241',
        'subject': '송도5동 행정복지센터 발열체크 지원 (14:00~18:00)',
        'recruit_period': '2021-09-16 ~ 2021-09-27',
        'completion': 'false',
        'hour': '7:00:00',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2756111'
    },
    {
        'volunteer_no': '2765997',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2765997',
        'subject': '토탈 자원봉사의 날 - 소상공인을 위한 착한소비 및 재난 약자를 위한 "연수사랑"키트 전달 행사지원 활동',
        'hour': '2:00:00',
        'recruit_period': '2021-09-13 ~ 2021-09-24',
        'completion': 'false'
    },
    {
        'volunteer_no': '2764359',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2764359',
        'subject': '초등학교 아동수학 학습지도',
        'hour': '1:00:00',
        'recruit_period': '2021-09-07 ~ 2021-09-24',
        'completion': 'false'
    },
    {
        'volunteer_no': '2766056',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2766056',
        'subject': '(검암역 오전근무)인천 수돗물 명칭변경 시민 선호도 현장투표소 지원 자원봉사',
        'hour': '3:00:00',
        'recruit_period': '2021-09-13 ~ 2021-09-28',
        'completion': 'false'
    },
    {
        'volunteer_no': '2764364',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2764364',
        'subject': '초등학교 아동과학 실험 진행 및 지도',
        'hour': '1:00:00',
        'recruit_period': '2021-09-07 ~ 2021-09-24',
        'completion': 'false'
    },
    {
        'volunteer_no': '2766069',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2766069',
        'subject': '(석남역 오후근무)인천 수돗물 명칭변경 시민 선호도 현장투표소 지원 자원봉사',
        'hour': '3:00:00',
        'recruit_period': '2021-09-13 ~ 2021-09-28',
        'completion': 'false'
    },
    {
        'volunteer_no': '2763930',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2763930',
        'subject': '아름다운가게 연수구청점-910 월 대학생 자원봉사자 모집 (8번이상 봉사가능한 분)',
        'hour': '8:00:00',
        'recruit_period': '2021-09-06 ~ 2021-09-30',
        'completion': 'false'
    },
    {
        'volunteer_no': '2755470',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2755470',
        'subject': '우리 함께 플로깅 자원봉사활동',
        'hour': '23:50:00',
        'recruit_period': '2021-08-05 ~ 2021-09-30',
        'completion': 'false'
    },
    {
        'volunteer_no': '2765619',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2765619',
        'subject': '한글 교실 자원봉사자 모집',
        'hour': '1:00:00',
        'recruit_period': '2021-09-10 ~ 2021-10-10',
        'completion': 'false'
    },
    {
        'volunteer_no': '2755067',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2755067',
        'subject': '외국어회화동아리 진행 멘토 모집 (재능기부)',
        'hour': '2:00:00',
        'recruit_period': '2021-08-04 ~ 2021-11-04',
        'completion': 'false'
    },
    {
        'volunteer_no': '2752815',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2752815',
        'subject': '인천시 자원봉사 홍보봉사자 자원봉사활동(비대면자원봉사)',
        'hour': '23:50:00',
        'recruit_period': '2021-08-01 ~ 2021-10-31',
        'completion': 'false'
    },
    {
        'volunteer_no': '2743330',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2743330',
        'subject': '사랑의 도시락 세척 자원봉사 활동',
        'hour': '2:00:00',
        'recruit_period': '2021-06-29 ~ 2021-11-30',
        'completion': 'false'
    },
    {
        'volunteer_no': '2766066',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2766066',
        'subject': '(석남역 오전근무)인천 수돗물 명칭변경 시민 선호도 현장투표소 지원 자원봉사',
        'hour': '3:00:00',
        'recruit_period': '2021-09-13 ~ 2021-09-28',
        'completion': 'false'
    },
    {
        'volunteer_no': '2762417',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2762417',
        'subject': '송도3동 행정복지센터 상생국민지원금 업무보조(14시~18시)',
        'hour': '4:00:00',
        'recruit_period': '2021-08-31 ~ 2021-09-30',
        'completion': 'false'
    },
    {
        'volunteer_no': '2763298',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2763298',
        'subject': '2021년 연수2동 지역사회보장협의체 찬나눔정나눔 밑반찬 지원',
        'hour': '2:00:00',
        'recruit_period': '2021-09-02 ~ 2021-09-30',
        'completion': 'false'
    },
    {
        'volunteer_no': '2756111',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2756111',
        'subject': '2021년 전통 성년식 참여자 모집 (남성 3명)',
        'hour': '7:00:00',
        'recruit_period': '2021-08-12 ~ 2021-10-25',
        'completion': 'false'
    },
    {
        'volunteer_no': '2755217',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2755217',
        'subject': '인천 연수구 둘레길 환경정화(쓰레기줍기)활동',
        'hour': '2:00:00',
        'recruit_period': '2021-08-04 ~ 2021-11-04',
        'completion': 'false'
    },
    {
        'volunteer_no': '2761796',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2761796',
        'subject': '송도 임시선별진료소 질서유지 봉사활동 (오후)',
        'hour': '2:00:00',
        'recruit_period': '2021-08-30 ~ 2021-11-30',
        'completion': 'false'
    },
    {
        'volunteer_no': '2766058',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2766058',
        'subject': '(검암역 오후근무)인천 수돗물 명칭변경 시민 선호도 현장투표소 지원 자원봉사',
        'hour': '3:00:00',
        'recruit_period': '2021-09-13 ~ 2021-09-28',
        'completion': 'false'
    },
    {
        'volunteer_no': '2761798',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2761798',
        'subject': '송도 임시선별진료소 질서유지 봉사활동 (오전)',
        'hour': '2:00:00',
        'recruit_period': '2021-08-30 ~ 2021-11-30',
        'completion': 'false'
    },
    {
        'volunteer_no': '2743367',
        'href': 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do?type=show&progrmRegistNo=2743367',
        'subject': '사랑의 도시락 세척자원봉사자 모집',
        'hour': '2:00:00',
        'recruit_period': '2021-06-29 ~ 2022-01-18',
        'completion': 'false'
    }
]

for data in datas:
    print("insert volunteer_no : " + data["volunteer_no"])
    db.volunteer.insert_one(data)