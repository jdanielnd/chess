#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# web-boardimage is an HTTP service that renders chess board images.
# Copyright (C) 2016-2017 Niklas Fiekas <niklas.fiekas@backscattering.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""An HTTP service that renders chess board images"""

import chess
import svg
import hashlib

index = 1

with open('fen_positions.csv', 'r') as f:
  for fen in f:
    parts = fen.replace("_", " ").split(" ", 1)
    board = chess.BaseBoard("/".join(parts[0].split("/")[0:8]))
    size = 360

    svgtext = svg.board(board, coordinates=True, size=size, style=open("default.css", "r").read())
    hash_object = hashlib.md5(fen.encode())
    svgfile = open("fen18/file_{0}.svg".format(index), "w")
    svgfile.write(svgtext)
    svgfile.close()
    index = index + 1

