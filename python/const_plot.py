#!/usr/bin/env python
#
# Copyright 2014 Tim O'Shea
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#
from plotter_base import *
class const_plot(plotter_base):
    def __init__(self, label="", *args):
        plotter_base.__init__(self, blkname="const_plot", label=label, *args)
        self.message_port_register_in(pmt.intern("cpdus"));
        self.set_msg_handler(pmt.intern("cpdus"), self.handler);

        # set up curve
        curve = Qwt.QwtPlotCurve("Plot 0");
        curve.attach(self);
        self.curves.append(curve);

        noline = True
        if(noline):
            curve.setStyle(Qwt.QwtPlotCurve.NoCurve);
            curve.setSymbol(Qwt.QwtSymbol(Qwt.QwtSymbol.XCross,
                                      Qt.QBrush(),
                                      #Qt.QPen(Qt.Qt.darkMagenta),
                                      Qt.QPen(Qt.Qt.green),
                                      Qt.QSize(1, 1)))

        self.curve_data = [([], [])];

    def handler(self, msg):
        # get input
        meta = pmt.car(msg);
        samples = pmt.cdr(msg);
        x = numpy.array(pmt.c32vector_elements(samples), dtype=numpy.complex64)
        
        # trigger update
        self.curve_data[0] = (numpy.real(x), numpy.imag(x));
        self.emit(QtCore.SIGNAL("updatePlot(int)"), 0)


