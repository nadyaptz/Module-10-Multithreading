import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        all_data.extend(lines)


file_names = [f'./file{number}.txt' for number in range(1, 5)]
# линейный
# start = datetime.datetime.now()
# for i in range(len(file_names)):
#     read_info(file_names[i])
# end = datetime.datetime.now()
# print(end - start)
# 0:00:04.669687

# мультипроцессорный
#
if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(4) as pool:
        pool.map(read_info, file_names)

    end = datetime.datetime.now()
    print(end - start)
# 0:00:02.710779