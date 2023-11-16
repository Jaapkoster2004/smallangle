# Small angle
# Jaap Koster

# import libraries
import click
import numpy as np
from numpy import pi
import pandas as pd

#define the group of commands
@click.group()
def smallangle():
    """group of smallangle, calculates the sinus or tangens of a given amount of values between 0 and 2pi
    """
    pass


@smallangle.command()
@click.option(
    "-n",
    "--number",
    default = 10,
    help = "The amount of values you want to calculate between 0 and 2 pi",
    show_default = True
)

# calculates the sinus of x for a given amount of values of x between 0 and 2pi
def sin(number):
    """Calculates the sinus of x for a given amount of values of x between 0 and 2pi

    Args:
        number (integer): The amount of values the sinus is calculated for. Splits in equal parts between 0 and 2 pi

    
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@smallangle.command()
@click.option(
    "-n",
    "--number",
    default = 10,
    help = "The amount of values you want to calculate between 0 and 2 pi",
    show_default = True
)

# calculates the tangens of x for a given amount of values of x between 0 and 2pi
def tan(number):
    """Calculates the tangens of x for a given amount of values of x between 0 and 2pi

    Args:
        number (integer): The amount of values the tangens is calculated for. Splits in equal parts between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

#makes it so small angle can be called from anywhere
if __name__ == "__main__":
    smallangle()