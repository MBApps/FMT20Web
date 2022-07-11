import streamlit as st
import Fumagalli_Motta_Tarantino_2020 as FMT20
import Fumagalli_Motta_Tarantino_2020.Notebooks.NotebookUtilities as FMT20_NB


def create_slider(label: str, key: str, default_key: str = ''):
    if key not in st.session_state:
        default_key = key if default_key == '' else default_key
        st.session_state[key] = get_default_value(default_key)
    return st.slider(label, min_value=0.0, max_value=1.0, step=0.001, key=key, help=get_doc_string(key))


def get_doc_string(attr: str) -> str:
    try:
        return getattr(FMT20.CoreModel, attr).__doc__
    except AttributeError:
        return getattr(FMT20.CournotCompetition, attr).__doc__



def get_default_value(param: str, model=FMT20.CoreModel):
    try:
        args_name = model.__init__.__code__.co_varnames[1:]  # "self" is not needed
        default_value = model.__init__.__defaults__
        arg_index = args_name.index(f"{param}")
        return default_value[arg_index]
    except ValueError:
        return 0.3

def model_label(m: FMT20.OptimalMergerPolicy) -> str:
    if m == FMT20.OptimalMergerPolicy:
        return "Optimal Merger Policy"
    if m == FMT20.ProCompetitive:
        return "Pro-Competitive"
    if m == FMT20.ResourceWaste:
        return "Resource Waste"


def get_configurations() -> list[tuple[int, type(FMT20.OptimalMergerPolicy)]]:
    output = []
    for i in range(0, 60):
        try:
            m = FMT20_NB.get_model_by_id(i)
            output.append((i, type(m)))
        except FMT20.IDNotAvailableError:
            pass
    return output

def configuration_label(t: tuple[int, type(FMT20.OptimalMergerPolicy)]) -> str:
    return f"{t[0]} - {model_label(t[1])}"

