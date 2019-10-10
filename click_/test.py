from click.testing import CliRunner
from click_.demo1 import hello

def test_hello_world():
  runner = CliRunner()
  result = runner.invoke(hello, ['Peter'])
  print(result)
  assert result.exit_code == 0
  assert result.output == 'Hello Peter!\n'