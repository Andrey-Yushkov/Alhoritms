from lab5.utils import file_read, file_write, measure

def calculate_height(n, parents):
    children = [[] for _ in range(n)]
    root = -1

    for child_index, parent_index in enumerate(parents):
        if parent_index == -1:
            root = child_index
        else:
            children[parent_index].append(child_index)

    def height(node):
        if not children[node]:
            return 1
        return 1 + max(height(child) for child in children[node])

    return height(root)

def process_tree_height():
    data = file_read()
    n = int(data[0][0])
    parents = list(map(int, data[1]))
    height = calculate_height(n, parents)
    file_write([height])

if __name__ == "__main__":
    measure(process_tree_height)