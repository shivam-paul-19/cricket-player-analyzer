import pandas as pd
import numpy as np
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
    player_stats_bat = odi_bat.loc[(odi_bat['Player'] == player)]
    if len(player_stats_bat) == 0:
        st.markdown("#### *>> No data available*")
        return
    player_stats_bowl = odi_bowl.loc[(odi_bowl['Player'] == player)]
    
    if type == "Batting":
        st.markdown("### *ODI data (Overall)*")
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
        st.markdown("### *ODI data (Overall)*")
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
        st.markdown("### *ODI data (Overall)*")
        span, match, run, wkts = list(player_stats_bat['Span_ODI_bat']), list(player_stats_bat['Inns_ODI_bat']), list(player_stats_bat['Runs_ODI_bat']), list(player_stats_bowl['Wkts_ODI'])
        if span[0] == 0:
            span[0] = "<1"
        col1, col2, col3, col4 = st.columns(4)
        col1.markdown(f"### {span[0]}\nYears Played")
        col2.markdown(f"### {match[0]}\nInnings played")
        col3.markdown(f"### {run[0]}\nRuns Scored")
        col4.markdown(f"### {wkts[0]}\nWickets taken")

def t20_show(player, type):
    player_stats_bat = t20_bat.loc[(t20_bat['Player'] == player)]
    if len(player_stats_bat) == 0:
        st.markdown("#### *>> No data available*")
        return
    player_stats_bowl = t20_bowl.loc[(t20_bowl['Player'] == player)]

    if type == "Batting":
        st.markdown("### *T20i data (Batting)*")
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
        
    elif type == "Bowling":
        st.markdown("### *T20i data (Bowling)*")
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
        st.markdown("### *T20i data (Overall)*")
        span, inn, run, wkts = list(player_stats_bat['Span_t20_bat']), list(player_stats_bat['Inns_t20_bat']), list(player_stats_bat['Runs_t20_bat']), list(player_stats_bowl['Wkts_t20'])
        if span[0] == 0:
            span[0] = "<1"
        col1, col2, col3, col4 = st.columns(4)
        col1.markdown(f"### {span[0]}\nYears Played")
        col2.markdown(f"### {inn[0]}\nInnings played")
        col3.markdown(f"### {run[0]}\nRuns Scored")
        col4.markdown(f"### {wkts[0]}\nWickets taken")
