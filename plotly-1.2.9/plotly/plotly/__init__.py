"""
plotly
======

This module defines functionality that requires interaction between your
local machine and Plotly. Almost all functionality used here will require a
verifiable account (username/api-key pair) and a network connection.

"""
from . plotly import (
    sign_in, update_plot_options, get_plot_options, get_credentials, iplot,
    plot, iplot_mpl, plot_mpl, get_figure, Stream, image
)
