---
permalink: /
title:  "Home"
type: pages
excerpt: Homepage for coneScenes.
header:
  image: /assets/images/fsa-split-lidar.jpg
---

# coneScenes Dataset

The coneScenes dataset is a dataset of LiDAR pointclouds with cone annotations as 3D bounding boxes. The dataset is designed to be used by Formula Student driverless teams.

The data is a collaborative work. It is expected that throught continuously extending and updating the dataset, all teams will be able to use it to train and test their perception algorithms. As for future additions and improvements, this is a community effort and we encourage everyone to contribute. Bigger decisions and potential roadmap changes will be discussed in the [GitHub Discussions](https://github.com/Chalmers-Formula-Student/coneScenes/discussions)

## Contributions

Thanks to all the teams involved in the data collection and annotation process. Our dataset will hopefully continue to grow.
{% include chart_contribution.html %}

## Data Distribution

We hope to keep improving the diversiy of the dataset and the quality of the annotations. As of now there is no labeling guidelines given the novelty of the dataset. We think that with mroe teams contributing and experimenting with the dataset we can come up with a set of guidelines that will be useful for everyone.

As for the current status of the dataset these following charts can give you an idea of the distribution of the data.


{% include chart_range_distribution.html %}

As for spacial distribution of the cones, we have the following chart. A small bias towards the negative y values (clockwise tracks) is aparent and expected to be corrected as more teams contribute to the dataset.

{% include chart_2d_distribution.html %}