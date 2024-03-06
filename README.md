# Point Cloud Processing and Volume Calculation
This Python script allows you to load and process a point cloud, ultimately calculating and displaying the volume of its convex hull. 
# Dependencies
- Python 3.10.11
- NumPy 1.24.2
- Open3D 0.17.0
- alphashape 1.3.1
- pyvista 0.38.5


```bash
pip install -r requirements.txt
```

## How it Works

- The script determines the file path of a specified point cloud file.
- It loads the point cloud and performs voxel down-sampling.
- The script then computes the axis-aligned bounding box of the point cloud and flips the point cloud.
- An alpha shape of the combined points (original and flipped) is computed.
- It generates random points on the faces of the alpha shape.
- The script calculates distances between the original point cloud and the alpha shape and masks the point cloud based on these distances.
- Outliers are removed and the convex hull is computed.
- The convex hull and the point cloud are visualized.
- Finally, the volume of the convex hull is calculated and displayed in both cubic meters and cubic feet.

## Additional Configuration

For PyVista backend settings:

In your script, include:
``` python
import pyvista as pv
from pyvista import settings
settings.default_backend = 'ipyvtk'  # Set the default backend for PyVista
pv.set_jupyter_backend('trame')  # Set the Jupyter backend for PyVista