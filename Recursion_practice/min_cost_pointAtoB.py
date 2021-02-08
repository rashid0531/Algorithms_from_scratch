distance = [[0, 10, 75, 94],
            [-1, 0, 35, 50],
            [-1, -1, 0, 80],
            [-1, -1, -1, 0]]


def get_cost(point1_idx, point2_idx):
    return distance[point1_idx][point2_idx]


def min_cost(source, destination, name_map, idx_to_name_map):
    if source == destination:
        return 0
    try:
        pt1_idx = name_map[source]
        pt2_idx = name_map[destination]

        pt_to_pt_cost_list = list()
        for idx in range(pt1_idx+1, pt2_idx+1):
            pt_to_pt_cost_list.append(get_cost(pt1_idx, idx) +
                                      min_cost(idx_to_name_map[idx],
                                               idx_to_name_map[pt2_idx],
                                               name_map,
                                               idx_to_name_map))
        return min(pt_to_pt_cost_list)

    except (IndexError, KeyError) as err:
        print('invalid index or key. Please give correct index or key')


if __name__ == "__main__":

    name_to_dist_index_mapping = {'A': 0,
                                  'B': 1,
                                  'C': 2,
                                  'D': 3}
    dis_idx_to_name_mapping = {0: 'A',
                               1: 'B',
                               2: 'C',
                               3: 'D'}

    cost = min_cost('A', 'C', name_to_dist_index_mapping, dis_idx_to_name_mapping)
    print(cost)








