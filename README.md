# Collaboration

Thanks for your interest in our solution. Having specific examples of replication and usage allows us to continue to grow and scale our work. If you clone or use this repository, kindly shoot us a quick email to let us know you are interested in this work!

<wwps-cic@amazon.com>

# Disclaimers

**Customers are responsible for making their own independent assessment of the information in this document.**

**This document:**


Customers are responsible for making their own independent assessment of the information in this document. 

This document: 

(a) is for informational purposes only, 

(b) references AWS product offerings and practices, which are subject to change without notice, 

(c) does not create any commitments or assurances from AWS and its affiliates, suppliers or licensors. AWS products or services are provided “as is” without warranties, representations, or conditions of any kind, whether express or implied. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements, and this document is not part of, nor does it modify, any agreement between AWS and its customers, and 

(d) is not to be considered a recommendation or viewpoint of AWS. 

Additionally, you are solely responsible for testing, security and optimizing all code and assets on GitHub repo, and all such code and assets should be considered: 

(a) as-is and without warranties or representations of any kind, 

(b) not suitable for production environments, or on production or other critical data, and 

(c) to include shortcuts in order to support rapid prototyping such as, but not limited to, relaxed authentication and authorization and a lack of strict adherence to security best practices. 

All work produced is open source. More information can be found in the GitHub repo. 
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
