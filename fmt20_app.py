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
    K = create_slider("Development Costs", 'development_costs', 'Costs for the development of the product (independent of success)')
    A = create_slider("Start-up Assets", 'startup_assets', 'Assets of the start-up at the beginning')
    p = create_slider("Probability for Development Success", 'success_probability', 'Probability, that the development by the owner of the product is successful')
    B = create_slider("Private Benefit", 'private_benefit', 'Private benefit of the entrepreneur')
    development_success = st.selectbox('Is Development successful if attempted?',(True, False))
    show_legend = st.checkbox('Show legends', value=True)

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
    v1.plot(legend=show_legend)
    v2.plot(legend=show_legend)
    v3.plot(legend=show_legend)
    st.pyplot(v1.fig, transparent=True)
    st.pyplot(v2.fig, transparent=True)
    st.pyplot(v3.fig, transparent=True)
except AssertionError as e:
    st.write(e)
    with st.expander("Help for Debugging"):
        st.markdown('Visit this [link](https://manuelbieri.ch/Fumagalli_2020/Fumagalli_Motta_Tarantino_2020/Models.html#BaseModel.__init__) to learn about the necessary assumptions.')
