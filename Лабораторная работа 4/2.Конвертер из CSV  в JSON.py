# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(INPUT_FILENAME, OUTPUT_FILENAME) -> None:
    with open(INPUT_FILENAME) as f:
        dict_ = [line for line in csv.DictReader(f)]

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(dict_, f, indent=4)

    ...  # TODO считать содержимое csv файла


    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
