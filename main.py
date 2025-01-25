import streamlit as st
import pandas as pd
import numpy as np

import analyzer

player_df = pd.read_csv(r"cleaned_data\ODI_bat.csv")
player_df = pd.DataFrame(player_df)

player_names = np.concatenate((np.array(["None"]), np.array(player_df['Player'])))

sideBar = st.sidebar

st.title("Cricket player Analyzer!🏏")
st.write("Know all the cricket related analysis at this one spot")
st.write("(Note: The information is limited to year 2019)")

sideBar.title("Choose the player")
player = sideBar.selectbox("Select", player_names)
format = sideBar.selectbox("Select the format", ["Overall", "ODI", "T20i"])
type = sideBar.selectbox("Select the type of Analysis", ["Overall", "Batting", "Bowling"])

if sideBar.button("Done"):
    if player == "None":
        sideBar.error("Select a player name")
    else:
        st.markdown("----")
        analyzer.getData(player=player, format=format, type=type)