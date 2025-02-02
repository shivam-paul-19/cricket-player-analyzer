import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

odi_bat = pd.read_csv("ODI_bat.csv")
odi_bat = pd.DataFrame(odi_bat)
odi_bowl = pd.read_csv("ODI_bowl.csv")
odi_bowl = pd.DataFrame(odi_bowl)

t20_bat = pd.read_csv("t20_bat.csv")
t20_bat = pd.DataFrame(t20_bat)
t20_bowl = pd.read_csv("t20_bowl.csv")
t20_bowl = pd.DataFrame(t20_bowl)

def getData(player, format, type):
    st.markdown(f"## {player}")
    if(format == "ODI"):
        odi_show(player=player, type=type)
    elif(format == "T20i"):
        t20_show(player=player, type=type)
    else:
        overall_show(player=player, type=type)

def overall_show(player, type):
    is_odi_data = is_t20_data = True
    player_stats_bat_odi = odi_bat.loc[(odi_bat['Player'] == player)]
    if len(player_stats_bat_odi) == 0:
        is_odi_data = False
    player_stats_bowl_odi = odi_bowl.loc[(odi_bowl['Player'] == player)]

    player_stats_bat_t20 = t20_bat.loc[(t20_bat['Player'] == player)]
    if len(player_stats_bat_t20) == 0:
        is_t20_data = False
    player_stats_bowl_t20 = t20_bowl.loc[(t20_bowl['Player'] == player)]
    
    if type == "Batting":
        if not is_t20_data:
            st.error(f"No T20i Batting Data available for {player}. Showing ODI data only")
            bat_ODI(stats=player_stats_bat_odi)
            balls2run_odi(stats=player_stats_bat_odi)
            milestones_ODI_bat(stats=player_stats_bat_odi)
            figures_ODI_bat(stats=player_stats_bat_odi)
            return

        bat_ODI(stats=player_stats_bat_odi)
        bat_t20(stats=player_stats_bat_t20)
        overall_Bat_chart(player=player)
        milestones_chart(player=player)
        bat_figures(player=player)

    elif type == "Bowling":
        if not is_t20_data:
            st.error(f"No T20i Bowling Data available for {player}. Showing ODI data only")
            bowl_ODI(stats=player_stats_bowl_odi)
            balls2wkt_odi(stats=player_stats_bowl_odi)
            milestones_ODI_bowl(stats=player_stats_bowl_odi)
            figures_ODI_bowl(stats=player_stats_bowl_odi)
            return

        bowl_ODI(stats=player_stats_bowl_odi)
        bowl_t20(stats=player_stats_bowl_t20)
        wickets_pie(player=player)
        bowl_figures(player=player)
        milestones_chart_bowl(player=player)

    else:
        if not is_t20_data:
            st.error(f"No T20i Data available for {player}. Showing ODI data only")
            bat_ODI(stats=player_stats_bat_odi)
            balls2run_odi(stats=player_stats_bat_odi)
            milestones_ODI_bat(stats=player_stats_bat_odi)
            figures_ODI_bat(stats=player_stats_bat_odi)

            bowl_ODI(stats=player_stats_bowl_odi)
            balls2wkt_odi(stats=player_stats_bowl_odi)
            milestones_ODI_bowl(stats=player_stats_bowl_odi)
            figures_ODI_bowl(stats=player_stats_bowl_odi)
            return
        
        bat_ODI(stats=player_stats_bat_odi)
        bat_t20(stats=player_stats_bat_t20)
        overall_Bat_chart(player=player)
        milestones_chart(player=player)
        bat_figures(player=player)

        bowl_ODI(stats=player_stats_bowl_odi)
        bowl_t20(stats=player_stats_bowl_t20)
        wickets_pie(player=player)
        bowl_figures(player=player)
        milestones_chart_bowl(player=player)

def odi_show(player, type):
    is_odi_data = True
    player_stats_bat = odi_bat.loc[(odi_bat['Player'] == player)]
    if len(player_stats_bat) == 0:
        is_odi_data = False
    player_stats_bowl = odi_bowl.loc[(odi_bowl['Player'] == player)]

    if not is_odi_data:
        st.error(f"No ODI Data available for {player}")
        return
    
    if type == "Batting":
        bat_ODI(stats=player_stats_bat)
        balls2run_odi(stats=player_stats_bat)
        milestones_ODI_bat(stats=player_stats_bat)
        figures_ODI_bat(stats=player_stats_bat)

    elif type == "Bowling":
        bowl_ODI(stats=player_stats_bowl)
        balls2wkt_odi(stats=player_stats_bowl)
        milestones_ODI_bowl(stats=player_stats_bowl)
        figures_ODI_bowl(stats=player_stats_bowl)

    else:
        bat_ODI(stats=player_stats_bat)
        balls2run_odi(stats=player_stats_bat)
        milestones_ODI_bat(stats=player_stats_bat)
        figures_ODI_bat(stats=player_stats_bat)
    
        bowl_ODI(stats=player_stats_bowl)
        balls2wkt_odi(stats=player_stats_bowl)
        milestones_ODI_bowl(stats=player_stats_bowl)
        figures_ODI_bowl(stats=player_stats_bowl)

def t20_show(player, type):
    is_t20_data = True
    player_stats_bat = t20_bat.loc[(t20_bat['Player'] == player)]
    if len(player_stats_bat) == 0:
        is_t20_data = False
    player_stats_bowl = t20_bowl.loc[(t20_bowl['Player'] == player)]

    if not is_t20_data:
        st.error(f"No T20i Data available for {player}")
        return
    
    if type == "Batting":
        bat_t20(stats=player_stats_bat)
        balls2run_t20(stats=player_stats_bat)
        milestones_t20_bat(stats=player_stats_bat)
        figures_t20_bat(stats=player_stats_bat)
        boundaries_t20(stats=player_stats_bat)
        
    elif type == "Bowling":
        bowl_t20(stats=player_stats_bowl)
        balls2wkt_t20(stats=player_stats_bowl)
        milestones_t20_bowl(stats=player_stats_bowl)
        figures_t20_bowl(stats=player_stats_bowl)
    else:
        bat_t20(stats=player_stats_bat)
        balls2run_t20(stats=player_stats_bat)
        milestones_t20_bat(stats=player_stats_bat)
        figures_t20_bat(stats=player_stats_bat)
        boundaries_t20(stats=player_stats_bat)

        bowl_t20(stats=player_stats_bowl)
        balls2wkt_t20(stats=player_stats_bowl)
        milestones_t20_bowl(stats=player_stats_bowl)
        figures_t20_bowl(stats=player_stats_bowl)

def bowl_t20(stats):
    st.markdown("----")
    st.markdown("### T20i Bowling data")
    span, inn, wkts = list(stats['Span_t20_bowl']), list(stats['Inns_t20_bowl']), list(stats['Wkts_t20'])
    econ, best_wk, best_run = list(stats['Econ_t20']), list(stats['best_wkts_t20']), list(stats['best_runs_given_t20'])
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

def bat_figures(player):
    st.markdown("----")
    st.markdown("### Batting figures")
    odi_sr = odi_bat.loc[(odi_bat['Player'] == player)]['SR_ODI_bat']
    t20_sr = t20_bat.loc[(t20_bat['Player'] == player)]['SR_t20_bat']
    odi_ave = odi_bat.loc[(odi_bat['Player'] == player)]['Ave_ODI_bat']
    t20_ave = t20_bat.loc[(t20_bat['Player'] == player)]['Ave_t20_bat']

    sr = list(odi_sr) + list(t20_sr)
    ave = list(odi_ave) + list(t20_ave)

    figures = pd.DataFrame([sr, ave], columns=["ODI", "T20i"], index=["Strike rate", "Average"])
    st.bar_chart(data=figures, horizontal=True, height=300)

def bowl_figures(player):
    st.markdown("----")
    st.markdown("### Bowling figures")
    odi_sr = odi_bowl.loc[(odi_bowl['Player'] == player)]['SR_ODI_bowl']
    t20_sr = t20_bowl.loc[(t20_bowl['Player'] == player)]['SR_t20_bowl']
    odi_ave = odi_bowl.loc[(odi_bowl['Player'] == player)]['Ave_ODI_bowl']
    t20_ave = t20_bowl.loc[(t20_bowl['Player'] == player)]['Ave_t20_bowl']
    odi_econ = odi_bowl.loc[(odi_bowl['Player'] == player)]['Econ_ODI']
    t20_econ = t20_bowl.loc[(t20_bowl['Player'] == player)]['Econ_t20']

    sr = list(odi_sr) + list(t20_sr)
    ave = list(odi_ave) + list(t20_ave)
    econ = list(odi_econ) + list(t20_econ)

    figures = pd.DataFrame([sr, ave, econ], columns=["ODI", "T20i"], index=["Strike rate", "Average", "Economy"])
    st.bar_chart(data=figures)

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
    st.markdown("----")
    st.markdown("### 100s, 50s and Ducks")
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

def milestones_chart_bowl(player):
    st.markdown("----")
    st.markdown("### 4 $ 5 Wicket hauls")
    _4s_ODI = odi_bowl.loc[(odi_bowl['Player'] == player)]['4_W_ODI']
    _4s_t20 = t20_bowl.loc[(t20_bowl['Player'] == player)]['4_W_t20']
    _5s_ODI = odi_bowl.loc[(odi_bowl['Player'] == player)]['5_W_ODI']
    _5s_t20 = t20_bowl.loc[(t20_bowl['Player'] == player)]['5_W_t20']

    _4s = list(_4s_ODI) + list(_4s_t20)
    _5s = list(_5s_ODI) + list(_5s_t20)

    milestones = pd.DataFrame([_4s, _5s], columns=["ODI", "T20i"], index=["4 Wicket haul", "5 Wicket haul"])
    st.bar_chart(data=milestones, horizontal=True, height=300)

def wickets_pie(player):
    st.markdown("----")
    st.markdown("### Distribution of wickets")
    odi_wkts = odi_bowl.loc[(odi_bowl['Player'] == player)]['Wkts_ODI']
    t20_wkts = t20_bowl.loc[(t20_bowl['Player'] == player)]['Wkts_t20']

    total_wkts = list(odi_wkts) + list(t20_wkts)

    fig = plt.figure(figsize=(5,5))
    plt.pie(total_wkts, labels=["ODI", "T20i"], autopct="%1.1f%%")
    plt.title(f"Total wicket in both formats: {total_wkts[0] + total_wkts[1]}")

    st.pyplot(fig)

def bat_ODI(stats):
    st.markdown("----")
    st.markdown("### ODI Batting data")
    span, inn, run = list(stats['Span_ODI_bat']), list(stats['Inns_ODI_bat']), list(stats['Runs_ODI_bat'])
    sr, hs, isNO = list(stats['SR_ODI_bat']), list(stats['HS_ODI']), list(stats['HS_ODI_isNO'])
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

def bat_t20(stats):
    st.markdown("----")
    st.markdown("### T20i Batting data")
    span, inn, run = list(stats['Span_t20_bat']), list(stats['Inns_t20_bat']), list(stats['Runs_t20_bat'])
    sr, hs, isNO = list(stats['SR_t20_bat']), list(stats['HS_t20']), list(stats['HS_t20_isNO'])
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
    
def bowl_ODI(stats):
    st.markdown("----")
    st.markdown("### ODI Bowling data")
    span, inn, wkts = list(stats['Span_ODI_bowl']), list(stats['Inns_ODI_bowl']), list(stats['Wkts_ODI'])
    econ, best_wk, best_run = list(stats['Econ_ODI']), list(stats['best_wkts_ODI']), list(stats['best_runs_given_ODI'])
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

def balls2run_odi(stats):
    st.markdown("----")
    st.markdown("### ODI Balls-to-Runs data")
    ballNruns = list(stats['BF_ODI']) + list(stats['Runs_ODI_bat'])
    data = pd.DataFrame(ballNruns, columns=['Values'], index=['Balls faced', 'Runs scored'])
    st.table(data=data)
    st.bar_chart(data=data, horizontal=True, height=200, color=["#00ff00"])

def milestones_ODI_bat(stats):
    st.markdown("----")
    st.markdown("### 100s, 50s and Ducks (ODI)")
    milestones = list(stats['100_ODI']) + list(stats['50_ODI']) + list(stats['0_ODI'])
    if any(milestones):
        fig = plt.figure(figsize=(4,4))
        plt.pie(milestones, labels=["100s", "50s", "0s"], autopct="%1.1f%%")
        st.pyplot(fig)
    else:
        st.table(pd.DataFrame(milestones, index=["100s", "50s", "0s"]))

def figures_ODI_bat(stats):
    st.markdown("----")
    st.markdown("### Batting figures (ODI)")
    odi_fig = list(stats['SR_ODI_bat']) + list(stats['Ave_ODI_bat'])
    odi_fig = pd.DataFrame(odi_fig, index=["Strike rate", "Average"])
    st.bar_chart(data=odi_fig, color=['#f7e520'])

def balls2run_t20(stats):
    st.markdown("----")
    st.markdown("### T20i Balls-to-Runs data")
    ballNruns = list(stats['BF_t20']) + list(stats['Runs_t20_bat'])
    data = pd.DataFrame(ballNruns, columns=['Values'], index=['Balls faced', 'Runs scored'])
    st.table(data=data)
    st.bar_chart(data=data, horizontal=True, height=200, color=["#00ff00"])

def milestones_t20_bat(stats):
    st.markdown("----")
    st.markdown("### 100s, 50s and Ducks (T20i)")
    milestones = list(stats['100_t20']) + list(stats['50_t20']) + list(stats['0_t20'])
    if any(milestones):
        fig = plt.figure(figsize=(4,4))
        plt.pie(milestones, labels=["100s", "50s", "0s"], autopct="%1.1f%%")
        st.pyplot(fig)
    else:
        st.table(pd.DataFrame(milestones, index=["100s", "50s", "0s"]))

def figures_t20_bat(stats):
    st.markdown("----")
    st.markdown("### Batting figures (T20i)")
    odi_fig = list(stats['SR_t20_bat']) + list(stats['Ave_t20_bat'])
    odi_fig = pd.DataFrame(odi_fig, index=["Strike rate", "Average"])
    st.bar_chart(data=odi_fig, color=['#f7e520'])

def boundaries_t20(stats):
    st.markdown("----")
    st.markdown("### Boundaries distribution")
    boundaries = list(stats['4s_t20']) + list(stats['6s_t20'])
    st.table(pd.DataFrame(boundaries, columns=["Values"] ,index=["4s", "6s"]))
    if any(boundaries):
        fig = plt.figure(figsize=(4,4))
        plt.pie(boundaries, labels=["Fours", "Sixes"], autopct="%1.1f%%")
        st.pyplot(fig)

def balls2wkt_odi(stats):
    st.markdown("----")
    st.markdown("### Balls Delivered, Runs Given and Wickers taken (ODI)")
    ballNwkt = list(stats['Balls_del_ODI']) + list(stats['Runs_given_ODI']) + list(stats['Wkts_ODI'])
    data = pd.DataFrame(ballNwkt, columns=['Values'], index=['Balls delivered', 'Runs given', 'Wickets taken'])
    st.table(data=data)
    st.bar_chart(data=data, horizontal=True, height=200, color=["#00ff00"])

def balls2wkt_t20(stats):
    st.markdown("----")
    st.markdown("### Balls Delivered, Runs Given and Wickers taken (T20i)")
    ballNwkt = list(stats['Balls_del_t20']) + list(stats['Runs_given_t20']) + list(stats['Wkts_t20'])
    data = pd.DataFrame(ballNwkt, columns=['Values'], index=['Balls delivered', 'Runs given', 'Wickets taken'])
    st.table(data=data)
    st.bar_chart(data=data, horizontal=True, height=200, color=["#00ff00"])

def milestones_t20_bowl(stats):
    st.markdown("----")
    st.markdown("### 4 & 5 Wicket hauls (T20i)")
    milestones = list(stats['4_W_t20']) + list(stats['5_W_t20'])
    if any(milestones):
        fig = plt.figure(figsize=(4,4))
        plt.pie(milestones, labels=["4W hauls", "5W hauls"], autopct="%1.1f%%")
        st.pyplot(fig)
    else:
        st.table(pd.DataFrame(milestones, index=["4 Wicket haul", "5 Wicket haul"]))

def milestones_ODI_bowl(stats):
    st.markdown("----")
    st.markdown("### 4 & 5 Wicket hauls (ODI)")
    milestones = list(stats['4_W_ODI']) + list(stats['5_W_ODI'])
    if any(milestones):
        fig = plt.figure(figsize=(4,4))
        plt.pie(milestones, labels=["4W hauls", "5W hauls"], autopct="%1.1f%%")
        st.pyplot(fig)
    else:
        st.table(pd.DataFrame(milestones, index=["4 Wicket haul", "5 Wicket haul"]))

def figures_ODI_bowl(stats):
    st.markdown("----")
    st.markdown("### Bowling figures (ODI)")
    odi_fig = list(stats['SR_ODI_bowl']) + list(stats['Ave_ODI_bowl']) + list(stats['Econ_ODI'])
    odi_fig = pd.DataFrame(odi_fig, index=["Strike rate", "Average", "Economy"])
    st.bar_chart(data=odi_fig, color=['#f7e520'])

def figures_t20_bowl(stats):
    st.markdown("----")
    st.markdown("### Bowling figures (T20i)")
    odi_fig = list(stats['SR_t20_bowl']) + list(stats['Ave_t20_bowl']) + list(stats['Econ_t20'])
    odi_fig = pd.DataFrame(odi_fig, index=["Strike rate", "Average", "Economy"])
    st.bar_chart(data=odi_fig, color=['#f7e520'])
