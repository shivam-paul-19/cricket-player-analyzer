import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

odi_bat = pd.read_csv(r"cleaned_data\ODI_bat.csv")
odi_bat = pd.DataFrame(odi_bat)
odi_bowl = pd.read_csv(r"cleaned_data\ODI_bowl.csv")
odi_bowl = pd.DataFrame(odi_bowl)

t20_bat = pd.read_csv(r"cleaned_data\t20_bat.csv")
t20_bat = pd.DataFrame(t20_bat)
t20_bowl = pd.read_csv(r"cleaned_data\t20_bowl.csv")
t20_bowl = pd.DataFrame(t20_bowl)

def getData(player, format, type):
    st.markdown(f"## {player}")
    if(format == "ODI"):
        odi_show(player=player, type=type)
    elif(format == "T20i"):
        t20_show(player=player, type=type)
    else:
        odi_show(player=player, type=type)
        t20_show(player=player, type=type)

def odi_show(player, type):
    st.markdown(f"### *ODI data ({type})*")
    player_stats_bat = odi_bat.loc[(odi_bat['Player'] == player)]
    if len(player_stats_bat) == 0:
        st.markdown("#### *>> No data available*")
        return
    player_stats_bowl = odi_bowl.loc[(odi_bowl['Player'] == player)]
    
    if type == "Batting":
        span, inn, run = list(player_stats_bat['Span_ODI_bat']), list(player_stats_bat['Inns_ODI_bat']), list(player_stats_bat['Runs_ODI_bat'])
        sr, hs, isNO = list(player_stats_bat['SR_ODI_bat']), list(player_stats_bat['HS_ODI']), list(player_stats_bat['HS_ODI_isNO'])
        if isNO:
            hs = f"{hs[0]}*"
        if span[0] == 0:
            span[0] = "<1"

        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)
        col1.markdown(f"### {span[0]}\nYears Played")
        col2.markdown(f"### {inn[0]}\nInnings played")
        col3.markdown(f"### {run[0]}\nRuns Scored")

        col4.markdown(f"### {sr[0]}\nStrike rate")
        col5.markdown(f"### {hs}\nHighest score")
    elif type == "Bowling":
        span, inn, wkts = list(player_stats_bat['Span_ODI_bat']), list(player_stats_bat['Inns_ODI_bat']), list(player_stats_bowl['Wkts_ODI'])
        econ, best_wk, best_run = list(player_stats_bowl['Econ_ODI']), list(player_stats_bowl['best_wkts_ODI']), list(player_stats_bowl['best_runs_given_ODI'])
        bbi = f"{best_wk[0]}/{best_run[0]}"
        if span[0] == 0:
            span[0] = "<1"

        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)
        col1.markdown(f"### {span[0]}\nYears Played")
        col2.markdown(f"### {inn[0]}\nInnings played")
        col3.markdown(f"### {wkts[0]}\nWickets taken")

        col4.markdown(f"### {econ[0]}\nEconomy")
        col5.markdown(f"### {bbi}\nBest Bowling")
    else:
        span, match, run, wkts = list(player_stats_bat['Span_ODI_bat']), list(player_stats_bat['Inns_ODI_bat']), list(player_stats_bat['Runs_ODI_bat']), list(player_stats_bowl['Wkts_ODI'])
        if span[0] == 0:
            span[0] = "<1"
        col1, col2, col3, col4 = st.columns(4)
        col1.markdown(f"### {span[0]}\nYears Played")
        col2.markdown(f"### {match[0]}\nInnings played")
        col3.markdown(f"### {run[0]}\nRuns Scored")
        col4.markdown(f"### {wkts[0]}\nWickets taken")

def t20_show(player, type):
    st.markdown(f"### *T20i data ({type})*")
    player_stats_bat = t20_bat.loc[(t20_bat['Player'] == player)]
    if len(player_stats_bat) == 0:
        st.markdown("#### *>> No data available*")
        return
    player_stats_bowl = t20_bowl.loc[(t20_bowl['Player'] == player)]

    if type == "Batting":
        span, inn, run = list(player_stats_bat['Span_t20_bat']), list(player_stats_bat['Inns_t20_bat']), list(player_stats_bat['Runs_t20_bat'])
        sr, hs, isNO = list(player_stats_bat['SR_t20_bat']), list(player_stats_bat['HS_t20']), list(player_stats_bat['HS_t20_isNO'])
        if isNO:
            hs = f"{hs[0]}*"
        if span[0] == 0:
            span[0] = "<1"

        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)
        col1.markdown(f"### {span[0]}\nYears Played")
        col2.markdown(f"### {inn[0]}\nInnings played")
        col3.markdown(f"### {run[0]}\nRuns Scored")

        col4.markdown(f"### {sr[0]}\nStrike rate")
        col5.markdown(f"### {hs}\nHighest score")
        overall_Bat_chart(player=player)
        milestones_chart(player=player)
        
    elif type == "Bowling":
        span, inn, wkts = list(player_stats_bat['Span_t20_bat']), list(player_stats_bat['Inns_t20_bat']), list(player_stats_bowl['Wkts_t20'])
        econ, best_wk, best_run = list(player_stats_bowl['Econ_t20']), list(player_stats_bowl['best_wkts_t20']), list(player_stats_bowl['best_runs_given_t20'])
        bbi = f"{best_wk[0]}/{best_run[0]}"
        if span[0] == 0:
            span[0] = "<1"

        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)
        col1.markdown(f"### {span[0]}\nYears Played")
        col2.markdown(f"### {inn[0]}\nInnings played")
        col3.markdown(f"### {wkts[0]}\nWickets taken")

        col4.markdown(f"### {econ[0]}\nEconomy")
        col5.markdown(f"### {bbi}\nBest Bowling")
    else:
        span, inn, run, wkts = list(player_stats_bat['Span_t20_bat']), list(player_stats_bat['Inns_t20_bat']), list(player_stats_bat['Runs_t20_bat']), list(player_stats_bowl['Wkts_t20'])
        if span[0] == 0:
            span[0] = "<1"
        col1, col2, col3, col4 = st.columns(4)
        col1.markdown(f"### {span[0]}\nYears Played")
        col2.markdown(f"### {inn[0]}\nInnings played")
        col3.markdown(f"### {run[0]}\nRuns Scored")
        col4.markdown(f"### {wkts[0]}\nWickets taken")

def overall_Bat_chart(player):
    odi_runs = odi_bat.loc[(odi_bat['Player'] == player)]['Runs_ODI_bat']
    t20_runs = t20_bat.loc[(t20_bat['Player'] == player)]['Runs_t20_bat']

    total_runs = list(odi_runs) + list(t20_runs)

    fig1 = plt.figure(figsize=(4,4))
    plt.pie(total_runs, labels=["ODI", "T20i"], autopct="%1.2f%%", colors=["#0000ff", "#ff0000"])
    plt.title(f"Total runs in all format: {total_runs[0] + total_runs[1]}")

    st.markdown("----")
    st.markdown("### Distribution of runs")
    st.pyplot(fig1)

def milestones_chart(player):
    st.markdown("### *100s*, *50s* and *Ducks*")
    _100s_ODI = odi_bat.loc[(odi_bat['Player'] == player)]['100_ODI']
    _100s_t20 = t20_bat.loc[(t20_bat['Player'] == player)]['100_t20']
    _50s_ODI = odi_bat.loc[(odi_bat['Player'] == player)]['50_ODI']
    _50s_t20 = t20_bat.loc[(t20_bat['Player'] == player)]['50_t20']
    _0s_ODI = odi_bat.loc[(odi_bat['Player'] == player)]['0_ODI']
    _0s_t20 = t20_bat.loc[(t20_bat['Player'] == player)]['0_t20']

    cents = list(_100s_ODI) + list(_100s_t20) 
    fifties = list(_50s_ODI) + list(_50s_t20)
    ducks = list(_0s_ODI) + list(_0s_t20)
    milestones = pd.DataFrame([cents, fifties, ducks], columns=["ODI", "T20i"], index=["100s", "50s", "Ducks"])

    st.bar_chart(data=milestones, color=["#0000ff", "#ff0000"])