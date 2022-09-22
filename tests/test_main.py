from click.testing import CliRunner
from rule_of_three import __main__
from unittest.mock import patch

def test_main():
    with patch("rule_of_three.__main__.rule_of_three") as rule_of_three_mocked:

        rule_of_three_mocked.return_value = 0

        runner = CliRunner()
        result = runner.invoke(__main__.main, ['1', '2', '3'])

        rule_of_three_mocked.assert_called_once_with(1, 2, 3)
        assert result.exit_code == 0
        assert result.output == '0\n' 
