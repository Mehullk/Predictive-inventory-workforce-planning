from streamlit_option_menu import option_menu
import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div style="padding-top:10px;padding-bottom:20px;">

            <div class="brand-title">
            📊 Predictive AI
            </div>

            <div class="brand-subtitle">
            Inventory & Workforce Planning
            </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        selected = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "Forecast",
                "Inventory",
                "Workforce",
                "Insights",
            ],
            icons=[
                "speedometer2",
                "graph-up-arrow",
                "boxes",
                "people-fill",
                "lightbulb-fill",
            ],
            default_index=0,
            styles={
    "container": {
        "padding": "0!important",
        "background-color": "#111827",
    },

    "icon": {
        "color": "#60A5FA",
        "font-size": "20px",
    },

    "nav-link": {
        "font-size": "17px",
        "font-weight": "600",

        "color": "#F8FAFC",          # FIX

        "text-align": "left",

        "margin": "6px 0",

        "padding": "14px",

        "border-radius": "12px",

        "--hover-color": "#22344D",
    },

    "nav-link-selected": {
        "background-color": "#2563EB",
        "color": "#FFFFFF",          # FIX
        "font-weight": "700",
    },
}
        )

        st.markdown("---")

        st.markdown(
            """
            <div class="card">

            <b>🤖 AI Model</b>

            <br><br>

            <span class="success">● Prophet Loaded</span>

            <br>

            <span style="color:#CBD5E1;">
            Inventory Planner Ready
            </span>

            <br>

            <span style="color:#CBD5E1;">
            Workforce Planner Ready
            </span>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.caption("Version 1.0")

    return selected