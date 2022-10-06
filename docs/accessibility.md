# Accessiblity

Visualizations present a few problems for vision impaired folks:

* Titles are rarely descriptive enough for people using screen readers
* No summary, so useless for people using screan readers
* SVG text doesn't help people using screen readers, including title, axis labels, trace labels, and legends
* Data hidden in tooltips is often not read by screen readers
* Color blind can't distinguish between cohorts when colors are used to differentiate
* A lack of whitespace between cohorts can make it impossible for color blind people to distinguish

Here are some solutions:

* Provide a descriptive title using HTML (not embedded SVG text)
* Provide a brief text summary near the visualization (can be part of the copy text if it's next to the visualization)
* Provide the label and value of each data point as text (not in a tooltip)
* Don't use legends - instead label traces with annotations (lines connecting the trace to a text label)
* Include whitespace between cohorts / data points

Example from [this great reference](https://www.betterment.com/design/accessible-data-visualization):

![Accessible visualization](./accessible%20visualization.png)
