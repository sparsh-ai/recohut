#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Functions to generate plots."""


from typing import Dict, List, Tuple, Union

import altair as alt
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go
from pandas import DataFrame

# pylint: disable=invalid-name
# pylint: disable=too-many-locals
# pylint: disable=dangerous-default-value
# pylint: disable=too-many-arguments


alt.data_transformers.disable_max_rows()
alt.renderers.set_embed_options(actions=False)
alt.renderers.set_embed_options(
    padding={"left": 0, "right": 0, "bottom": 0, "top": 0}
)


def convert_df_to_format_for_plotly_heatmap(
    df: DataFrame, df_annot: DataFrame, log_scale: bool = False
) -> Dict:
    """Convert pandas.DataFrame into format compatible with plotly heatmap."""
    return {
        "z": np.log1p(df).to_numpy().tolist()
        if log_scale
        else df.to_numpy().tolist(),
        "x": df.columns.tolist(),
        "y": df.index.tolist(),
        "annotation_text": df_annot.to_numpy().tolist(),
    }


def altair_plot_grid_by_column(
    df: DataFrame,
    xvar: str,
    yvar: str,
    col2grid: str,
    space_between_plots: int = 5,
    row_size: int = 3,
    labelFontSize: int = 14,
    titleFontSize: int = 14,
    fig_size: Tuple = (100, 200),
) -> alt.Chart:
    """Plot grid of barcharts with Altair."""
    columns = []
    chunks = (df[col2grid].nunique() - 1) // row_size + 1
    for i in range(chunks):
        # print(i * row_size, (i + 1) * row_size)
        rows = []
        row_mul_start = i * row_size
        row_mul_stop = (i + 1) * row_size
        for y in df[col2grid].unique()[row_mul_start:row_mul_stop]:
            row_chart = (
                alt.Chart(df[df[col2grid] == y], title=str(y))
                .mark_bar()
                .encode(
                    x=alt.X(f"{xvar}:Q", title=""),
                    y=alt.Y(f"{yvar}:N", title="", sort="-x"),
                    color=alt.Color(
                        f"{col2grid}:N",
                        scale=alt.Scale(scheme="tableau20"),
                        legend=None,
                    ),
                    tooltip=[
                        alt.Tooltip(f"{yvar}:N"),
                        alt.Tooltip(f"{xvar}:Q", format=".6f"),
                    ],
                )
                .properties(width=fig_size[0], height=fig_size[1])
            )
            rows.append(row_chart)
        col_chart = alt.vconcat(*rows)
        columns.append(col_chart)
    combo = (
        alt.hconcat(*columns)
        .configure_concat(spacing=space_between_plots)
        .configure_axis(
            labelFontSize=labelFontSize, titleFontSize=titleFontSize
        )
    )
    return combo


def plot_altair_heatmap(
    data: DataFrame,
    legend: alt.Legend(),
    tooltip: List = [],
    agg: str = "mean",
    xvar: str = "created_at_weekday",
    yvar: str = "created_at_hour",
    color_by_col: str = "count",
    ptitle: str = "My plot title",
    sort_x: List = ["A", "B"],
    sort_y: List = list(range(0, 23 + 1)),
    marker_linewidth: int = 1,
    cmap: str = "yelloworangered",
    scale: str = "log",
    show_x_labels: bool = True,
    show_y_labels: bool = True,
    fig_size: Tuple = (240, 750),
) -> alt.Chart:
    """Plot heatmap with Altair."""
    chart = (
        alt.Chart(data)
        .mark_rect(stroke="white", strokeWidth=marker_linewidth)
        .encode(
            y=alt.Y(
                f"{yvar}:N",
                title=None,
                axis=alt.Axis(ticks=False, labels=show_y_labels),
                sort=sort_y,
            ),
            x=alt.X(
                f"{xvar}:O",
                title=None,
                axis=alt.Axis(
                    ticks=False,
                    labelAngle=0,
                    orient="top",
                    labels=show_x_labels,
                ),
                sort=sort_x,
            ),
            color=alt.Color(
                f"{agg}({color_by_col}):Q",
                scale=alt.Scale(type=scale, scheme=cmap),
                legend=legend,
            ),
            tooltip=tooltip,
        )
        .properties(height=fig_size[1], width=fig_size[0], title=ptitle)
    )
    return chart


def plot_plotly_heatmap(
    data_dict: Dict,
    annotation_text: Dict,
    margin_dict: Dict = dict(l=30, r=0, b=0, t=0, pad=0),
    fig_width: Union[int, None] = 900,
) -> go.Figure:
    """Plot Heatmap with PlotLy."""
    layout = go.Layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=go.layout.Margin(**margin_dict),
        font={"size": 16},
    )
    fig = ff.create_annotated_heatmap(
        z=data_dict["z"],
        x=data_dict["x"],
        y=data_dict["y"],
        colorscale="YlOrRd",
        annotation_text=annotation_text,
        font_colors=["#454545", "white"],
        hoverinfo="skip",
        # hovertemplate="<b>Number of Tweets:</b> %{z:,}<extra></extra>",
    )
    fig.layout.update(layout)
    fig.update_layout(
        # hoverlabel=dict(
        #     bgcolor="white",
        #     bordercolor="black",
        #     font_size=16,
        #     font_family="Rockwell",
        # ),
        autosize=False,
    )
    fig.update_xaxes(
        tickfont=dict(family="Arial", size=18, color="rgb(92,90,90)"),
        tickangle=0,
    )
    fig.update_yaxes(
        tickfont=dict(family="Arial", size=18, color="rgb(92,90,90)")
    )
    fig["data"][0]["showscale"] = False
    if fig_width:
        fig.update_layout(width=fig_width)
    return fig
