# Import necessary libraries
import dash
from dash import dcc, html
import pandas as pd

# Load the provided dataset
df = pd.read_csv('income_demographics.csv')

# Create a Dash web application
app = dash.Dash(__name__)

# Define the layout of the application
app.layout = html.Div([
    html.H1("Income Demographics Exploratory Data Analysis (EDA) Dashboard"),
    
    # Display the first few rows of the dataset
    html.Div([
        html.H3("Dataset Preview"),
        dcc.Markdown(df.head().to_markdown())
    ]),
    
    # Display summary statistics
    html.Div([
        html.H3("Summary Statistics"),
        dcc.Markdown(df.describe().to_markdown())
    ]),
    
    # Create a histogram of age distribution
    html.Div([
        html.H3("Age Distribution"),
        dcc.Graph(
            figure={
                'data': [
                    dict(
                        x=df['age'],
                        type='histogram'
                    )
                ],
                'layout': dict(
                    xaxis={'title': 'Age'},
                    yaxis={'title': 'Count'},
                    hovermode='closest'
                )
            }
        )
    ]),
    
    # Create a bar chart of hours-per-week distribution by occupation
    html.Div([
        html.H3("Hours-per-Week Distribution by Occupation"),
        dcc.Graph(
            figure={
                'data': [
                    dict(
                        x=df[df['occupation'] == occupation]['hours-per-week'],
                        type='histogram',
                        name=occupation
                    ) for occupation in df['occupation'].unique()
                ],
                'layout': dict(
                    xaxis={'title': 'Hours-per-Week'},
                    yaxis={'title': 'Count'},
                    barmode='overlay',
                    hovermode='closest'
                )
            }
        )
    ]),

    # Create a pie chart for gender distribution
    html.Div([
        html.H3("Gender Distribution"),
        dcc.Graph(
            figure={
                'data': [
                    dict(
                        labels=df['gender'].value_counts().index,
                        values=df['gender'].value_counts().values,
                        type='pie',
                        textinfo='label+percent',
                        insidetextorientation='radial'
                    )
                ],
                'layout': dict(
                    hovermode='closest'
                )
            }
        )
    ]),

        # Create a bar chart for marital status distribution
    html.Div([
        html.H3("Marital Status Distribution"),
        dcc.Graph(
            figure={
                'data': [
                    dict(
                        x=df['marital-status'].value_counts().index,
                        y=df['marital-status'].value_counts().values,
                        type='bar'
                    )
                ],
                'layout': dict(
                    xaxis={'title': 'Marital Status'},
                    yaxis={'title': 'Count'},
                    hovermode='closest'
                )
            }
        )
    ]),

    # Create a bar chart for education level distribution
    html.Div([
        html.H3("Education Level Distribution"),
        dcc.Graph(
            figure={
                'data': [
                    dict(
                        x=df['education'].value_counts().index,
                        y=df['education'].value_counts().values,
                        type='bar'
                    )
                ],
                'layout': dict(
                    xaxis={'title': 'Education Level'},
                    yaxis={'title': 'Count'},
                    hovermode='closest'
                )
            }
        )
    ]),
    
    
])

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
