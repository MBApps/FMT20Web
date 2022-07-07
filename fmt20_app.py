import sys
import streamlit as st
import Fumagalli_Motta_Tarantino_2020 as FMT20

from utilities import *


sys.tracebacklimit = 0
st.set_page_config(
     page_title="Fumagalli et al. (2020)",
     page_icon="https://raw.githubusercontent.com/manuelbieri/Fumagalli_2020/master/assets/visual/logo.svg",
     menu_items={
         'Get help': 'https://manuelbieri.ch/Fumagalli_2020',
         'About': "https://github.com/manuelbieri/Fumagalli_2020",
     },
    layout="wide"
 )


def set_config():
    config = FMT20.LoadParameters(config_id=st.session_state.configs[0])
    st.write(config.params.params)
    st.session_state.model = st.session_state.configs[1]
    st.session_state.development_costs = config.params.params["development_costs"]
    st.session_state.startup_assets = config.params.params["startup_assets"]
    st.session_state.development_success = config.params.params["development_success"]
    st.session_state.success_probability = config.params.params["success_probability"]
    st.session_state.private_benefit = config.params.params["private_benefit"]
    st.session_state.consumer_surplus_without_innovation = config.params.params["consumer_surplus_without_innovation"]
    st.session_state.consumer_surplus_with_innovation = config.params.params["consumer_surplus_with_innovation"]
    st.session_state.consumer_surplus_duopoly = config.params.params["consumer_surplus_duopoly"]
    st.session_state.incumbent_profit_without_innovation = config.params.params["incumbent_profit_without_innovation"]
    st.session_state.incumbent_profit_duopoly = config.params.params["incumbent_profit_duopoly"]
    st.session_state.startup_profit_duopoly = config.params.params["startup_profit_duopoly"]
    st.session_state.incumbent_profit_with_innovation = config.params.params["incumbent_profit_with_innovation"]
    st.write(st.session_state)


with st.sidebar:
    model = st.selectbox('', (FMT20.OptimalMergerPolicy, FMT20.ProCompetitive, FMT20.ResourceWaste), format_func=lambda x:model_label(x), key='model')
    "### Set the model parameters"
    policy = st.selectbox('Merger Policy', (FMT20.MergerPolicies.Strict, FMT20.MergerPolicies.Intermediate_late_takeover_prohibited, FMT20.MergerPolicies.Intermediate_late_takeover_allowed, FMT20.MergerPolicies.Laissez_faire), key='policy')
    K = create_slider("Development Costs", 'development_costs', 'Costs for the development of the product (independent of success)')
    A = create_slider("Start-up Assets", 'startup_assets', 'Assets of the start-up at the beginning')
    p = create_slider("Probability for Development Success", 'success_probability', 'Probability, that the development by the owner of the product is successful')
    B = create_slider("Private Benefit", 'private_benefit', 'Private benefit of the entrepreneur')
    development_success = st.selectbox('Is Development successful if attempted?',(True, False), key='development_success')
    csm = create_slider("Consumer Surplus without Innovation", 'consumer_surplus_without_innovation', '')
    csM = create_slider("Consumer Surplus with Innovation", 'consumer_surplus_with_innovation', '')
    csd = create_slider("Consumer Surplus Duopoly", 'consumer_surplus_duopoly', '')
    pim = create_slider("Incumbent Profit without Innovation", 'incumbent_profit_without_innovation', '')
    piM = create_slider("Incumbent Profit with Innovation", 'incumbent_profit_with_innovation', '')
    piId = create_slider("Incumbent Profit Duopoly", 'incumbent_profit_duopoly', '')
    piSd = create_slider("Start-up Profit Duopoly", 'startup_profit_duopoly', '')
    gamma = create_slider("Substitutability", 'gamma', '')
    # configs = st.selectbox('Available configurations',get_configurations(), format_func=lambda x:configuration_label(x), on_change=set_config, key='configs')


try:
    m = st.session_state.model(
        merger_policy=st.session_state.policy,
        development_costs=st.session_state.development_costs,
        startup_assets=st.session_state.startup_assets,
        success_probability=st.session_state.success_probability,
        private_benefit=st.session_state.private_benefit,
        development_success=st.session_state.development_success,
        consumer_surplus_without_innovation=st.session_state.consumer_surplus_without_innovation,
        consumer_surplus_with_innovation=st.session_state.consumer_surplus_with_innovation,
        consumer_surplus_duopoly=st.session_state.consumer_surplus_duopoly,
        incumbent_profit_without_innovation = st.session_state.incumbent_profit_without_innovation,
        incumbent_profit_duopoly = st.session_state.incumbent_profit_duopoly,
        startup_profit_duopoly = st.session_state.startup_profit_duopoly,
        incumbent_profit_with_innovation = st.session_state.incumbent_profit_with_innovation,
        asset_distribution=FMT20.Distributions.UniformDistribution
    )
    v = FMT20.Overview(m, default_style=False, figsize=(9.5, 7))
    v.plot(fontsize=7, title='', thresholds=True, optimal_policy=True, y_offset=-40)
    v.fig.set_label("Fumagalli et al. (2020)")
    st.pyplot(v.fig, transparent=True, dpi=750)
except AssertionError as e:
    st.write(e)
    with st.expander("Help for Debugging"):
        st.markdown('Visit this [link](https://manuelbieri.ch/Fumagalli_2020/Fumagalli_Motta_Tarantino_2020/Models.html#BaseModel.__init__) to learn about the necessary assumptions.')
