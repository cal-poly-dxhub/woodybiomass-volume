import os
import pathlib
import numpy as np
import open3d as o3d
import alphashape
from vedo import *

def get_file_path():
    base_path = pathlib.Path(__file__).parent.absolute()
    relative_path = 'assets\\wood_piles\\wood_stack_1.ply' if os.name == "nt" else 'assets/wood_piles/wood_stack_1.ply'
    return f"{base_path}/{relative_path}"

def load_point_cloud(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    pcl = o3d.io.read_point_cloud(file_path)
    pcl = pcl.voxel_down_sample(voxel_size=0.04)
    return pcl

def process_point_cloud(file_path):
    pcl = load_point_cloud(file_path)

    axis_aligned_bbox = pcl.get_axis_aligned_bounding_box()
    axis_aligned_bbox.color = (1, 0, 0)

    flipped_pcl_points = np.asarray(pcl.points) * [-1, -1, -1]
    combined_points = np.vstack((np.asarray(pcl.points), flipped_pcl_points))

    alpha_shape = alphashape.alphashape(combined_points, 0.1)

    pcl_points = [vertex for vertex in alpha_shape.vertices]

    for face in alpha_shape.faces:
        v1, v2, v3 = alpha_shape.vertices[face]
        for _ in range(20):
            r1, r2 = np.random.random(), np.random.random()
            if r1 + r2 > 1:
                r1, r2 = 1 - r1, 1 - r2
            point = (1 - r1 - r2) * v1 + r1 * v2 + r2 * v3
            pcl_points.append(point)

    outer_pcl = o3d.geometry.PointCloud()
    outer_pcl.points = o3d.utility.Vector3dVector(np.array(pcl_points))

    distances = pcl.compute_point_cloud_distance(outer_pcl)
    threshold = 0.4 if len(pcl.points) >= 100000 else 0.1
    mask = np.asarray(distances) < threshold

    pcl_masked = pcl.select_by_index(np.where(mask)[0], invert=True)
    cl, _ = pcl_masked.remove_statistical_outlier(nb_neighbors=350, std_ratio=0.6)

    hull, _ = cl.compute_convex_hull()
    hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
    hull_ls.paint_uniform_color((1, 0, 0))
    o3d.visualization.draw_geometries([cl, hull_ls])

    volume_m3 = hull.get_volume()
    conversion_factor = 35.3147
    volume_ft3 = volume_m3 * conversion_factor

    print("Volume in cubic meters:", volume_m3)
    print("Volume in cubic feet:", volume_ft3)

    chu = ConvexHull(cl.points)
    chu.print()

if __name__ == "__main__":
    file_path = get_file_path()
    process_point_cloud(file_path)
