import random
from typing import List
from Models.Cluster import Cluster
from Models.Point import Point
from utils import update_clusters


def clusters_task():
    points: List[Point] = [
        Point(1.0, 2.0),
        Point(2.0, 2.0),
        Point(3.0, 1.0),
        Point(4.0, 1.0),
        Point(11.0, 1.0),
        Point(12.0, 1.0),
        Point(13.0, 1.0)
    ]

    # Create clusters with middle in random point
    cluster_list: List[Cluster] = [Cluster(point, idx) for idx, point in enumerate(random.sample(points, 2))]

    has_any_change = True

    while has_any_change:
        update_clusters(points, cluster_list)  # update cluster points
        has_any_change = any([cluster.update_middle() for cluster in cluster_list])  # update cluster middle and check if changed

    for cluster in cluster_list:
        for point in cluster.points:
            print(f"(After) Point ({point.x}, {point.y}) belongs to cluster {cluster.k} ({cluster.middle.x}, {cluster.middle.y})")
