import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from visualization import app

def test(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Soul Foods Pink Morsel Sales Dashboard" in header.text


def test_graph_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    radio = dash_duo.find_element("#region-selector")
    assert radio is not None
