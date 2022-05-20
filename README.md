# Floki

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
![logo](https://github.com/luckythandel/Floki/blob/main/assets/logo/logo.png)

Floki is a mainly Python based tool to create some sequences of words. It is helpful in Binary Exploitation and in PWN CTF challanges. You can use this tool in various ways. You can create sequences like, `AAAA,BBBB,CCCC,DDDD`. Or You can create random words like, `ABCD, ACBD, ADCB, ABDC`.

## Features
* Play with your own words
* Generate wordlists
* Random sequence
* Cylic sequence
* Standered Output
* Save output in a file 

## Usage
>❯ python3 floki.py ABCDEFGHIJKLM 4 -m 0 -
```
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMM
```
>❯ python3 main.py ABCD 3 -m 1
```
ABC
ABD
ACD
Base Char A Completed!!
BAC
BAD
BCD
Base Char B Completed!!
CAB
CAD
CBD
Base Char C Completed!!
DAB
DAC
DBC
Base Char D Completed!!
```

