# CART on the Bank Note dataset
from random import seed
from random import randrange
from csv import reader
import Utility


# global tree
global isFinished
global queryDone


# Load a CSV file
def load_csv(filename):
    file = open(filename, "r+")
    lines = reader(file)
    dataset = list(lines)
    return dataset


# Convert string column to float
def str_column_to_int(dataset, column):
    for row in dataset:
        if column != len(dataset[0])-1:
            row[column] = int(row[column].strip())




def evaluate_algorithm(dataset, decision_tree):
    tree = decision_tree(dataset)
    return tree



# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right


# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
    # count all samples at split point
    n_instances = float(sum([len(group) for group in groups]))
    # sum weighted Gini index for each group
    gini = 0.0
    for group in groups:
        size = float(len(group))
        # avoid divide by zero
        if size == 0:
            continue
        score = 0.0
        # score the group based on the score for each class
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        # weight the group score by its relative size
        gini += (1.0 - score) * (size / n_instances)
    return gini



# Select the best split point for a dataset
def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    for index in range(len(dataset[0]) - 1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    return {'index': b_index, 'value': b_value, 'groups': b_groups}



def split(node, depth):
    leftBlank = False
    rightBlank = False
    left, right = node['groups']
    # print(len(left), " ", len(right))
    del(node['groups'])
    if not left:
        node['left'] = None
        leftBlank = True
    else:
        node['left'] = left
    if not right:
        node['right'] = None
        rightBlank = True
    else:
        node['right'] = right
    
    if leftBlank == False and len(left) > 1:
        node['left'] = get_split(left)
        split(node['left'], depth + 1)
    else:
        return
    if rightBlank == False and len(right) > 1:
        node['right'] = get_split(right)
        split(node['right'], depth + 1)
    else:
        return


# Build a decision tree
def build_tree(train):
    root = get_split(train)
    split(root, 1)
    return root


# Print a decision tree
def print_tree(node, depth=0):
	if isinstance(node, dict):
		print('%s%s[X%d < %.3f]' % ((depth*'  ', "Level: " + str(depth) + " ", (node['index']+1), node['value'])))
		print_tree(node['left'], depth+1)
		print_tree(node['right'], depth+1)
	else:
		print('%s%s[%s]' % ((depth*'  ', "Level: " + str(depth) + " ", node)))



# Make a prediction with a decision tree
def predict(node, row):
    if node['index'] <= len(row) - 1:
        if row[node['index']] < node['value']:       
            if isinstance(node['left'], dict):
                return predict(node['left'], row)
            elif isinstance(node['left'], list):
                if node['left'][0][1] == row[1] and node['left'][0][0] == row[0]:
                    # print(node['left'])
                    return node['left']
        else:
            if isinstance(node['right'], dict):
                return predict(node['right'], row)
            elif isinstance(node['right'], list):
                if node['right'][0][1] == row[1] and node['right'][0][0] == row[0]:
                    # print(node['right'])
                    return node['right']
    else:
        # print(node)
        return node



# Classification and Regression Tree Algorithm
def decision_tree(trained_dataset):
    # global tree
    tree = build_tree(trained_dataset)
    return tree


def takeQuery(tree, queryLine):
    prediction = list()
    # query = input("Write if you have any Query:\n")
    queryLine = queryLine.strip().split(",")
    for i in range(len(queryLine)):
        if i != 2:
            queryLine[i] = int(queryLine[i])

    # global tree, isFinished
    if len(queryLine) == 1:
        queryLine.append(0)
        for i in range(0, 5):
            queryLine[1] = i
            # print(queryLine)
            result = predict(tree, queryLine)
            if result:
                prediction.extend(result)
    else:
        prediction = predict(tree, queryLine)

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
    filename = '../input/ClassRoutine.txt'
    dataset = load_csv(filename)
    # print(dataset)
    # convert string attributes to integers
    for i in range(len(dataset[0])):
        str_column_to_int(dataset, i)
    # evaluate algorithm
    tree = evaluate_algorithm(dataset, decision_tree)
    # reply = takeQuery()
    # global tree
    return tree
    


if __name__ == "__main__":
    tree = main()