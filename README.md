# NAKK
Nathan's Awesome Kalculus Kalculator :-)

## About 😎
This project is a small calculator I opted to create the summer prior to entering Calc BC at my school. I wanted to make sure I at least understood the general idea of the topic and not go in blind, especially since I'm taking Physics C: Mechanics this year and am supposed to know some prior to the course anyway. I did not write this alone; my good friend Mariano taught me through this and helped generate some ideas with me. He definitely proved to be very helpful when I got stuck.

## Working Features 👍
So far, the (mostly) working features are:

* `Resize graph`
    * This allows the user to adjust the x and y dimensions of the graph in both dimensions to control where the window shows the output
* `Derive at a Point`
    * This creates a popup window which allows the user to input an x-coordinate and is given two options from there: either `Plot derivative tangent line` or `Print derivative of point`. The tangent line plots onto the graph on the main window. However, the printing of the derivative at the entered point currently just prints onto the popup - need to adjust that eventually; additionally, this window is not reopenable after closing; easy fix, will do soon
* `Plot derivative of a function`
    * Relatively self-explanatory; currently it just plots the derivative of hardcoded function
* `Calculate integral between two points`
    * This one is still in the works however does properly return the correct value. Currently, it only takes inputs from the terminal - working to implement it onto the window eventually. If possible, I would like to shade the section of the graph or at least draw lines where the integral is being calculated

For 2-4 I am hoping to implement some sort of way to choose from a list of inputted (is that a word?) functions and perform actions on that function specifically rather than only the hardcoded one. It's a WIP 


## Broken/Unfinished Features 🔧
* Multi-functon entry
    * WIP on creating a section where you can enter up to 5 functions and choose which to be displayed. Will happen eventually but as of right now need to tweak some things in working ones first