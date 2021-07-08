#Задача № 3
import requests

url_1 = 'https://api.stackexchange.com/2.3/questions?' \
        'fromdate=1625529600&todate=1625702400&order=desc&sort=activity&tagged=python&site=stackoverflow&filter=!)riR7Z9)aTchGocSVE-j'

class PythonQuestions:
    def __init__(self):
        pass

    def get_data(self, url):
        res = requests.get(url)
        n = 0
        for r in res.json()['items']:
            n += 1
            print(f"ЗАГОЛОВОК_{n} --- {r['title']}")
            print('='*80)
            print(f"ТЭГИ --- {r['tags']} ||| id_вопроса {r['question_id']}")
            print('=' * 80)
            print(f"LINK --- {r['link']}")
            print('=' * 80)
            print(f"ВОПРОС_{n} --- {r['body']}")
            print('='*180)
        print(f'Всего {n} вопросов за 2 дня')

pq = PythonQuestions()
pq.get_data(url_1)