import streamlit as st


def section_title(title: str, subtitle: str = ""):
    st.title(title)

    if subtitle:
        st.caption(subtitle)

    st.write("")


def kpi_card(title, value, delta=None, delta_color="normal", icon="📊"):

    with st.container(border=True):

        left, right = st.columns([4, 1])

        with left:
            st.caption(title)

            st.markdown(
                f"""
### {value}
"""
            )

            if delta:

                if delta_color == "#22C55E":
                    st.success(delta)

                elif delta_color == "#EF4444":
                    st.error(delta)

                elif delta_color == "#F59E0B":
                    st.warning(delta)

                else:
                    st.info(delta)

        with right:
            st.markdown(f"# {icon}")


def info_card(title, body):

    with st.container(border=True):

        st.subheader(title)

        st.write(body)


def status_card(title, status):

    with st.container(border=True):

        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(title)

        with col2:

            if status.lower() == "critical":
                st.error(status)

            elif status.lower() == "warning":
                st.warning(status)

            else:
                st.success(status)