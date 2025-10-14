import plotly.graph_objects as go

#########################################################################################################################################
# (CONDITION FILTERS AND COLOR FUNCTION)
def cond(df, indicator, timeframe, color_by):

    # (Conditions Filters) 
    c  = f'{indicator}_{timeframe}_{color_by}'
    ih = df[df[c] >= 4]
    eh = df[(df[c] >= 3) & (df[c] < 4)]
    rh = df[(df[c] >= 2) & (df[c] < 3)]
    h  = df[(df[c] >= 1.5) & (df[c] < 2)]
    l  = df[(df[c] <= -1.5) & (df[c] > -2)]
    rl = df[(df[c] <= -2) & (df[c] > -3)]
    el = df[(df[c] <= -3) & (df[c] > -4)]
    il = df[df[c] <= -4]
    n= df[(df[c] <= 1.5) &(df[c] >= -1.5)]

    # (Names and Colors)
    dict = {
        f"{indicator} Zscore (>4)": [ih, "rgb(136, 14, 79)"],
        f"{indicator} Zscore (>3)": [eh, "rgb(211, 47, 47)"],
        f"{indicator} Zscore (>2)": [rh, "rgb(255, 143, 0)"],
        f"{indicator} Zscore (>1.5)": [h, "rgb(255, 241, 118)"],
        f"{indicator} Zscore (<-1.5)": [l, "rgb(128, 222, 234)"],
        f"{indicator} Zscore (<-2)": [rl, "rgb(41, 182, 246)"],
        f"{indicator} Zscore (<-3)": [el, "rgb(25, 118, 210)"],
        f"{indicator} Zscore (<-4)": [il, "rgb(26, 35, 126)"],
        f"{indicator} Neutral" : [n, "rgb(158, 158, 158)"]
    }
    return dict    

#########################################################################################################################################
# (CANDLE FUNCTION)
def candle(df, indicator, name, color, row, fig):
              
    fig.add_trace(
        go.Candlestick(
            x=df["datetime"],
            open=df[f"open_{indicator}"],
            close=df[f"close_{indicator}"],
            high=df[f"high_{indicator}"],
            low=df[f"low_{indicator}"],
            increasing=dict(
                            fillcolor=color,
                            line=dict(color=color)
                            ),
            decreasing=dict(
                            fillcolor=color,
                            line=dict(color=color)
                            ),
            name=name,
            showlegend=False
        ),
        row=row,
        col=1         
    )
####################################################################################################################################################################
# (Bar function)
def bar(df, indicator, name, color, row, fig):
    
    fig.add_trace(
                go.Bar(
                        x=df["datetime"],
                        y=df[indicator],
                        marker=dict(color=color),
                        name=name,
                        showlegend=False
                        ),
                row=row, 
                col=1
                )
    
####################################################################################################################################################################   
# (Line function)
def line(df, name, line, color, width, row, fig):

    fig.add_trace(
        go.Scatter(
            x=df["datetime"],
            y=line,
            line=dict(color=color, width=width),
            name=name,
            showlegend=False,
            ),
        row=row,
        col=1   
    )