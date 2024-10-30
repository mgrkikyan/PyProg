import typer

from superpack import main2_8_
from superpack import main_7_
from superpack import app_7_

app = typer.Typer()


@app.command()
def foo(i: int):
    print(f'i: {i}\n', main_7_.func(i))


@app.command()
def foo2(a: int, b: int):
    print(f'a: {a}, b: {b}\n', main2_8_.divide(a, b))

@app.command()
def foo3(lst: list, n: int):
    print(f'lst: {lst}, n: {n}\n', app_7_.split(lst, n))

if __name__ == "__main__":
    app()
