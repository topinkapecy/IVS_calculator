import importlib
import sys
import types
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


class FakeStringVar:
    def __init__(self, *args, **kwargs):
        self.value = ""

    def get(self):
        return self.value

    def set(self, value):
        self.value = str(value)


class FakeWidget:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def pack(self, *args, **kwargs):
        return None

    def place(self, *args, **kwargs):
        return None

    def bind_all(self, *args, **kwargs):
        return None


class FakeTk(FakeWidget):
    def title(self, *args, **kwargs):
        return None

    def iconphoto(self, *args, **kwargs):
        return None

    def mainloop(self, *args, **kwargs):
        return None


@pytest.fixture()
def app(monkeypatch): 
    fake_tkinter = types.ModuleType("tkinter")
    fake_tkinter.Tk = FakeTk
    fake_tkinter.Canvas = FakeWidget
    fake_tkinter.PhotoImage = FakeWidget
    fake_tkinter.StringVar = FakeStringVar
    fake_tkinter.Entry = FakeWidget
    fake_tkinter.Button = FakeWidget

    monkeypatch.setitem(sys.modules, "tkinter", fake_tkinter)
    sys.modules.pop("main", None)

    module = importlib.import_module("main")
    module.clear()
    return module


def test_clearing_display(app):
    app.press(1)
    app.press("+")
    app.press(3)

    assert app.display.get() == "1+3"

    app.clear()

    assert app.display.get() == ""


def test_factorial_button_writes_symbol(app):
    app.press(5)
    app.factorial()

    assert app.display.get() == "5!"

@pytest.mark.parametrize(
    "symbol, expected",
    [
        ("+", "5+"),
        ("-", "5-"),
        ("×", "5×"),
        ("÷", "5÷"),
        (".", "5."),
        ("^", "5^"),
    ],
)
def test_operation_button_writes_symbol(app, symbol, expected):
    app.press(5)
    app.press(symbol)

    assert app.display.get() == expected


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("2+3", "5"),
        ("10-4", "6"),
        ("6×7", "42"),
        ("8÷2", "4.0"),
        ("2+3×4", "14"),
        ("2^4", "16"),
        ("5!", "120"),
        ("4!+2^4", "40"),
        ("12+3÷5", "12.6"),
    ],
)
def test_valid_expressions(app, expression, expected):
    app.display.set(expression)

    app.calculate()

    assert app.display.get() == expected


@pytest.mark.parametrize(
    "expression",
    [
        "5÷0",
        "5+*2",
        "5.5!",
        "",
    ],
)
def test_invalid_expressions_error(app, expression):
    app.display.set(expression)

    app.calculate()

    assert app.display.get() == "Error"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("49", "7.0"),
        ("2", "1.414214"),
        ("2.25", "1.5"),
    ],
)
def test_square_root_valid_values(app, value, expected):
    app.display.set(value)

    app.square_root()

    assert app.display.get() == expected


@pytest.mark.parametrize("value", ["-9", ""])
def test_square_root_invalid_values_error(app, value):
    app.display.set(value)

    app.square_root()

    assert app.display.get() == "Error"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("50", "0.5"),
        ("100", "1.0"),
        ("-25", "-0.25"),
        ("2.5", "0.025"),
    ],
)
def test_percentage_values(app, value, expected):
    app.display.set(value)

    app.percentage()

    assert app.display.get() == expected

def test_long_result_is_shortened(app):
    app.display.set("99999999999×99999999999999")

    app.calculate()

    digits_only = app.display.get().replace(".", "").replace("-", "")
    assert "e+" in app.display.get() or len(digits_only) <= 16
