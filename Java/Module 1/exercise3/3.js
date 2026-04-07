'use strict';
let no1,no2,no3
no1 = parseInt(prompt("Enter first number"));
no2 = parseInt(prompt("Enter second number"));
no3 = parseInt(prompt("Enter third number"));

let sum = no1+ no2+ no3;
let product = no1*no2*no3;
let average = sum/3;

document.querySelector("#target").innerHTML = ("Sum of the three numbers:" + sum + "<br>" +
"Product of the three numbers:" + product + "<br>" + "Average of the three numbers:" + average);
