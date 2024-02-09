import os
import pandas as pd

# Path to the directory containing the scene files
scene_dir = '/Users/bertaveira/Documents/CFS/dv/CFS_dataset/awesome_dataset'

# Open existing csv file
df = pd.read_csv(os.path.join(os.getcwd(),'tools', 'coneScenes_stats.csv'))

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
current_num_scans = df['NumScans'].iloc[-1]
current_num_new_cones = df['NumNewCones'].iloc[-1]

# Get all txt files in the scene directory
label_files = [os.path.join(scene_dir, 'labels', f) for f in os.listdir(os.path.join(scene_dir, 'labels')) if f.endswith('.txt')]
num_scans = len(label_files)

num_new_cones = 0
distribution = []
for label_file in label_files:
    # Open the label file
    with open(label_file, 'r') as f:
        # Count number of non empty lines
        # Read first 3 numbers of each line
        for line in f:
            if line.strip() != '':
                num_new_cones += 1

                numbers = line.split(' ')
                # Compute euclidean distance in 3d
                
                if numbers[0] == '0' and numbers[1] == '0' and numbers[2] == '0':
                    print(f"Skipping cone at origin: {label_file}")
                    continue

                distribution.append((float(numbers[0]), float(numbers[1]), (float(numbers[0]) ** 2 + float(numbers[1]) ** 2 + float(numbers[2]) ** 2) ** 0.5))

# Add new row to the dataframe with current date and number of new cones
new_row = {
    'Date': pd.to_datetime('today'),
    'NumScans': current_num_scans + num_scans,
    'NumNewCones': current_num_new_cones + num_new_cones
}

print(f"New row: {new_row}")

df = pd.concat([df, pd.DataFrame(new_row, index=[0])], ignore_index=True)

# Save the updated dataframe to the csv file
df.to_csv(os.path.join('tools', 'coneScenes_stats.csv'), index=False)

# Append to distribution csv
csv_file = os.path.join('tools', 'coneScenes_distribution.csv')
distribution_df = pd.DataFrame(distribution)
distribution_df.columns = ['X', 'Y', 'Distance']

distribution_df = pd.concat([pd.read_csv(csv_file), distribution_df], ignore_index=True)
distribution_df.to_csv(os.path.join('tools', 'coneScenes_distribution.csv'), index=False, float_format='%.1f')

# Distribution plot
# import plotly.express as px

# fig = px.histogram(distribution_df, x=0, histnorm='density', title='Distribution of cone distances', template='plotly_white')
# fig.update_layout(width=800, height=400)
# fig.update_xaxes(title_text='Distance (m)')
# fig.update_yaxes(title_text='Count')
# fig.show()

import numpy as np
import plotly.figure_factory as ff
import plotly.express as px

pos = np.array(distribution)
x, y = pos[:, 0], pos[:, 1]

import plotly.graph_objects as go

import numpy as np

fig = go.Figure()
fig.add_trace(go.Histogram2dContour(
        x = y,
        y = x,
        colorscale = 'Blues',
        reversescale = True,
        xaxis = 'y',
        yaxis = 'y'
    ))
fig.add_trace(go.Histogram(
        y = x,
        xaxis = 'x2',
        marker = dict(
            color = 'rgba(0,0,0,1)'
        )
    ))
fig.add_trace(go.Histogram(
        x = y,
        yaxis = 'y2',
        marker = dict(
            color = 'rgba(0,0,0,1)'
        )
    ))

fig.update_layout(
    autosize = False,
    xaxis = dict(
        zeroline = False,
        domain = [0,0.85],
        showgrid = False
    ),
    yaxis = dict(
        zeroline = False,
        domain = [0,0.85],
        showgrid = False
    ),
    xaxis2 = dict(
        zeroline = False,
        domain = [0.85,1],
        showgrid = False
    ),
    yaxis2 = dict(
        zeroline = False,
        domain = [0.85,1],
        showgrid = False
    ),
    height = 600,
    width = 600,
    bargap = 0,
    hovermode = 'closest',
    showlegend = False
)

fig.show()
