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

## Dataset Structure
In order to facilitate structure and modularity, the dataset is structured in scenes, where each scene is a collection of LiDAR scans and cone annotations. These scenes were acquired by different teams and in different tracks, which makes the dataset diverse and challenging. This structure allows for easy expansion of the dataset by adding new scenes as well as a flexible way to use the dataset for training and testing by selecting scenes that are relevant to the task at hand.

### Scene Structure
Each scene is a collection of LiDAR scans and cone annotations. A scene is usually related to a specific track, allowing the user to select scenes independently knowingly that no track will be repeated in different scenes. This is crutial to ensure there is no data leakage between training and testing.

Additionally the scans in a scene are ordered but not continuous, meaning that a significan amount of time has passed between consecutive scans. Thismakes the data more unique and diverse.

#### Scene Structure
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

#### metadata.json
