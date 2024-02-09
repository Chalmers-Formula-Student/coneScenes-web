import os
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

# Assuming you have already read the CSV files into `dist_df` and `contributions_df`
contributions_df = pd.read_csv(os.getcwd() + '/tools/coneScenes_stats.csv')
dist_df = pd.read_csv(os.getcwd() + '/tools/coneScenes_distribution.csv')


###########################################################
# Contribution plot
###########################################################

# Initialize subplots with 1 row and 2 columns
fig = make_subplots(rows=1, cols=2)

# Scan history across time
fig.add_trace(
    go.Scatter(x=contributions_df['Date'], y=contributions_df['NumScans'], fill='tozeroy', name='LiDAR scans'), # Assuming 'tozeroy' for area plot
    row=1, col=1
)

# Number of cones across time
fig.add_trace(
    go.Scatter(x=contributions_df['Date'], y=contributions_df['NumNewCones'], fill='tozeroy', name='Cones'),
    row=1, col=2
)

# Update layout
fig.update_layout(
    template='plotly_dark',
    title='Contribution history',
    width=1200, # Adjusted for two side-by-side plots
    height=400,
    xaxis_tickformat='%B %Y',
    xaxis2_tickformat='%B %Y', # Ensure the second subplot also has the same tick format
    paper_bgcolor='rgba(0,0,0,0)', # Transparent background
    plot_bgcolor='rgba(0,0,0,0)', # Transparent plot area
)

# If you want to save the plot to HTML, you can use the following
html_string = fig.to_html(full_html=False, include_plotlyjs='cdn')  # Use CDN-hosted JavaScript

# Write the HTML string to a file to be included in your Jekyll template:
with open('_includes/chart_contribution.html', 'w') as f:
    f.write(html_string)


###########################################################
# Range distribution plot
###########################################################

fig = go.Figure()
fig.add_trace(go.Violin(x=dist_df['Distance'], fillcolor='lightsalmon', hoverinfo='x', line_color='salmon', showlegend=False))

fig.update_traces(orientation='h', side='positive', width=3, points=False)
fig.update_layout(
    xaxis_showgrid=False, 
    xaxis_zeroline=False, 
    xaxis_title='Distance (m)', 
    yaxis_title='Density',  # Adjusted to indicate density rather than count
    yaxis=dict(
        showticklabels=False,  # Hides the y-axis tick labels
        showgrid=False,        # Ensures no grid lines are shown on the y-axis
        zeroline=False,        # Hides the y-axis zero line
        showline=False         # Hides the y-axis line
    ),
    width=600, 
    height=300, 
    title='Distribution of Cone Distances', 
    template='plotly_dark',
    paper_bgcolor='rgba(0,0,0,0)', # Transparent background
    plot_bgcolor='rgba(0,0,0,0)', # Transparent plot area
)

# Save html
html_string = fig.to_html(full_html=False, include_plotlyjs='cdn')  # Use CDN-hosted JavaScript

# Write the HTML string to a file to be included in your Jekyll template:
with open('_includes/chart_range_distribution.html', 'w') as f:
    f.write(html_string)


###########################################################
# 2D distribution plot
###########################################################
    
pos = np.array(dist_df[['X', 'Y']])
x, y = pos[:, 0], pos[:, 1]

print(f"X shape: {x.shape}, Y shape: {y.shape}")

fig = go.Figure()
# Detailed filled contours without lines
fig = go.Figure(go.Histogram2dContour(
    x=y,
    y=x,
    colorscale='deep',
    reversescale=True,
    xaxis='x',
    yaxis='y',
    ncontours=100,  # High number for granularity in fill
    contours=dict(
        coloring='fill',
        showlines=False,  # Hide lines in the detailed fill
    )
))

# Add simplified contour lines for a cleaner look
fig.add_trace(go.Histogram2dContour(
    x=y,
    y=x,
    colorscale='Blues',
    reversescale=True,
    xaxis='x',
    yaxis='y',
    ncontours=10,  # Lower number for fewer lines
    contours=dict(
        coloring='none',  # No fill, only lines
        showlines=True,  # Show contour lines
    ),
    line=dict(width=0.5),  # Thinner lines for subtlety
))
fig.add_trace(go.Histogram(
        y = x,
        xaxis = 'x2',
        marker = dict(
            color = 'rgba(250,250,250,1)'
        )
    ))
fig.add_trace(go.Histogram(
        x = y,
        yaxis = 'y2',
        marker = dict(
            color = 'rgba(250,250,250,1)'
        )
    ))

# Add line at x=0
fig.add_shape(
    type="line",
    x0=0,
    y0=0,
    x1=0,
    y1=1,
    line=dict(
        color="LightSeaGreen",
        width=1,
    ),
    xref="x",
    yref="paper",
)

# Add line at y=0
fig.add_shape(
    type="line",
    x0=0,
    y0=0,
    x1=1,
    y1=0,
    line=dict(
        color="LightSeaGreen",
        width=1,
    ),
    xref="paper",
    yref="y",
)

fig.update_layout(
    title='2D Distribution of Cone Positions',
    autosize = False,
    template='plotly_dark',
    xaxis = dict(
        zeroline = False,
        domain = [0,0.85],
        showgrid = False,
        scaleanchor='y',
        scaleratio=1,
        title='Y (m)',
        autorange="reversed",
    ),
    yaxis = dict(
        zeroline = False,
        domain = [0,0.85],
        showgrid = False,
        title='X (m)',
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
    bargap = 0,
    hovermode = 'closest',
    showlegend = False,
    paper_bgcolor='rgba(0,0,0,0)', # Transparent background
    plot_bgcolor='rgba(0,0,0,0)', # Transparent plot area
)

fig.show()

# Save html
html_string = fig.to_html(full_html=False, include_plotlyjs='cdn')  # Use CDN-hosted JavaScript

# Write the HTML string to a file to be included in your Jekyll template:
with open('_includes/chart_2d_distribution.html', 'w') as f:
    f.write(html_string)
