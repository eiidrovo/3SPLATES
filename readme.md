# 3S-Plates

This repo was made by [Esau Idrovo](mailto:eiidrovo@protonmail.com), student of Naval Engineering at ESPOL - Ecuador. This script is open to everyone, but if it is useful to you, give me an Star and reference this repo into your work.

## Sinusoidal Simple Supported Plates

This repository can be used for the calculation of:

- Load distribution
- Deflection
- Bending moments
- Normal stresses

In plates using sinusoidal load approximation for simple supported rectangular plates with 2 kind of loads: **point** and **distributed** along the plate.

## How to use the script?

First! Check out the [dependencies](#dependencies) and install them before start (**recommendation**: keep it simple, download python from its official website, don't use PyCharm, Spyder or whatever, you won't need it).

Download the [plate.json](https://github.com/eiidrovo/3SPLATES/blob/main/plate.json) and [3SPlates.1.0.py](https://github.com/eiidrovo/3SPLATES/blob/main/3SPlates.1.0.py) files.

Edit the [plate.json](https://github.com/eiidrovo/3SPLATES/blob/main/plate.json) file with the dimmensions of the plate detailed below:

- E: Young Modulus  $\left[\frac{N}{m^2}\right]$
- Yield: The yield point or maximun allowable stress $\left[\frac{N}{m^2}\right]$
- Pois: Poisson Ratio
- Lenghtx and lenghty: Lenght in x and y of the plate $\left[m\right]$
- Thickness: thickness of the plate $\left[m\right]$
- Z: Half of the thickness $\left[m\right]$
- Resolution: Numer of subdivitions in the plate 
- Terms: Number of m and n terms odd, even or none.
- Type: Type of force ('point', 'distributed')
- F: Force $\left[N\right]$ (point-type) or load acting on the plate $\left[\frac{N}{m^2}\right]$ (distributed-type)
- XF and YF: If the force is point-type, are the x and y position of the force acting on the plate $\left[m\right]$ If the foce is distributed this value doesn't matter.

- Parity: Parity of the m and n terms. It can take the values "odd", "even" and "none". Review the section "[Parity](#parity)"

Open the terminal in the folder where you've downloaded the files. and run the script.

<pre>
python 3SPlates.1.0.py

or

py 3SPlates.1.0.py
</pre>

Be sure that the python file is in the same folder as the plate.json file.


If everything worked, you will see a file named **output.log** with the maximun values of normal stresses and deflection, and also a csv-like columns with the values of the coordinates and bending moment, load distribution, etc. You can use that data to plot using other programs or python. 

For now I will be providing only the output array with all the values necessary to plot, for the next version I will release the program that make plots also.


## <a  id="parity"></a>Parity

For **Distributed-Load** the parity value must be **odd**.

For **Point-Load** the parity value can be odd, eve or none, it depends on how many force your case need, for example: for a single point load (delta dirac) the **none** value works fine.


## <a  id="dependencies"></a>Dependencies

- Python 3.11.2
- Numpy






