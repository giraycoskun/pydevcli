import typer
from rich.console import Console
from typing_extensions import Annotated

app = typer.Typer()
console = Console()

@app.command()
def test(address: Annotated[str, typer.Argument(help="Connection Address")],
        port: Annotated[int, typer.Argument(help="Connection Port", default=3306)],
        username: Annotated[str, typer.Argument(help="Database Username", default="root")],
        password: Annotated[str, typer.Argument(help="Database Password")]):
    """Test Connection
    """
    pass
