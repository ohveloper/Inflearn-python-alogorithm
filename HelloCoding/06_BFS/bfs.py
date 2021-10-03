from collections import deque

graph = {}
graph["me"] = ["shay", "ohveloper", "neul"]
graph["shay"] = ["summer", "spring"]
graph["ohveloper"] = []
graph["neul"] = []
graph["summer"] = []
graph["spring"] = []

def is_person_seller(name):
    if name[-1] == "y":
        return True

def search(name):

    bfs = deque()
    # print(bfs)
    bfs += graph[name]
    # print(bfs)
    searched = []
    while bfs:
        person = bfs.popleft()
        if not person in searched:
            if is_person_seller(person):
                print("%s is seller!!" % person)
                return True
            else:
                bfs += graph[person]
                searched.append(person)
    print("can't find seller..")
    return False


search("me")
