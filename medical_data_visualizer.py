import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = np.where((df['weight']/np.square(df['height']/100))>25,1,0)

# 3
df["cholesterol"] = np.where(df["cholesterol"] ==1,0,1)
df["gluc"] = np.where(df["gluc"]==1,0,1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])


    # 6
    figure =sns.catplot(x="variable",kind="count",hue="value",data=df_cat,col="cardio")
    

    # 7

    figure.set_axis_labels("variable","total")

    # 8
    fig = figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df["ap_hi"]) & (df["height"] >= df["height"].quantile(0.025)) & (df["height"] <= df["height"].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025))&(df['weight'] >= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12,12))

    # 15

    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', square=True, linewidths=1,
                cbar_kws={"shrink": 0.5}, vmin=-0.1, vmax=0.25)

    # 16
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
draw_heat_map()