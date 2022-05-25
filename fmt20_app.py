import sys
import streamlit as st
from Fumagalli_Motta_Tarantino_2020 import Models, Visualize

st.set_page_config(
     page_title="Home",
     page_icon="🧊",
     menu_items={
         'Get help': 'https://manuelbieri.ch/Fumagalli_2020',
         'About': "https://github.com/manuelbieri/Fumagalli_2020",
     }
 )

"## Implementation of Fumagalli et al. (2020)"
sys.tracebacklimit = 0
p = st.slider("P", 0.0, 1.0, 0.7, 0.01)
try:
    m = Models.OptimalMergerPolicy(success_probability=p)
    v1 = Visualize.Timeline(m)
    v2 = Visualize.AssetRange(m)
    v3 = Visualize.MergerPoliciesAssetRange(m)

    v1.plot()
    v2.plot()
    v3.plot()
    st.pyplot(v1.fig)
    st.pyplot(v2.fig)
    st.pyplot(v3.fig)
except AssertionError as e:
    st.write(e)



