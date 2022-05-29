import streamlit as st

import Fumagalli_Motta_Tarantino_2020 as FMT20


def create_slider(label: str, param: str, help_label: str = ''):
    return st.slider(label, 0.0, 1.0, get_default_value(param), 0.01, help=help_label)

def get_default_value(param: str, model=FMT20.BaseModel):
    args_name = model.__init__.__code__.co_varnames[1:]  # "self" is not needed
    default_value = model.__init__.__defaults__
    arg_index = args_name.index(f"{param}")
    return default_value[arg_index]
