import typer
from superpack import main_7_, main2_8_, app_7_
from main_7_ import func as main_7_func
from main2_8_ import divide as main2_8_divide
from app_7_ import split as app_7_split

app = typer.Typer()

@app.command()
def run_module1(num: int):
    main_7_func(num)

@app.command()
def run_module2(a: int, b: int):
    main2_8_divide(a, b)

@app.command()
def run_module3(lst: str, n: int):
    lst = lst.split(",")
    result = app_7_split(lst, n)
    typer.echo(result)

if __name__ == "__main__":
    app()



