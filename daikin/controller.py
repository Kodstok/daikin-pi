#!/usr/bin/python3.6

from daikin import DaikinMessage, DaikinState, DaikinLIRC, AC_MODE, DaikinController,FAN_MODE

controller = DaikinController()
controller.update(
            power=True,
            temperature=19,
            ac_mode=AC_MODE.HEAT,
            fan_mode=FAN_MODE.AUTO,
            swing_vertical=False,
            swing_horizontal=True,
            powerful=False,
    )
