


# Adding Calculator Compiler

## Motivation
The focus of this project was to enquire into the technologies that make up a compiler. I wanted to figure out how the components of a compiler work on a small scale and fully implement a working compiler for a language that can work on an actual computer, in this case the stack-based [Desk Calculator](https://en.wikipedia.org/wiki/Dc_%28computer_program%29). The source language is AC, or adding calculator.

## Introduction
Compilers (and more generally, translators) form the foundation of modern computing. They allow the programmer to abstract the inner workings of the computer away and focus on the manipulation of data more efficiently. Furthermore, compilers allow for the use of languages with simpler and more expressive syntax, which can widen the scope for who can develop software for computers. This opens information technology up to a horizontal expansion and use from other fields of expertise.
In order to explore how compilers work, I researched the principle components of a compiler and the data flow inside of a compiler, an example of this is below:
![Data flow diagram of a compiler](https://user-images.githubusercontent.com/25799076/103317181-aa36e580-4a22-11eb-89d9-1ad2ba6d7ef0.png)
The finished compiler follows this exact data flow diagram, leaving out the Optimiser section as to reduce the workload.
Adding Calculator is a simple language, consisting of variable delcaration and assignment, add, subtract, and print operations. This allows a complex enough grammar as to be a challenging problem, without being too much for a first project in compilers given the time frame of 2 evenings to finish it.

An example of a program written in AC is as follows:

    f b 
    i a
    
    a = 5
    
    b = 3.2 + a
    
    p b
This simple program declares the float b and the integer a, then assigns a to be 5 and b to be 3.2 + a. Then outputs b into the terminal. This program also demonstrates the type-checking ability of the compiler, as a type error would have been thrown given b had been delcared as an integer instead of a float. This code then compiles into the following dc code:

    5 k
    0.0
    sb
    0 k
    0
    sa
    5
    sa
    0 k
    3.2
    la
    5 k
    +
    sb
    0 k
    lb
    p
    si
Which helps demonstrate the usefulness of code-translators, as the first block of code is undoubtably easier to read and write than the second. When put throught the dc program, the following is printed:

    8.2
Which one may check to be the correct answer.

## Technology
The primary language used in this project was Python 3.8, selected for its prowess in rapid prototyping, ease-of-use, and readibility. It allowed me to finish the program in the timeframe allocated for it. If speed was a consideration, I likely would have chosen Java as I am proficient in that language as well.

## Getting Started
If you want to get the project running immediately or wish to tinker around with the code, this is the place to start!

### Prerequisites
This project can be run on Windows 10, 7 and Linux. The prerequisites you need to install are Python 3.8.
To get started, go into /python and run the following command:

    $ python3 main.py
The program will then convert the code written in test.ac into dc and save the result as test.txt. You can then run the program by invoking the dc program installed on most unix machines:

    $ dc test.txt

## Authors

* **Jordan Hall** - *Sole developer* - [PlatinumNinja72]
