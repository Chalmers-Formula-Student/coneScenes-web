---
permalink: /tools
title: "Tools"
excerpt: Details of the tools used in the project.
---


# Tools

- [CLI](#cli)
- [generate_scene.py](#generate-scene---generate_scenepy)
- [remove_scan.py](#remove-scans---remove_scanpy)

## CLI

The CLI is a tool that allows you to interact with the dataset. It is designed to be simple and easy to use. The CLI is a Python script that can be run from the command line. It has a number of commands that allow you to add new scenes to the dataset, update existing scenes, and generate statistics about the dataset.

More importantly, the CLI allows you to generate a dataset formated correctly to use the dataset for deep learning.

### `build` command

The `build` command is used to generate a dataset from selected scenes.

When this command is executed you are shown a table of all available scenes in the dataset. You can select the scenes you want and click on which data split you want to add it to (Train, Val or Test). The CLI will then generate a dataset with the selected scenes and save it to the specified output directory.

![CLI build command](/assets/images/tools/cli_build.jpg)

For a more detailed description of the label format and the pointcloud files, please refer to the [Dataset page](/dataset). The final dataset format is preserved for the most part.

Additionally it generates a folder name ÌmageSets` with the following files:

- `train.txt`: List of scenes used for training.
- `val.txt`: List of scenes used for validation.
- `test.txt`: List of scenes used for testing.

These were created to be used with common used deep learning codebases like MMDetection3D.

### `add` command
Usage: conescenes add [OPTIONS] FILE`

> :warning: **This command should only be used with manual package instalation.** The PIP package is not usefull here since this chnage sinternal files that you are expected to commit and make a pull request with to submit the new scene. 

> Fork/Clone the repository and run `pip install -e .` to manually install the package in editable mode.

The `add` command is used to add new scenes to the dataset. When this command is executed, the CLI will prompt you to enter the information about the new scene. This includes the name of the scene, the team that acquired the scene, a description of the scene, the submission date, the label every, the LiDAR information... etc.

After you have entered all the informtion you can notice that the data.json file has been updated with the new scene information. Feel free to make a pull request with this change.

### `doctor` command

The `doctor` command is used to check the integrity of the dataset. When this command is executed, the CLI will check the dataset for any missing files or corrupted files. It will also check the data.json file for any inconsistencies. 

With You should provide the folder with the zips of the scenes you want to check. The CLI will then check the integrity of the dataset and report any issues it finds as well as tell you how many scenes you have avaliable and if you are missing any (you don't need to have all scenes but it is good to know if any are missing).

## Generate Scene - generate_scene.py
> Note: This script is not part of the CLI and is not intended to be used with the CLI. It is a standalone script that you can run on your own.

This is a standalone script that allows you to generate a scene from recording file of your car. This is useful for teams that want to contribute to the dataset but don't have the patience to manually annotate it. 

> :warning: As of now this script only works with MCAP with ROS2 but we think you can easily adapt it to work with other systems. **Please contribute back with changes if you do so.** Either by sharing in discussions or directly in the repository as a pull request.

It is expected that you will need to change soome parameters like the topic names to make it work.

For a detailed explanation on how this script is used, please refer to the [WIP please be patient :)](/guides).


## Remove scans - remove_scan.py

This script is used to remove scans from a scene. This is useful if you want to remove scans that is defective or that you are not happy with. This is useful to run after the `generate_scene.py` script to remove scans that are not good.
