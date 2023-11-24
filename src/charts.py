import plotly.express as px

def pct_ingresos_sobre_gasto_fig(df):
    fig = px.line(
        data_frame=df,
        x='year',
        y='pct_ingresos',
        title='% de ingresos sobre el gasto',
    )
    fig.update_xaxes(tickmode='linear')
    fig.update_yaxes(rangemode='tozero')
    return fig