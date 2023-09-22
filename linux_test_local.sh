#!/bin/bash

# Install Ruby Gems to ~/gems
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"

bundle exec jekyll serve --lsi

xdg-open http://127.0.0.1:4000

$SHELL
