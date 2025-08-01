def lca(root, v1, v2):
    def find_path(root, val):
        path = []
        while root:
            path.append(root)
            if val < root.info:
                root = root.left
            elif val > root.info:
                root = root.right
            else:
                break
        return path

    path1 = find_path(root, v1)
    path2 = find_path(root, v2)
    lca_node = None
    for u, v in zip(path1, path2):
        if u.info == v.info:
            lca_node = u
        else:
            break

    return lca_node
