from csv import reader
import Utility

# Load a CSV file
def load_csv(filename):
    file = open(filename, "r+")
    lines = reader(file)
    dataset = list(lines)    
    return dataset




def analyse(dataset, query):
    value = list()
    for line in dataset:
        if query[1] != -1 and line[0] == query[0] and line[1] == query[1]:
            value.append(line)
        if line[0] == query[0] and query[1] == -1:
            value.append(line)
        if line[0] > query[0]:
            break
    # print(value)
    return value


def takeQuery(dataset, queryLine):
    prediction = list()
    # query = input("Write if you have any Query:\n")
    queryLine = queryLine.strip().upper().split(",")    

    # print(queryLine)
    reply = "[  " + queryLine[0] + " BLOOD GROUP  ]" + "\n\n"
    for line in dataset:
        if line[0] == queryLine[0]:
            reply = reply + line[1] +" ("+ line[2] +") : " + line[3] + "\n"
    # print('\n')
    # print(reply)
    return reply


def main():
    # seed(1)
    filename = '../input/Blood_Group_BSSE09.txt'
    dataset = load_csv(filename)
    # print(dataset)
    # print("\n", dataset[0])
    # convert string attributes to integers
    # evaluate_algorithm(dataset, decision_tree)
    # reply = takeQuery(dataset)
    return dataset



if __name__ == "__main__":
    dataset = main()
