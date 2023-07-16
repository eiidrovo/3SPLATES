# 3S-Plates

This repo was made by [Esau Idrovo](mailto:eiidrovo@protonmail.com), student of Naval Engineering at ESPOL - Ecuador. This script is open to everyone, but if it is useful to you, give me an Star and reference this repo into your work.

## Sinusoudal Simple Supported Plates

This repository is used for the calculation of:

- Load distribution
- Deflection
- Bending moments
- Normal stresses

In plates using sinusoidal load approximation.

## How to use the script?

First! Check out the [dependencies](#dependencies) and install them before start (**recommendation**: keep it simple, download python from its official website, don't use PyCharm, Spyder or whatever, you won't need it).

Download the [plate.json]() and [3SPlates.1.0.py]() files.

Edit the [plate.json]() file with the dimmensions of the plate detailed below:

- E: Young Modulus  $\left[\frac{N}{m^2}\right]$
- Pois: Poisson Ratio
- Lenghtx and lenghty: Lenght in x and y of the plate $\left[m\right]$
- Thickness: thickness of the plate $\left[m\right]$
- Z: Half of the thickness $\left[m\right]$
- Resolution: Numer of subdivitions in the plate 
- Terms: Number of m and n terms odd, even or none.
- Type: Type of force ('point', 'distributed')
- F: Force $\left[N\right]$ (point-type) or load acting on the plate $\left[\frac{N}{m^2}\right]$ (distributed-type)
- XF and YF: If the force is point-type, are the x and y position of the force acting on the plate $\left[m\right]$ If the foce is distributed this value doesn't matter.
- Strainx and Strainy: The position in x and y of the point where you wanna analyze the strain $\left[m\right]$ 
- Parity: Parity of the m and n terms. It can take the values "odd", "even" and "none". Review the section "[Parity](#parity)"

Open the terminal in the folder where you've downloaded the files. and run the script.

<pre>
python 3SPlates.1.0.py
</pre>

Then write **PLOT** if you want to make the calculations for all the plate: load distribution, deflection, bending moments, etc. It will generate a folder name CSV for each magnitude of analysis that you can plot with other software like LabPlot or EasyPlot (For the version 2.0 of the script, the plotting will be automated).

But, if you wanna make an alaysis of strains in a singlepoint, write **STRAIN**. It will generate a file named **strains.log**. that contains the strains in x and y in the point you've specified.


## <a  id="parity"></a>Parity

For **Distributed-Load** the parity value must be **odd**.

For **Point-Load** the parity value can be odd, eve or none, it depends on how many force your case need, for example: for a single point load (delta dirac) the **none** works.


## <a  id="dependencies"></a>Dependencies

- Python 3.11.2
- Numpy






