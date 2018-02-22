A = [7, 8, 3, 9, 5, 1, 10, 1]

segment_tree = [0] * (2*len(A))

print(len(segment_tree))


def build_segment_tree(code, A, node, b, e):
    if b == e:
        segment_tree[node] = b

    else:
        left_index = 2*node
        right_index = 2*node+1
        build_segment_tree(code, A, left_index, b, int((b+e)/2))
        build_segment_tree(code, A, right_index, int((b+e)/2) + 1, e)
        l_content = segment_tree[left_index]
        r_content = segment_tree[right_index]

        if A[l_content] <= A[r_content]:
            segment_tree[node] = l_content
        else:
            segment_tree[node] = r_content


build_segment_tree("MIN", A, 1, 0, 7)
print(segment_tree)