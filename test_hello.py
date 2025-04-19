import click
from hello import hello

def test_hello():
    # Test the hello function with a specific name and color
    from click.testing import CliRunner
    runner = CliRunner()
    result = runner.invoke(hello, ['--name', 'Michelangelo', '--color', 'red'])
    
    # Check if the output contains the expected strings
    assert "Nunchacos" in result.output
    assert "Hello Michelangelo" in result.output
    assert result.exit_code == 0