
import subprocess

from ..read_all_lines import read_all_lines

# python3 -m homework data/input data/output
from ..wordcount import parse_args


def test_parse_args():

    result = subprocess.run(
        ["python", "-m", "homework", "data/input/", "data/output/"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "input: data/input/" in result.stdout
    assert "output: data/output/" in result.stdout


def test_read_all_lines():
    input_folder = "data/input/"
    lines = read_all_lines(input_folder)
    assert len(lines) > 0
    assert any(
        "Analytics refers to the systematic computational analysis of data" in line
        for line in lines
    )