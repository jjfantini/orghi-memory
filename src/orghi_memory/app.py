"""Streamlit app."""

from importlib.metadata import version

import streamlit as st

st.title(f"orghi-memory v{version('orghi-memory')}")  # type: ignore[no-untyped-call]
