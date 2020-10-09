# leap_year
Leap Year: Tells you if a certain year is leap year or not.

Programmed in Python 3.8.5, uses CLI. 

## Details:
- The year must be greater than 1582, when the transition between the Julian Calendar and the Greagorian calendar started.
- A leap year must follow the next statements:
  - The year must be divisible by 4 (year%4 == 0).
  - The year must not be divisible by 100, unless the year is also divisible by 400 (year%100 != 0 or year%400 == 0).

## Run:
- Introducing 2020:
<p align="center"> <img src="https://github.com/irving-rs/leap_year/blob/main/Program_Execution_1.png"> </p>

- Introducing 2100:
<p align="center"> <img src="https://github.com/irving-rs/leap_year/blob/main/Program_Execution_2.png"> </p>

- Introducing a non-valid option:
<p align="center"> <img src="https://github.com/irving-rs/leap_year/blob/main/Program_Execution_3.png"> </p>
