function flashGrn () {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.GREEN)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.OFF)
    basic.pause(150)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.OFF)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.GREEN)
    basic.pause(150)
}
function clrColors () {
    green = 0
    yellow = 0
    red = 0
    blue = 0
    white = 0
}
function flashYel () {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.YELLOW)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.OFF)
    basic.pause(200)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.OFF)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.YELLOW)
    basic.pause(200)
}
function flashBlue () {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.BLUE)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.OFF)
    basic.pause(150)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.OFF)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.BLUE)
    basic.pause(150)
}
function flashRed3 () {
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.RED)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.OFF)
    basic.pause(150)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.OFF)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.RED)
    basic.pause(150)
}
let motorRspeed = 0
let motorLspeed = 0
let joyV = 0
let joyH = 0
let white = 0
let blue = 0
let red = 0
let yellow = 0
let green = 0
let angle = 90
DFRobotMaqueenPlus.servoRun(Servos.S1, angle)
DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.WHITH)
music.playTone(262, music.beat(BeatFraction.Whole))
basic.forever(function () {
    joyH = Math.map(pins.pulseIn(DigitalPin.P1, PulseValue.High), 1000, 2000, 0, 1023)
    joyV = Math.map(pins.pulseIn(DigitalPin.P2, PulseValue.High), 1000, 2000, 0, 1023)
})
basic.forever(function () {
    if (joyV > 550) {
        motorLspeed = Math.map(joyV, 550, 1023, 10, 255)
        motorRspeed = motorLspeed
        DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, motorLspeed)
        DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, motorRspeed)
    } else if (joyV < 450) {
        motorLspeed = Math.map(joyV, 450, 0, 10, 255)
        motorRspeed = motorLspeed
        DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, motorLspeed)
        DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, motorRspeed)
    } else if (joyH < 450) {
        DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, motorLspeed)
        DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, motorLspeed)
    } else if (joyH > 550) {
        DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, motorLspeed)
        DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, motorLspeed)
    } else {
        DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, 0)
    }
})
basic.forever(function () {
    if (green == 1) {
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.WHITH)
    } else if (yellow == 1) {
        flashYel()
    } else if (red == 1) {
        flashRed3()
    } else if (blue == 1) {
        flashBlue()
    } else if (white == 1) {
        flashGrn()
    } else {
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.WHITH)
    }
})
basic.forever(function () {
    if (blue == 1) {
        music.playMelody("C5 G C5 G C5 G C5 G ", 240)
    }
})
