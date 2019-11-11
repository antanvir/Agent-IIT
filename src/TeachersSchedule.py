from csv import reader
import Utility

# Load a CSV file
def load_csv(filename):
    file = open(filename, "r+")
    lines = reader(file)
    dataset = list(lines)
    return dataset


# Convert string column to float
def str_column_to_int(dataset, column):
    for row in dataset:
        if column != len(dataset[0]) - 1:
            row[column] = int(row[column].strip())


def analyse(dataset, query):
    value = list()
    for line in dataset:
        if line[0] == query[0] and line[1] == query[1]:
            value.append(line)
        if line[0] > query[0]:
            break
    # print(value)
    return value


def takeQuery(dataset, queryLine):
    prediction = list()
    # query = input("Write if you have any Query:\n")
    queryLine = queryLine.strip().split(",")
    for i in range(len(queryLine)):
        if i != 2:
            queryLine[i] = int(queryLine[i])

    # queryLine = [int(x) for x in queryLine]
    # global tree, isFinished
    # isFinished = [False for x in queryLine]
    if len(queryLine) == 1:
        queryLine.append(0)
        for i in range(0, 5):
            queryLine[1] = i
            # print(queryLine)
            # result = analyse(dataset, queryLine)
            # if result:
            prediction.extend(analyse(dataset, queryLine))
    else:
        prediction = analyse(dataset, queryLine)

    if len(queryLine) == 3:
        found = False
        for row in prediction:
            if row:
                course = row[2].split("|")
                # print(course)
                if course[0].strip() == queryLine[2].strip():
                    found = True
                    reply = "Yes.\n"
                    reply = reply + Utility.days[row[1]] + " : " + course[0].strip() + " (" + course[1].strip() + ")" + "\n"
        if found == False:
            reply = "No\n"

    else:
        reply = ""
        for row in prediction:
            if row:
                course = row[2].split("|")
                # print(course)
                # for i in range(0, len(course)):
                reply = reply + Utility.days[row[1]] + " : " + course[0].strip() + " (" + course[1].strip() + ")" + "\n"

    # print('\n')
    # print(reply)
    return reply


def main():
    # seed(1)
    filename = '../input/Teachers_Class_Schedule.txt'
    dataset = load_csv(filename)
    # print(dataset)
    # print("\n", dataset[0])
    # convert string attributes to integers
    for i in range(len(dataset[0]) - 1):
        str_column_to_int(dataset, i)
    # evaluate_algorithm(dataset, decision_tree)
    # reply = takeQuery(dataset)
    return dataset


if __name__ == "__main__":
    dataset = main()
