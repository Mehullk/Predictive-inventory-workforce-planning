import plotly.express as px
import plotly.graph_objects as go


def apply_theme(fig):

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="#182538",
        plot_bgcolor="#182538",

        font=dict(
            family="Inter",
            color="#F8FAFC",
            size=14,
        ),

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20,
        ),

        title_font=dict(
            size=20,
            color="white",
        ),

        legend=dict(
            orientation="h",
            y=1.08,
            bgcolor="rgba(0,0,0,0)",
        ),

        hoverlabel=dict(
            bgcolor="#22344D",
            font_size=14,
        ),

    )

    fig.update_xaxes(

        showgrid=True,
        gridcolor="#2B3C52",
        zeroline=False,
        showline=False,

    )

    fig.update_yaxes(

        showgrid=True,
        gridcolor="#2B3C52",
        zeroline=False,
        showline=False,

    )

    return fig


def forecast_chart(df):

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=df["Date"],
            y=df["PredictedUnitsSold"],

            mode="lines",

            line=dict(
                color="#3B82F6",
                width=4,
            ),

            name="Forecast",

        )

    )

    if "Upper95CI" in df.columns and "Lower95CI" in df.columns:

        fig.add_trace(

            go.Scatter(

                x=df["Date"],
                y=df["Upper95CI"],

                mode="lines",

                line=dict(width=0),

                showlegend=False,

            )

        )

        fig.add_trace(

            go.Scatter(

                x=df["Date"],
                y=df["Lower95CI"],

                mode="lines",

                fill="tonexty",

                fillcolor="rgba(59,130,246,0.20)",

                line=dict(width=0),

                name="95% Confidence",

            )

        )

    fig.update_layout(
        title="90-Day Sales Forecast"
    )

    return apply_theme(fig)


def inventory_chart(df):

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=df["Date"],
            y=df["ClosingStock"],

            mode="lines",

            name="Closing Stock",

            line=dict(
                color="#22C55E",
                width=4,
            ),

        )

    )

    if "ReorderPoint" in df.columns:

        if df["ReorderPoint"].nunique() == 1:

            fig.add_hline(

                y=df["ReorderPoint"].iloc[0],

                line_color="#EF4444",

                line_dash="dash",

                annotation_text="Reorder Point",

            )

        else:

            fig.add_trace(

                go.Scatter(

                    x=df["Date"],
                    y=df["ReorderPoint"],

                    mode="lines",

                    name="Reorder Point",

                    line=dict(

                        color="#EF4444",

                        dash="dash",

                        width=3,

                    ),

                )

            )

    if "SafetyStock" in df.columns:

        if df["SafetyStock"].nunique() == 1:

            fig.add_hline(

                y=df["SafetyStock"].iloc[0],

                line_color="#FACC15",

                line_dash="dot",

                annotation_text="Safety Stock",

            )

        else:

            fig.add_trace(

                go.Scatter(

                    x=df["Date"],
                    y=df["SafetyStock"],

                    mode="lines",

                    name="Safety Stock",

                    line=dict(

                        color="#FACC15",

                        dash="dot",

                        width=3,

                    ),

                )

            )

    fig.update_layout(

        title="Inventory Levels"

    )

    return apply_theme(fig)


def workforce_chart(df):

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=df["Date"],
            y=df["RequiredWorkers"],

            name="Required Workers",

            marker_color="#F59E0B",

        )

    )

    fig.add_trace(

        go.Scatter(

            x=df["Date"],
            y=df["CurrentStaff"],

            mode="lines",

            name="Current Staff",

            line=dict(

                color="#3B82F6",

                width=4,

            ),

        )

    )

    fig.update_layout(

        title="Workforce Requirement",

        barmode="group",

    )

    return apply_theme(fig)