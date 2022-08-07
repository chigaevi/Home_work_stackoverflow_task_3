import requests
from pprint import pprint

def get_questions(todate = 1659916800, max = 1659744000,tagged = 'python'):
    # На stackoverflow даты в параметрах указаны в неявном виде, поэтом значения todate и max получил на странице
    # https://api.stackexchange.com/docs/questions  Однако Я не уверен, что эти даты верны!

    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'todate': todate, 'max': max, 'tagged': tagged, 'site': 'stackoverflow', 'sort': 'activity'}
    response = requests.get(url, params=params)
    # pprint(response.json())
    questions = response.json()['items']
    for question in questions:
        display_name = question['owner']['display_name']
        question = question['title']
        result = f'{display_name} --> {question}'
        print(result)

if __name__ == '__main__':
    get_questions()


