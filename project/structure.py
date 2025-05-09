def render(file_obj) -> str:
    """
    Turn the project structure from simple text description to standard tree structure.

    :file_obj: the input file.

    :return: tree structure.
    """
    lines = [line.strip() for line in file_obj if line.strip()]
    if not lines:
        return ""
    
    root = lines[0]
    tree = {root: {}}
    stack = [(0, tree[root])]
    
    for line in lines[1:]:
        indent = line.count('>')
        name = line.lstrip('>').strip()
        
        while stack and stack[-1][0] >= indent:
            stack.pop()
            
        if stack:
            parent_indent, parent_node = stack[-1]
            parent_node[name] = {}
            stack.append((indent, parent_node[name]))
    
    return build_tree_string(root, tree[root], "")

def build_tree_string(name, children, prefix) -> str:
    """
    Build tree structure.

    :name: current node name
    :children: child node
    :prefix: the prefix string in current line.
    
    :return: the result of building.
    """
    lines = [name]
    child_keys = sorted(children.keys())
    for i, child in enumerate(child_keys):
        if i == len(child_keys) - 1:
            new_prefix = prefix + "    "
            lines.append(prefix + "└── " + build_tree_string(child, children[child], new_prefix))
        else:
            new_prefix = prefix + "│   "
            lines.append(prefix + "├── " + build_tree_string(child, children[child], new_prefix))
    
    return "\n".join(lines)


if __name__ == '__main__':
    """
    Here shows the way to use project.strcture.py .
    First, open a file in the 'with' sentence,
    then use render to get the string return.
    Finally, you can print the result, or write it into a new file.

    If you are using this module by 'import' in other python file,
    you can just import the 'render' method:
        from Unifout.project.structure import render
    """
    with open("test.txt", "r") as f:
    # change the 'test.txt' to your own file target.
        result = render(f)
        print(result)