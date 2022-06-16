import sys
import streamlit as st
import Fumagalli_Motta_Tarantino_2020 as FMT20

from utilities import *


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
    show_legend = st.checkbox('Show legends', value=False)
    # config_id = st.number_input('Enter Configuration ID:',min_value=1, max_value=40, value=1, step=1)

try:
    m = FMT20.OptimalMergerPolicy(
        development_costs=K,
        startup_assets=A,
        success_probability=p,
        private_benefit=B,
        development_success=development_success
    )
    v1 = FMT20.Timeline(m)
    v2 = FMT20.Payoffs(m)
    v3 = FMT20.MergerPoliciesAssetRange(m)
    v1.plot(legend=show_legend)
    v2.plot(legend=show_legend)
    v3.plot(legend=show_legend, thresholds=True, y_offset=-60)
    "At first have a look at the payoffs of the model."
    st.pyplot(v2.fig, transparent=True)
    "Now let us focus on the timeline of events in the model."
    st.pyplot(v1.fig, transparent=True)
    "What happens for different merger policies?"
    st.pyplot(v3.fig, transparent=True)
except AssertionError as e:
    st.write(e)
    with st.expander("Help for Debugging"):
        st.markdown('Visit this [link](https://manuelbieri.ch/Fumagalli_2020/Fumagalli_Motta_Tarantino_2020/Models.html#BaseModel.__init__) to learn about the necessary assumptions.')
