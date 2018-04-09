from tomd import Tomd


html="""<table>
	<caption>List of Functions in Python Math Module</caption>
	<tbody>
		<tr>
			<th>Function</th>
			<th>Description</th>
		</tr>
		<tr>
			<td>ceil(x)</td>
			<td>Returns the smallest integer greater than or equal to x.</td>
		</tr>
		<tr>
			<td>copysign(x, y)</td>
			<td>Returns x with the sign of y</td>
		</tr>
		<tr>
			<td>fabs(x)</td>
			<td>Returns the absolute value of x</td>
		</tr>
		<tr>
			<td>factorial(x)</td>
			<td>Returns the factorial of x</td>
		</tr>
		<tr>
			<td>floor(x)</td>
			<td>Returns the largest integer less than or equal to x</td>
		</tr>
		<tr>
			<td>fmod(x, y)</td>
			<td>Returns the remainder when x is divided by y</td>
		</tr>
		<tr>
			<td>isinf(x)</td>
			<td>Returns True if x is a positive or negative infinity</td>
		</tr>
		<tr>
			<td>modf(x)</td>
			<td>Returns the fractional and integer parts of x</td>
		</tr>
		<tr>
			<td>trunc(x)</td>
			<td>Returns the truncated integer value of x</td>
		</tr>
		<tr>
			<td>exp(x)</td>
			<td>Returns e**x</td>
		</tr>
		<tr>
			<td>log(x[, base])</td>
			<td>Returns the logarithm of x to the base (defaults to e)</td>
		</tr>
		<tr>
			<td>log2(x)</td>
			<td>Returns the base-2 logarithm of x</td>
		</tr>
		<tr>
			<td>log10(x)</td>
			<td>Returns the base-10 logarithm of x</td>
		</tr>
		<tr>
			<td>pow(x, y)</td>
			<td>Returns x raised to the power y</td>
		</tr>
		<tr>
			<td>sqrt(x)</td>
			<td>Returns the square root of x</td>
		</tr>
		<tr>
			<td>acos(x)</td>
			<td>Returns the arc cosine of x</td>
		</tr>
		<tr>
			<td>asin(x)</td>
			<td>Returns the arc sine of x</td>
		</tr>
		<tr>
			<td>atan(x)</td>
			<td>Returns the arc tangent of x</td>
		</tr>
		<tr>
			<td>atan2(y, x)</td>
			<td>Returns atan(y / x)</td>
		</tr>
		<tr>
			<td>cos(x)</td>
			<td>Returns the cosine of x</td>
		</tr>
		<tr>
			<td>sin(x)</td>
			<td>Returns the sine of x</td>
		</tr>
		<tr>
			<td>tan(x)</td>
			<td>Returns the tangent of x</td>
		</tr>
		<tr>
			<td>degrees(x)</td>
			<td>Converts angle x from radians to degrees</td>
		</tr>
		<tr>
			<td>radians(x)</td>
			<td>Converts angle x from degrees to radians</td>
		</tr>
		<tr>
			<td>acosh(x)</td>
			<td>Returns the inverse hyperbolic cosine of x</td>
		</tr>
		<tr>
			<td>asinh(x)</td>
			<td>Returns the inverse hyperbolic sine of x</td>
		</tr>
		<tr>
			<td>atanh(x)</td>
			<td>Returns the inverse hyperbolic tangent of x</td>
		</tr>
		<tr>
			<td>cosh(x)</td>
			<td>Returns the hyperbolic cosine of x</td>
		</tr>
		<tr>
			<td>sinh(x)</td>
			<td>Returns the hyperbolic cosine of x</td>
		</tr>
		<tr>
			<td>tanh(x)</td>
			<td>Returns the hyperbolic tangent of x</td>
		</tr>
		<tr>
			<td>erf(x)</td>
			<td>Returns the error function at x</td>
		</tr>
		<tr>
			<td>erfc(x)</td>
			<td>Returns the complementary error function at x</td>
		</tr>
		<tr>
			<td>gamma(x)</td>
			<td>Returns the Gamma function at x</td>
		</tr>
		<tr>
			<td>lgamma(x)</td>
			<td>Returns the natural logarithm of the absolute value of the Gamma function at x</td>
		</tr>
		<tr>
			<td>pi</td>
			<td>Mathematical constant, the ratio of circumference of a circle to it&#39;s diameter (3.14159...)</td>
		</tr>
		<tr>
			<td>e</td>
			<td>mathematical constant e (2.71828...)</td>
		</tr>
	</tbody>
</table>
"""


print(Tomd(html).markdown)
