#!/bin/bash

# filename: installation_packages.sh
#
# by: Abhay Gupta
# date: 02/23/19
#
# description: developer packages installation script for macOS

# Need to run: chmod -x <filename> 
# This changes permissions of file to be an executable
#
# To run file: ./installation_packages.sh

echo Installing Homebrew and Xcode cmd line tools

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

echo installing packages via Homebrew
brew install git

echo installing applications via Hombrew Cask
brew cask install google-chrome

