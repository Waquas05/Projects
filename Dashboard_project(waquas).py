#dataframe work
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
file = pd.read_csv(r"C:\Users\Zeya\Downloads\death rate dataset\death rate of countries and its causes.csv")
df = pd.DataFrame(file)
grouped = df.groupby("Entity")
df.drop(columns="Code", inplace=True)
df.drop(columns="Entity", inplace=True)
tables = {}
for i, j in grouped:
    tables[i]=j.reset_index(drop=True)
df.set_index("Year", inplace=True)
#=============================================================================================================
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import requests
import json

# Step 1: Read the CSV file into a pandas DataFrame
url = 'https://drive.google.com/uc?id=1Wbb3hH5u_qkfSMQcPuSIkHPXYtP-gJUH'
df = pd.read_csv(r"C:\Users\Zeya\Downloads\death rate dataset\death rate of countries and its causes.csv")
# Step 2: Load the JSON file of the world map
world_map_json_url = 'https://github.com/johan/world.geo.json/raw/master/countries.geo.json'
response = requests.get(world_map_json_url)
world_map_json = response.json()

#Dashboard work
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app=dash.Dash()
app.layout=html.Div([html.H1(children="ANALYSIS OF CAUSES OF DEATH IN VARIOUS COUNTRIES",
                             style={
                                  'font-family': 'Arial, sans-serif',
                                 'textAlign':'center',
                                 'color': 'Black'
                             }),
                     html.Label('Choose a country',
                                 style={
                                      'font-family': 'Arial, sans-serif'
                                      }),
    html.Label('Choose a year for Pie Chart',
            style={
            'position': 'absolute',
            'font-family': 'Arial, sans-serif',
            'top': '100px',
            'right': '340px',
            'width': '200px'
        }),
    dcc.Dropdown(
        id='dropdown3',
        options=[
{'label':'1990', 'value':1990},
{'label':'1991', 'value':1991},
{'label':'1992', 'value':1992},
{'label':'1993', 'value':1993},
{'label':'1994', 'value':1994},
{'label':'1995', 'value':1995},
{'label':'1996', 'value':1996},
{'label':'1997', 'value':1997},
{'label':'1998', 'value':1998},
{'label':'1999', 'value':1999},
{'label':'2000', 'value':2000},
{'label':'2001', 'value':2001},
{'label':'2002', 'value':2002},
{'label':'2003', 'value':2003},
{'label':'2004', 'value':2004},
{'label':'2005', 'value':2005},
{'label':'2006', 'value':2006},
{'label':'2007', 'value':2007},
{'label':'2008', 'value':2008},
{'label':'2009', 'value':2009},
{'label':'2010', 'value':2010},
{'label':'2011', 'value':2011},
{'label':'2012', 'value':2012},
{'label':'2013', 'value':2013},
{'label':'2014', 'value':2014},
{'label':'2015', 'value':2015},
{'label':'2016', 'value':2016},
{'label':'2017', 'value':2017},
{'label':'2018', 'value':2018},
{'label':'2019', 'value':2019}],
        placeholder='select a year',
        style={'position': 'absolute',
            'width': '200px',
               'backgroundColor': '#C8FF11',
               'right':'170px'}),
    html.Label('Choose a year for map',
            style={
            'position': 'absolute',
            'font-family': 'Arial, sans-serif',
            'top': '100px',
            'right': '16px',
            'width': '200px'
        }),
    dcc.Dropdown(
        id='dropdown4',
        options=[
{'label':'1990', 'value':1990},
{'label':'1991', 'value':1991},
{'label':'1992', 'value':1992},
{'label':'1993', 'value':1993},
{'label':'1994', 'value':1994},
{'label':'1995', 'value':1995},
{'label':'1996', 'value':1996},
{'label':'1997', 'value':1997},
{'label':'1998', 'value':1998},
{'label':'1999', 'value':1999},
{'label':'2000', 'value':2000},
{'label':'2001', 'value':2001},
{'label':'2002', 'value':2002},
{'label':'2003', 'value':2003},
{'label':'2004', 'value':2004},
{'label':'2005', 'value':2005},
{'label':'2006', 'value':2006},
{'label':'2007', 'value':2007},
{'label':'2008', 'value':2008},
{'label':'2009', 'value':2009},
{'label':'2010', 'value':2010},
{'label':'2011', 'value':2011},
{'label':'2012', 'value':2012},
{'label':'2013', 'value':2013},
{'label':'2014', 'value':2014},
{'label':'2015', 'value':2015},
{'label':'2016', 'value':2016},
{'label':'2017', 'value':2017},
{'label':'2018', 'value':2018},
{'label':'2019', 'value':2019}],
        placeholder='select a year',
        style={'position': 'absolute',
            'width': '200px',
               'backgroundColor': '#C8FF11',
               'right':'10px'}),
    dcc.Dropdown(
        id='dropdown',
        options=[
{'label':'Afghanistan', 'value':'Afghanistan'},
{'label':'Albania', 'value':'Albania'},
{'label':'Algeria', 'value':'Algeria'},
{'label':'Andorra', 'value':'Andorra'},
{'label':'Angola', 'value':'Angola'},
{'label':'Antigua and Barbuda', 'value':'Antigua and Barbuda'},
{'label':'Argentina', 'value':'Argentina'},
{'label':'Armenia', 'value':'Armenia'},
{'label':'Australia', 'value':'Australia'},
{'label':'Austria', 'value':'Austria'},
{'label':'Azerbaijan', 'value':'Azerbaijan'},
{'label':'The Bahamas', 'value':'The Bahamas'},
{'label':'Bahrain', 'value':'Bahrain'},
{'label':'Bangladesh', 'value':'Bangladesh'},
{'label':'Barbados', 'value':'Barbados'},
{'label':'Belarus', 'value':'Belarus'},
{'label':'Belgium', 'value':'Belgium'},
{'label':'Belize', 'value':'Belize'},
{'label':'Benin', 'value':'Benin'},
{'label':'Bhutan', 'value':'Bhutan'},
{'label':'Bolivia', 'value':'Bolivia'},
{'label':'Bosnia and Herzegovina', 'value':'Bosnia and Herzegovina'},
{'label':'Botswana', 'value':'Botswana'},
{'label':'Brazil', 'value':'Brazil'},
{'label':'Brunei', 'value':'Brunei'},
{'label':'Bulgaria', 'value':'Bulgaria'},
{'label':'Burkina Faso', 'value':'Burkina Faso'},
{'label':'Burundi', 'value':'Burundi'},
{'label':'Cabo Verde', 'value':'Cabo Verde'},
{'label':'Cambodia', 'value':'Cambodia'},
{'label':'Cameroon', 'value':'Cameroon'},
{'label':'Canada', 'value':'Canada'},
{'label':'Central African Republic', 'value':'Central African Republic'},
{'label':'Chad', 'value':'Chad'},
{'label':'Chile', 'value':'Chile'},
{'label':'China', 'value':'China'},
{'label':'Colombia', 'value':'Colombia'},
{'label':'Comoros', 'value':'Comoros'},
{'label':'Congo', 'value':'Congo'},
{'label':'Costa Rica', 'value':'Costa Rica'},
{'label':'Croatia', 'value':'Croatia'},
{'label':'Cuba', 'value':'Cuba'},
{'label':'Cyprus', 'value':'Cyprus'},
{'label':'Czech Republic', 'value':'Czech Republic'},
{'label':'Denmark', 'value':'Denmark'},
{'label':'Djibouti', 'value':'Djibouti'},
{'label':'Dominica', 'value':'Dominica'},
{'label':'Dominican Republic', 'value':'Dominican Republic'},
{'label':'East Timor', 'value':'East Timor'},
{'label':'Ecuador', 'value':'Ecuador'}, 
{'label':'Egypt', 'value':'Egypt'},
{'label':'El Salvador', 'value':'El Salvador'},
{'label':'Equatorial Guinea', 'value':'Equatorial Guinea'},
{'label':'Eritrea', 'value':'Eritrea'},
{'label':'Estonia', 'value':'Estonia'},
{'label':'Eswatini', 'value':'Eswatini'},
{'label':'Ethiopia', 'value':'Ethiopia'},
{'label':'Fiji', 'value':'Fiji'},
{'label':'Finland', 'value':'Finland'},
{'label':'France', 'value':'France'},
{'label':'Gabon', 'value':'Gabon'},
{'label':'The Gambia', 'value':'The Gambia'},
{'label':'Georgia', 'value':'Georgia'},
{'label':'Germany', 'value':'Germany'},
{'label':'Ghana', 'value':'Ghana'},
{'label':'Greece', 'value':'Greece'},
{'label':'Grenada', 'value':'Grenada'},
{'label':'Guatemala', 'value':'Guatemala'},
{'label':'Guinea', 'value':'Guinea'},
{'label':'Guinea-Bissau', 'value':'Guinea-Bissau'},
{'label':'Guyana', 'value':'Guyana'},
{'label':'Haiti', 'value':'Haiti'},
{'label':'Honduras', 'value':'Honduras'},
{'label':'Hungary', 'value':'Hungary'},
{'label':'Iceland', 'value':'Iceland'},
{'label':'India', 'value':'India'},
{'label':'Indonesia', 'value':'Indonesia'},
{'label':'Iran', 'value':'Iran'},
{'label':'Iraq', 'value':'Iraq'},
{'label':'Ireland', 'value':'Ireland'},
{'label':'Israel', 'value':'Israel'},
{'label':'Italy', 'value':'Italy'},
{'label':'Jamaica', 'value':'Jamaica'},
{'label':'Japan', 'value':'Japan'},
{'label':'Jordan', 'value':'Jordan'},
{'label':'Kazakhstan', 'value':'Kazakhstan'},
{'label':'Kenya', 'value':'Kenya'},
{'label':'Kiribati', 'value':'Kiribati'},
{'label':'North Korea', 'value':'North Korea'},
{'label':'South Korea', 'value':'South Korea'},
{'label':'Kosovo', 'value':'Kosovo'},
{'label':'Kuwait', 'value':'Kuwait'},
{'label':'Kyrgyzstan', 'value':'Kyrgyzstan'},
{'label':'Laos', 'value':'Laos'},
{'label':'Latvia', 'value':'Latvia'},
{'label':'Lebanon', 'value':'Lebanon'},
{'label':'Lesotho', 'value':'Lesotho'},
{'label':'Liberia', 'value':'Liberia'},
{'label':'Libya', 'value':'Libya'},
{'label':'Liechtenstein', 'value':'Liechtenstein'},
{'label':'Lithuania', 'value':'Lithuania'},
{'label':'Luxembourg', 'value':'Luxembourg'},
{'label':'Madagascar', 'value':'Madagascar'},
{'label':'Malawi', 'value':'Malawi'},
{'label':'Malaysia', 'value':'Malaysia'},
{'label':'Maldives', 'value':'Maldives'},
{'label':'Mali', 'value':'Mali'},
{'label':'Malta', 'value':'Malta'},
{'label':'Marshall Islands', 'value':'Marshall Islands'},
{'label':'Mauritania', 'value':'Mauritania'},
{'label':'Mauritius', 'value':'Mauritius'},
{'label':'Mexico', 'value':'Mexico'},
{'label':'Micronesia (country)', 'value':'Micronesia (country)'},
{'label':'Moldova', 'value':'Moldova'},
{'label':'Monaco', 'value':'Monaco'},
{'label':'Mongolia', 'value':'Mongolia'},
{'label':'Montenegro', 'value':'Montenegro'},
{'label':'Morocco', 'value':'Morocco'},
{'label':'Mozambique', 'value':'Mozambique'},
{'label':'Myanmar', 'value':'Myanmar'},
{'label':'Namibia', 'value':'Namibia'},
{'label':'Nauru', 'value':'Nauru'},
{'label':'Nepal', 'value':'Nepal'},
{'label':'Netherlands', 'value':'Netherlands'},
{'label':'New Zealand', 'value':'New Zealand'},
{'label':'Nicaragua', 'value':'Nicaragua'},
{'label':'Niger', 'value':'Niger'},
{'label':'Nigeria', 'value':'Nigeria'},
{'label':'North Macedonia', 'value':'North Macedonia'},
{'label':'Norway', 'value':'Norway'},
{'label':'Oman', 'value':'Oman'},
{'label':'Pakistan', 'value':'Pakistan'},
{'label':'Palau', 'value':'Palau'},
{'label':'Panama', 'value':'Panama'},
{'label':'Papua New Guinea', 'value':'Papua New Guinea'},
{'label':'Paraguay', 'value':'Paraguay'},
{'label':'Peru', 'value':'Peru'},
{'label':'Philippines', 'value':'Philippines'},
{'label':'Poland', 'value':'Poland'},
{'label':'Portugal', 'value':'Portugal'},
{'label':'Qatar', 'value':'Qatar'},
{'label':'Romania', 'value':'Romania'},
{'label':'Russia', 'value':'Russia'},
{'label':'Rwanda', 'value':'Rwanda'},
{'label':'Saint Kitts and Nevis', 'value':'Saint Kitts and Nevis'},
{'label':'Saint Lucia', 'value':'Saint Lucia'},
{'label':'Saint Vincent and the Grenadines', 'value':'Saint Vincent and the Grenadines'},
{'label':'Samoa', 'value':'Samoa'},
{'label':'San Marino', 'value':'San Marino'},
{'label':'Sao Tome and Principe', 'value':'Sao Tome and Principe'},
{'label':'Saudi Arabia', 'value':'Saudi Arabia'},
{'label':'Senegal', 'value':'Senegal'},
{'label':'Serbia', 'value':'Serbia'},
{'label':'Seychelles', 'value':'Seychelles'},
{'label':'Sierra Leone', 'value':'Sierra Leone'},
{'label':'Singapore', 'value':'Singapore'},
{'label':'Slovakia', 'value':'Slovakia'},
{'label':'Slovenia', 'value':'Slovenia'},
{'label':'Solomon Islands', 'value':'Solomon Islands'},
{'label':'Somalia', 'value':'Somalia'},
{'label':'South Africa', 'value':'South Africa'},
{'label':'Spain', 'value':'Spain'},
{'label':'Sri Lanka', 'value':'Sri Lanka'},
{'label':'Sudan', 'value':'Sudan'},
{'label':'Suriname', 'value':'Suriname'},
{'label':'Sweden', 'value':'Sweden'},
{'label':'Switzerland', 'value':'Switzerland'},
{'label':'Syria', 'value':'Syria'},
{'label':'Taiwan', 'value':'Taiwan'},
{'label':'Tajikistan', 'value':'Tajikistan'},
{'label':'Tanzania', 'value':'Tanzania'},
{'label':'Thailand', 'value':'Thailand'},
{'label':'Togo', 'value':'Togo'},
{'label':'Tonga', 'value':'Tonga'},
{'label':'Trinidad and Tobago', 'value':'Trinidad and Tobago'},
{'label':'Tunisia', 'value':'Tunisia'},
{'label':'Turkey', 'value':'Turkey'},
{'label':'Turkmenistan', 'value':'Turkmenistan'},
{'label':'Tuvalu', 'value':'Tuvalu'},
{'label':'Uganda', 'value':'Uganda'},
{'label':'Ukraine', 'value':'Ukraine'},
{'label':'United Arab Emirates', 'value':'United Arab Emirates'},
{'label':'United Kingdom', 'value':'United Kingdom'},
{'label':'United States', 'value':'United States'},
{'label':'Uruguay', 'value':'Uruguay'},
{'label':'Uzbekistan', 'value':'Uzbekistan'},
{'label':'Vanuatu', 'value':'Vanuatu'},
{'label':'Vatican City', 'value':'Vatican City'},
{'label':'Venezuela', 'value':'Venezuela'},
{'label':'Vietnam', 'value':'Vietnam'},
{'label':'Yemen', 'value':'Yemen'},
{'label':'Zambia', 'value':'Zambia'},
{'label':'Zimbabwe', 'value':'Zimbabwe'}
],
value="India" ,  #by default value of country dropbox
        placeholder='select a country',
        style={
             'width': '200px',
               'backgroundColor': '#C8FF11'}),
        html.Label('Choose a cause',
            style={
            'position': 'absolute',
            'font-family': 'Arial, sans-serif',
            'top': '100px',
            'left': '330px',
            'width': '200px'
        }),
        dcc.Dropdown(
            id='dropdown2',
            options=[
{'label':'Outdoor air pollution','value':'Outdoor air pollution'},
{'label':'High systolic blood pressure','value':'High systolic blood pressure'},
{'label':'Diet high in sodium ','value':'Diet high in sodium '},
{'label':'Diet low in whole grains','value':'Diet low in whole grains'},
{'label':'Alcohol use','value':'Alochol use'},
{'label':'Diet low in fruits','value':'Diet low in fruits'},
{'label':'Unsafe water source','value':'Unsafe water source'},
{'label':'Secondhand smoke','value':'Secondhand smoke'},
{'label':'Low birth weight','value':'Low birth weight'},
{'label':'Child wasting','value':'Child wasting'},
{'label':'Unsafe sex','value':'Unsafe sex'},
{'label':'Diet low in nuts and seeds','value':'Diet low in nuts and seeds'},
{'label':'Household air pollution from solid fuels','value':'Household air pollution from solid fuels'},
{'label':'Diet low in vegetables','value':'Diet low in vegetables'},
{'label':'Low physical activity','value':'Low physical activity'},
{'label':'Smoking','value':'Smoking'},
{'label':'High fasting plasma glucose','value':'High fasting plasma glucose'},
{'label':'Air pollution','value':'Air pollution'},
{'label':'Low bone mineral density','value':'Low bone mineral density'},
{'label':'Vitamin A deficiency','value':'Vitamin A deficiency'},
{'label':'Child stunting','value':'Child stunting'},
{'label':'Discontinued breastfeeding','value':'Discontinued breastfeeding'},
{'label':'Iron deficiency','value':'Iron deficiency'},
{'label':'No access to handwashing facility','value':'No access to handwashing facility'}
],
            placeholder='select a cause',
        style={'position': 'absolute',
            'width': '200px',
               'left': '160px',
               'top':'59px',
               'backgroundColor': '#C8FF11'}),
                     dcc.Graph(id="graph1", style={'position': 'absolute', 'top': '600px'}),
                     dcc.Graph(id="graph2", style={'position': 'absolute', 'top': '1100px'}),
                     dcc.Graph(id="graph3", style={'position': 'absolute', 'top': '1600px'}),
                     dcc.Graph(id="graph4", style={'position': 'absolute', 'top': '2100px'}),
                     dcc.Graph(id='choropleth-map', className='choropleth-map', 
                               style={'position': 'absolute', 'top': '170px',
                                      'left': '10px'})],
                     style={
        'border': '2px solid black',  # Outline border style
        'padding': '10px',  # Padding inside the border
        'borderRadius': '5px',  # Rounded corners
        'backgroundColor': '#11ABFF'  # Background color of the dashboard
    })
#========================================================================================
#callback function:
@app.callback(
    [Output("graph1", "figure"),
     Output("graph2", "figure"),
     Output("graph3", "figure"),
     Output("graph4", "figure"),
     Output('choropleth-map', 'figure')],
    [Input("dropdown4", "value"),
     Input("dropdown2", "value"),
     Input("dropdown3", "value"),
     Input("dropdown", "value")])
def update_heatmap(year_selected, selected_cause, selected_year, selected_country):
        filtered_df1=pd.DataFrame(tables[selected_country])
        filtered_df2 = filtered_df1[filtered_df1['Year'] == selected_year]
        fig1=px.imshow(filtered_df1, y=filtered_df1.Year, title=f"Heatmap showing intensity of deaths due to various causes in {selected_country} overtime", color_continuous_scale='Sunsetdark',
                       labels={'x': 'causes of death', 'y': 'Year'})
        fig1.update_layout(height=500, width=1200)
        fig2=px.bar(filtered_df1, x="Year", y=selected_cause,
                    title=f"Number of deaths due to {selected_cause} in {selected_country}")
        fig2.update_traces(marker_color='teal')
        fig2.update_layout(height=500, width=1200)
        fig3 = px.pie(filtered_df2.melt(var_name='causes', value_name='deaths'),
                      names='causes', values='deaths', 
                      title=f"Number of deaths in {selected_country} in the year {selected_year}")
        fig3.update_layout(height=500, width=1200)
        fig4=px.line(filtered_df1, x="Year", y=selected_cause, markers=True,
                    title=f"Line chart of measure of deaths due to {selected_cause} in {selected_country} overtime")
        fig4.update_traces(line_color='Red') 
        fig4.update_layout(height=500, width=1200)  


        filtered_df = df[df['Year'] == year_selected]
        fig = px.choropleth_mapbox(filtered_df,
                                    geojson=world_map_json,
                                    locations='Code',
                                    color=selected_cause,
                                    color_continuous_scale="sunset",
                                    range_color=(0, df[selected_cause].mean()),  # Set range_color as specified
                                        mapbox_style="carto-positron",
                                    zoom=0.4,  # Increase the zoom level
                                    opacity=0.5,
                                    center={"lat": 41, "lon": 28},
                                    labels={selected_cause: selected_cause}
                                    )
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, title_text=f"choropleth map of deaths caused by {selected_cause} in the year {year_selected}")
        fig.update_layout(height=400, width=1200)

        return fig4, fig2, fig1, fig3, fig

if __name__ == '__main__':
    app.run_server()