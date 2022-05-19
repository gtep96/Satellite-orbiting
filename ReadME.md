I've used libs: cgitb, cmath, turtle, txaio and vpython for visualization. There is no special maths for now, so there was no need for SimyPy. 

In this visualization all physics parameters (such as Moon mass and radius) is like in real world, but visual size of sphere of Moon in visualization is 95% of real for better view. Starting altitude is 20 km, velocity is 1700 m/s. I can't check all output data (such as apoapsis for example) for now, but I hope all calculations are correct.

On the lower-left corner you can see current altitude and velocity of satellite. There is CalcVel also, which is precalculated first cosmic velocity for given starting data. It will change if SatAltitude and/or Moon parameters will be changed. 

You can change simulation speed by changing "dt" or vp.rate parameters.

Also, yellow arrow shows current direction of satellite velocity.
