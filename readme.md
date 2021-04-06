# Bonus 
Bonus, a pure python GUI library wrapped around tkinter in development. The goal for Bonus is for it to be capable of making a variety of projects (Applications, Games, etc.) that run smoothly and look good, without the developer having to recreate the wheel.

## Goal
Currently my main goal is to get a smooth running chromium canvas rendering inside of a tkinter frame. This is not going to be the only option to make GUIs. But will be an easy way to make a GUI powered by python. 

## Status
Currently it is extremely buggy and does not have any widgets. I'm mainly focused on the window engine since I feel that is something that Tkinter lacks and needs to be easy for teh developer. After the window and app engine are to a point I feel satisfied, I will begin to implement a chromium canvas and other widgets. 

## Background
I wanted the original name to be Tkinter++ or Tkinter-bonus and they were both taken. So I've decided to settle with BonusUI until I have a better name. 

## What it will include?
- Reliable Window engine that gives the developer infinite customizability
- 2D engine which can be used to load textures, create 2D games, or other unique designs. 
- Plethora of easy and accessible widgets to apply to the window
- Chromium canvas which will provide the developer to create GUIs with JavaScript and HTML + CSS
- Reliable for all operating systems and monitors/monitorsizes (problem i've notices with lots of application engines)
- Quick and reliable saving and backup systems that will save the position, size, and state of the window and buttons
- Excellent performace and speedy launches
- Easy-to-release capabilities allowing you to launch the application to a variety of platforms

## Knwon Issues:
- Unreliable saving systems (likely data loss)
- FPS limiter above 1000 gets glitchy with the counter
- Iherited from Window class does not always call the correct init class or work properly 