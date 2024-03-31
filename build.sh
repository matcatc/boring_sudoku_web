#!/bin/sh
#
# Main entry script to build the program.
# Since it's simple, build is done entirely in shell script.
#
# @author Matthew Todd
# @date 2024-03-31
#
# Copyright 2024 Matthew Todd
# 
# This file is part of Boring Sudoku Web.
# 
# Boring Sudoku Web is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
# 
# Boring Sudoku Web is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
# 
# You should have received a copy of the GNU General Public License along with
# Boring Sudoku Web. If not, see <https://www.gnu.org/licenses/>.

set -e

echo "Building README..."
asciidoctor README.asciidoc

