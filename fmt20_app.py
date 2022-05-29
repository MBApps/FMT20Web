import sys
import streamlit as st

from utilities import *
from Fumagalli_Motta_Tarantino_2020 import Models, Visualize


sys.tracebacklimit = 0

st.set_page_config(
     page_title="Home",
     page_icon="🧊",
     menu_items={
         'Get help': 'https://manuelbieri.ch/Fumagalli_2020',
         'About': "https://github.com/manuelbieri/Fumagalli_2020",
     }
 )

"""
## Implementation of Fumagalli et al. (2020)

Set the parameters of the model on the left side.
"""

with st.sidebar:
    "#### Set the model parameters below"
    K = create_slider("Development Costs", 'development_costs')
    A = create_slider("Start-up Assets", 'startup_assets')
    p = create_slider("Probability for Development Success", 'success_probability')
    B = create_slider("Private Benefit", 'private_benefit')
    development_success = st.selectbox('Is Development successful if attempted?',(True, False))
try:
    m = Models.OptimalMergerPolicy(
        development_costs=K,
        startup_assets=A,
        success_probability=p,
        private_benefit=B,
        development_success=development_success
    )
    v1 = Visualize.Timeline(m)
    v2 = Visualize.AssetRange(m)
    v3 = Visualize.MergerPoliciesAssetRange(m)
    v1.plot()
    v2.plot()
    v3.plot()
    st.pyplot(v1.fig, transparent=True)
    st.pyplot(v2.fig, transparent=True)
    st.pyplot(v3.fig, transparent=True)
except AssertionError as e:
    st.write(e)
    with st.expander("Show assumption for debugging"):
        "These are the assumptions made in the model."



