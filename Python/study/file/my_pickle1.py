# pickle.dump()를 사용하여 해당 내용을 my_pickle1.pickle 파일에 입출력
import pickle

files = "Data/my_pickle1.pickle"
text_list= [
    {'greg': 95},
    {'john': 25},
    {'yang': 50},
    {'timothy': 15},
    {'melisa': 100},
    {'thor': 10},
    {'elen': 25},
    {'mark': 80},
    {'steve': 95},
    {'anna': 20},
]

with open(files, 'wb') as file:
    for data in text_list:
        pickle.dump(data, file)

# pickle.load()를 사용하여 파일 전체 내용 로드
with open(files, 'rb') as file:
    data_list = []
    while True:
        try:
            data = pickle.load(file)
        except EOFError:
            break
        data_list.append(data)

print(data_list)