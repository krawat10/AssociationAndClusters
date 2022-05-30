from typing import List
import numpy as np
from Models.Cluster import Cluster
from Models.Point import Point


def powerset(s: np.array, array_size: int):
    x = len(s)
    combinations = []
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        combination = []
        for mask, ss in zip(masks, s):
            if i & mask:
                combination.append(ss)
        if len(combination) == array_size:
            combinations.append(combination)

    return combinations


def flatten(list: List[List[any]]):
    flattened = []
    for sublist in list:
        for val in sublist:
            flattened.append(val)

    return flattened


def update_clusters(points: List[Point], clusters: List[Cluster]):
    for cluster in clusters:
        cluster.clear_points()

    for point in points:
        closest_cluster = clusters[0]

        for cluster in clusters:
            distance_to_middle = cluster.middle.distance_to(point)
            if distance_to_middle <= closest_cluster.middle.distance_to(point):
                closest_cluster = cluster

        closest_cluster.add_point(point)

    return clusters
