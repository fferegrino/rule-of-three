from click.testing import CliRunner
from rule_of_three import __main__
from mock import patch

def test_main():
    runner = CliRunner()
    result = runner.invoke(__main__.main, ['1', '2', '3'])
    assert result.exit_code == 0
    assert result.output == '6.0\n'
