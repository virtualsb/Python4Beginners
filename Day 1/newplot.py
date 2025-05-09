import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# Sample Data
np.random.seed(42)
df = pd.DataFrame({
    'Year': np.tile(np.arange(2015, 2021), 3),
    'Category': np.repeat(['A', 'B', 'C'], 6),
    'Value': np.random.randint(100, 500, size=18)
})

# 1. Line chart using Plotly Express
fig_line = px.line(df, x='Year', y='Value', color='Category', markers=True,
                   title='Line Chart - Value Over Years by Category')

# 2. Bar chart
fig_bar = px.bar(df, x='Year', y='Value', color='Category', barmode='group',
                 title='Bar Chart - Grouped by Category')

# 3. Scatter plot
df_scatter = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'size': np.random.rand(100) * 40,
    'group': np.random.choice(['X', 'Y'], size=100)
})
fig_scatter = px.scatter(df_scatter, x='x', y='y', color='group', size='size',
                         title='Scatter Plot with Size and Color')

# 4. Pie chart
df_pie = df.groupby("Category")['Value'].sum().reset_index()
fig_pie = px.pie(df_pie, names='Category', values='Value', title='Pie Chart - Total Value per Category')

# 5. Combined subplots using Graph Objects
fig_combined = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Line Chart", "Bar Chart", "Scatter Plot", "Pie Chart"),
    specs=[[{}, {}], [{"type": "scatter"}, {"type": "domain"}]]
)

# Add traces
for cat in df['Category'].unique():
    df_cat = df[df['Category'] == cat]
    fig_combined.add_trace(go.Scatter(x=df_cat['Year'], y=df_cat['Value'], mode='lines+markers', name=cat),
                           row=1, col=1)

for cat in df['Category'].unique():
    df_cat = df[df['Category'] == cat]
    fig_combined.add_trace(go.Bar(x=df_cat['Year'], y=df_cat['Value'], name=f"{cat} - Bar"), row=1, col=2)

fig_combined.add_trace(go.Scatter(x=df_scatter['x'], y=df_scatter['y'],
                                  mode='markers', marker=dict(size=df_scatter['size']),
                                  name='Scatter'), row=2, col=1)

fig_combined.add_trace(go.Pie(labels=df_pie['Category'], values=df_pie['Value'], name='Pie'), row=2, col=2)

fig_combined.update_layout(title_text="Combined Dashboard with Subplots", height=800)

# 6. Interactive buttons (toggle chart type)
fig_toggle = go.Figure()
fig_toggle.add_trace(go.Scatter(x=df['Year'], y=df['Value'], mode='lines', name='Line'))
fig_toggle.add_trace(go.Bar(x=df['Year'], y=df['Value'], name='Bar'))

fig_toggle.update_layout(
    updatemenus=[dict(
        type="buttons",
        direction="right",
        buttons=list([
            dict(label="Line", method="update",
                 args=[{"type": "scatter"}, {"title": "Line View"}]),
            dict(label="Bar", method="update",
                 args=[{"type": "bar"}, {"title": "Bar View"}]),
        ]),
        pad={"r": 10, "t": 10},
        showactive=True,
        x=0.1,
        xanchor="left",
        y=1.2,
        yanchor="top"
    )],
    title="Toggle Between Line and Bar Chart"
)

# Show all figures
fig_line.show()
fig_bar.show()
fig_scatter.show()
fig_pie.show()
fig_combined.show()
fig_toggle.show()
