from tomd import Tomd


html="""<table border="1">
	<caption>List of Functions in Python Math Module</caption>
	<tbody>
		<tr>
			<th style="text-align:left">Function</th>
			<th style="text-align:left">Description</th>
		</tr>
		<tr>
			<td style="text-align:left">ceil(x)</td>
			<td style="text-align:left">Returns the smallest integer greater than or equal to x.</td>
		</tr>
		<tr>
			<td style="text-align:left">copysign(x, y)</td>
			<td style="text-align:left">Returns x with the sign of y</td>
		</tr>
		<tr>
			<td style="text-align:left">fabs(x)</td>
			<td style="text-align:left">Returns the absolute value of x</td>
		</tr>
		<tr>
			<td style="text-align:left">factorial(x)</td>
			<td style="text-align:left">Returns the factorial of x</td>
		</tr>
		<tr>
			<td style="text-align:left">floor(x)</td>
			<td style="text-align:left">Returns the largest integer less than or equal to x</td>
		</tr>
		<tr>
			<td style="text-align:left">fmod(x, y)</td>
			<td style="text-align:left">Returns the remainder when x is divided by y</td>
		</tr>
		<tr>
			<td style="text-align:left">isinf(x)</td>
			<td style="text-align:left">Returns True if x is a positive or negative infinity</td>
		</tr>
		<tr>
			<td style="text-align:left">modf(x)</td>
			<td style="text-align:left">Returns the fractional and integer parts of x</td>
		</tr>
		<tr>
			<td style="text-align:left">trunc(x)</td>
			<td style="text-align:left">Returns the truncated integer value of x</td>
		</tr>
		<tr>
			<td style="text-align:left">exp(x)</td>
			<td style="text-align:left">Returns e**x</td>
		</tr>
		<tr>
			<td style="text-align:left">log(x[, base])</td>
			<td style="text-align:left">Returns the logarithm of x to the base (defaults to e)</td>
		</tr>
		<tr>
			<td style="text-align:left">log2(x)</td>
			<td style="text-align:left">Returns the base-2 logarithm of x</td>
		</tr>
		<tr>
			<td style="text-align:left">log10(x)</td>
			<td style="text-align:left">Returns the base-10 logarithm of x</td>
		</tr>
		<tr>
			<td style="text-align:left">pow(x, y)</td>
			<td style="text-align:left">Returns x raised to the power y</td>
		</tr>
		<tr>
			<td style="text-align:left">sqrt(x)</td>
			<td style="text-align:left">Returns the square root of x</td>
		</tr>
		<tr>
			<td style="text-align:left">acos(x)</td>
			<td style="text-align:left">Returns the arc cosine of x</td>
		</tr>
		<tr>
			<td style="text-align:left">asin(x)</td>
			<td style="text-align:left">Returns the arc sine of x</td>
		</tr>
		<tr>
			<td style="text-align:left">atan(x)</td>
			<td style="text-align:left">Returns the arc tangent of x</td>
		</tr>
		<tr>
			<td style="text-align:left">atan2(y, x)</td>
			<td style="text-align:left">Returns atan(y / x)</td>
		</tr>
		<tr>
			<td style="text-align:left">cos(x)</td>
			<td style="text-align:left">Returns the cosine of x</td>
		</tr>
		<tr>
			<td style="text-align:left">sin(x)</td>
			<td style="text-align:left">Returns the sine of x</td>
		</tr>
		<tr>
			<td style="text-align:left">tan(x)</td>
			<td style="text-align:left">Returns the tangent of x</td>
		</tr>
		<tr>
			<td style="text-align:left">degrees(x)</td>
			<td style="text-align:left">Converts angle x from radians to degrees</td>
		</tr>
		<tr>
			<td style="text-align:left">radians(x)</td>
			<td style="text-align:left">Converts angle x from degrees to radians</td>
		</tr>
		<tr>
			<td style="text-align:left">acosh(x)</td>
			<td style="text-align:left">Returns the inverse hyperbolic cosine of x</td>
		</tr>
		<tr>
			<td style="text-align:left">asinh(x)</td>
			<td style="text-align:left">Returns the inverse hyperbolic sine of x</td>
		</tr>
		<tr>
			<td style="text-align:left">atanh(x)</td>
			<td style="text-align:left">Returns the inverse hyperbolic tangent of x</td>
		</tr>
		<tr>
			<td style="text-align:left">cosh(x)</td>
			<td style="text-align:left">Returns the hyperbolic cosine of x</td>
		</tr>
		<tr>
			<td style="text-align:left">sinh(x)</td>
			<td style="text-align:left">Returns the hyperbolic cosine of x</td>
		</tr>
		<tr>
			<td style="text-align:left">tanh(x)</td>
			<td style="text-align:left">Returns the hyperbolic tangent of x</td>
		</tr>
		<tr>
			<td style="text-align:left">erf(x)</td>
			<td style="text-align:left">Returns the error function at x</td>
		</tr>
		<tr>
			<td style="text-align:left">erfc(x)</td>
			<td style="text-align:left">Returns the complementary error function at x</td>
		</tr>
		<tr>
			<td style="text-align:left">gamma(x)</td>
			<td style="text-align:left">Returns the Gamma function at x</td>
		</tr>
		<tr>
			<td style="text-align:left">lgamma(x)</td>
			<td style="text-align:left">Returns the natural logarithm of the absolute value of the Gamma function at x</td>
		</tr>
		<tr>
			<td style="text-align:left">pi</td>
			<td style="text-align:left">Mathematical constant, the ratio of circumference of a circle to it&#39;s diameter (3.14159...)</td>
		</tr>
		<tr>
			<td style="text-align:left">e</td>
			<td style="text-align:left">mathematical constant e (2.71828...)</td>
		</tr>
	</tbody>
</table>
"""


print(Tomd(html).markdown)
