def dfs(tree, idx):
    operations_queue = []
    stack = [idx]
    while stack:
        task = stack.pop()
        for dependence in tree[task]:
            stack.append(dependence)
        operations_queue.append(task)
    operations_queue.reverse()
    return operations_queue


def main():
    num_of_operations, num_of_lines = map(int, raw_input().split())
    dependencies_tree = {idx: [] for idx in xrange(1, num_of_operations+1)}
    for i in xrange(num_of_lines):
        line = map(int, raw_input().split())
        idx, _, dependencies = line[0], line[1], line[2:]
        dependencies_tree[idx] = dependencies
    print ' '.join(map(str, dfs(dependencies_tree, num_of_operations)))

if __name__ == '__main__':
    main()

