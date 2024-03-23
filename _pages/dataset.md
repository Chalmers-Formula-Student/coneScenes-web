---
permalink: /dataset
title: "Dataset"
excerpt: Details of the dataset.
header:
  image: /assets/images/fsa-split-lidar.jpg
---

# coneScenes Dataset

The coneScenes dataset is a collection of LiDAR scans from formula student tracks composed of cones. The dataset is designed to be used for training and testing of perception algorithms for Formula Student Driverless vehicles. The dataset is composed of 3D point clouds and cone annotations.

As community driven dataset, we encourage contributions from the community in order to expand the dataset and make it more diverse with multiple LiDAR models, positions and environments.

Page index:

- [Dataset Structure](#dataset-structure)
    - [data.json](#datajson)
- [Scene Structure](#scene-structure)
    - [metadata.json](#metadatajson)
    - [Point Cloud File Format](#point-cloud-file-format)
    - [Labels File Format](#labels-file-format)
    - [Unlabeled Clouds](#unlabeled-clouds)

## Dataset Structure
In order to facilitate structure and modularity, the dataset is structured in scenes, where each scene is a collection of LiDAR scans and cone annotations. 
These scenes were acquired by different teams and in different tracks, which makes the dataset diverse and challenging. This structure allows for easy expansion of the dataset by adding new scenes as well as a flexible way to use the dataset for training and testing by selecting scenes that are relevant to the task at hand.

### data.json

The dataset is described by a `data.json` file that contains the following fields:

- `version`: Version of the dataset. This is useful to keep track of the changes in the dataset.
- `last_updated`: Date of the last update of the dataset. This generally means the addition of new scenes.
- `data`: List of scenes in the dataset. Each scene is represented by a dictionary with the following fields:
    - `name`: Name of the scene.
    - `team`: Name of the team that acquired the scene.
    - `description`: Description of the scene.
    - `submission_date`: Date of the submission of the scene.
    - `label_every`: How many past lidar scans exist for every labeled one.
    - `lidar`: Info about LiDAR
        - `manufacturer`: Manufacturer of the LiDAR (e.g. Velodyne, Ouster, etc.)
        - `model`: Model of the LiDAR (e.g. VLP, OS1, etc.)
        - `config`: Configuration of the beams of LiDAR or empty if not applicable (e.g. Gradient, Bellow Horizon, etc.)
        - `vres`: Vertical resolution of the LiDAR (e.g. 64, 23, etc.)
        - `hres`: Horizontal resolution of the LiDAR (e.g. 1024, 2048 etc.)
        - `fov`: Field of view of the LiDAR (e.g. 360, 120, etc.)
        - `frequency`: Frequency of the LiDAR (e.g. 10, 20, etc.)
        - `location`: Location of lidar in the car (e.g. nose, mainhoop, frontwing, etc.)
    - `num_labelled_frames`: Number of annotated scans
    - `num_unlabelled_frames`: Number of unannotated scans (belongign to past frames of the annotated ones)
    - `file_path`: Path to the scene folder.
    - `checksum`: Checksum of the scene zip file.

This file can be found on the Github repository of the dataset. **This file should not be manually overwritten. The CLI commands like "add" write to this file directly.**

## Scene Structure
Each scene is a collection of LiDAR scans and cone annotations. A scene is usually related to a specific track, allowing the user to select scenes independently knowingly that no track will be repeated in different scenes. This is crutial to ensure there is no data leakage between training and testing.

Additionally the scans in a scene are ordered but not continuous, meaning that a significan amount of time has passed between consecutive scans. Thismakes the data more unique and diverse.

### Scene Structure
Each scene is composed of the following files:

```
scene_name/
    points/
        0000000.bin
        0000001.bin
        ...
    labels/
        scan_0000.json
        scan_0001.json
        ...
    metadata.json
```

### metadata.json

The metadata file contains information about all the scenes. **Apart from the discription this file should not be manually overwritten.** It contains the following fields:

- `info`: Information about the tool used to generate the dataset, the version of the tool, the description of the dataset, the date of generation, the date of the last update, the source of the data and the user that generated the dataset.
    - `tool`: Tool used to generate the dataset.
    - `version`: Version of the tool used to generate the dataset.
    - `description`: Description of the dataset. Feel free to add any notes here about the data.
    - `generated_on`: Date of the generation of the dataset.
    - `last_updated`: Date of the last update of the dataset.
    - `source`: Source of the data. Usually advisable to keep the original file name so it can be used to regenerate if needed.
    - `user`: User that generated the dataset.
- `data`: List of scenes in the dataset. Each scene is represented by a dictionary with the following fields:
    - `id`: Unique identifier of the scene. This id is unique for the scene but not the dataset. Usually starts at 0
    - `odom`: Odometry information of the scan.
        - `timestamp`: Timestamp of the scan. This should be in epoch time!
        - `x`: X position of the scan.
        - `y`: Y position of the scan.
        - `z`: Z position of the scan.
        - `yaw`: Yaw angle of the scan.
        - `vx`: X velocity of the scan.
        - `vy`: Y velocity of the scan.
        - `yawrate`: Yaw rate of the scan.
    - `pointcloud`: File name and checksum of the point cloud. For more information about the point cloud file format, see the [Point Cloud File Format](#point-cloud-file-format) section.        
    - `labels`: File name and checksum of the labels. The labels file is a JSON file containing the annotations of the cones in the scan. For more information about the labels file format, see the [Labels File Format](#labels-file-format) section.
    - `unlabeled_clouds`: List of unlabeled point clouds in the scene. For why we have this read the [Unlabeled Clouds](#unlabeled-clouds) section.

Example:

```
{
    "info": {
        "tool": "generateDataset.py",
        "version": "0.1",
        "description": "Generated from MCAP file",
        "generated_on": "2023-11-12 17:01:14",
        "last_updated": "2023-11-14 22:34:25",
        "source": "vargarda8_mixed_2023-07-27-17-22-00_0.mcap",
        "user": "bertaveira"
    },
    "data": [
        {
            "id": 1,
            "odom": {
                "timestamp": 1690471366.251078,
                "x": 10.72408035097532,
                "y": -0.4972308351082878,
                "z": 0.0,
                "yaw": -0.11381138116121292,
                "vx": 11.2505778617818,
                "vy": -0.13662984009074464,
                "yawrate": -0.18480854369234262
            },
            "pointcloud": {
                "file": "points/0000001.bin",
                "checksum": "d4366d8da59d19c14d6fa46fe445c4cf"
            },
            "labels": {
                "file": "labels/0000001.txt",
                "checksum": "ffc7ac5c5672630b84a096f3ef4f53ac"
            },
            "unlabeled_clouds": [
                {
                    "file": "unlabeled_pc/0000001_01.bin",
                    "checksum": "8bacb90ecb90efa6ed46f790f0f0115c",
                    "odom": {
                        "timestamp": 1690471365.801196,
                        "x": 5.793006310679532,
                        "y": -0.0972052977780586,
                        "z": 0.0,
                        "yaw": -0.10356351733207703,
                        "vx": 10.908167654673383,
                        "vy": 0.08232379387432813,
                        "yawrate": 0.028638576665627
                    }
                },
                {
                    ...
```


### Point Cloud File Format

The pointcloud file is a binary file containing the 3D points of the LiDAR scan. The file is in the binary format and can be read using the `numpy` library. The file is a 2D array with the shape `(N, 4)` where `N` is the number of points in the scan and the columns are the `x`, `y`, `z` and `intensity` of the points.

```python
import numpy as np

num_points = 100

# random pointcloud
points = np.random.rand(num_points, 4).astype(np.float32)
with open('point_cloud_data.bin', 'wb') as f:
    f.write(points.tobytes())
```

### Labels File Format

The labels file is a TXT file that is compliant with the MMDetection3D format (see [MMDetection3D](https://mmdetection3d.readthedocs.io/en/latest/advanced_guides/customize_dataset.html#label-format)). The label should be named `Cone` and the format should be as follows:

```
# format: [x, y, z, dx, dy, dz, yaw, category_name]
1.23 1.42 -0.4 0.23 0.23 0.33 0.0 Cone_Yellow
...
```

There are 4 possible labels for the cones: `Cone_Yellow`, `Cone_Blue`, `Cone_Orange` and `Cone_Big`. The `Cone_Big` label is used for the big cones that are usually placed at the start and end of the track.


### Unlabeled Clouds

For each scan in a scene we also provide n amount of past scans. These previous scans are not annotated in themselfs but their oddometry is published so they can be used aggregated with the labeled scans. This is useful for training models that require temporal information or to build a denser cloud. The number of unlabeled clouds is not fixed and can vary from scene to scene.
