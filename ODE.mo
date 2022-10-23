model ODE

  Real Fr(unit="N");
  Real Cf;
  
  Real a(unit="m/s2");
  Real Re;
  Real F(unit="N");
  parameter Real Ft (unit="N") = 400;

  parameter Real S (unit="m2") = 100;
  parameter Real density (unit="kg/m3") = 1025;
  parameter Real k (unit="m2/s") = 1.188*10^(-6);
  parameter Real L (unit="m") = 21.54;
  parameter Real m (unit="kg") = 32000;
  Modelica.Blocks.Interfaces.RealOutput v (unit="m/s") annotation(
    Placement(visible = true, transformation(origin = {106, 34}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {106, 34}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Interfaces.RealOutput x (unit="m") annotation(
  
  
    Placement(visible = true, transformation(origin = {104, -28}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {104, -28}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  a = der(v)/der(time);
  v = der(x)/der(time);

  Re = (v*L)/k;
  if(v == 0) then
    Cf = 0;
  else
    Cf = 0.075/(log10(Re)-2)^2;
  end if;
  Fr = (1/2)*density*(v^2)*S*Cf;
  der(v)/der(time) = (Ft-Fr)/m;
  F = Ft-Fr;
  

annotation(
    uses(Modelica(version = "4.0.0")),
    Icon(graphics = {Rectangle(origin = {-1, 17}, extent = {{-99, 75}, {99, -75}}), Text(origin = {-5, 25}, extent = {{-57, 35}, {57, -35}}, textString = "ODE")}));
end ODE;
