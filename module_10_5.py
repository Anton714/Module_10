from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, encoding="utf-8") as file:
        while file.readline():
            all_data.append(file.readline())


file_names = []
for i in range(1, 5):
    file_names.append(f'./file {i}.txt')

if __name__ == "__main__":

    start_line = datetime.now()

    for file_name in file_names:
        read_info(file_name)

    end_line = datetime.now()
    print(end_line - start_line, '- линейный')

    start_multi = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    end_multi = datetime.now()
    print(end_multi - start_multi, '- многопроцессный')
