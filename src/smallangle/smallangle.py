# Small angle
# Jaap Koster

# import libraries
import click
import numpy as np
from numpy import pi
import pandas as pd

#define the group of commands
@click.group()
def small_angle():
    pass


@small_angle.command()
@click.option(
    "-n",
    "--number",
    default = 10,
    help = "The amount of values you want to calculate between 0 and 2 pi",
    show_default = True
)
# calculates the sinus of x for N values of x between 0 and 2pi
def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@small_angle.command()
@click.option(
    "-n",
    "--number",
    default = 10,
    help = "The amount of values you want to calculate between 0 and 2 pi",
    show_default = True
)
# calculates the tangens of x for N values of x between 0 and 2pi
def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

#makes it so small angle can be called from anywhere
if __name__ == "__main__":
    small_angle()