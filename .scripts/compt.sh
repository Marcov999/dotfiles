#!/bin/bash
killall compton
compton --backend glx --vsync opengl-swc &
