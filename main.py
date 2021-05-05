def flashGrn():
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.GREEN)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.OFF)
    basic.pause(150)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.OFF)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.GREEN)
    basic.pause(150)
def clrColors():
    global green, yellow, red, blue, white
    green = 0
    yellow = 0
    red = 0
    blue = 0
    white = 0
def flashYel():
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.YELLOW)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.OFF)
    basic.pause(200)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.OFF)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.YELLOW)
    basic.pause(200)
def getSerialdata():
    global serialBufferIn, rcChan1A, rcChan1B, joyH
    serialBufferIn = []
    for index in range(32):
        serialBufferIn.append(serial.read_buffer(NumberFormat.UINT8_LE))
    rcChan1A = serialBufferIn[1]
    rcChan1B = serialBufferIn[2]
    joyH = rcChan1A + 256 * rcChan1B
def flashBlue():
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.BLUE)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.OFF)
    basic.pause(150)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.OFF)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.BLUE)
    basic.pause(150)
def flashRed3():
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.RED)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.OFF)
    basic.pause(150)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.OFF)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.RED)
    basic.pause(150)
motorRspeed = 0
motorLspeed = 0
joyH = 0
rcChan1B: Buffer = None
rcChan1A: Buffer = None
serialBufferIn: List[Buffer] = []
white = 0
blue = 0
red = 0
yellow = 0
green = 0
angle = 90
DFRobotMaqueenPlus.servo_run(Servos.S1, angle)
DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.WHITH)
serial.redirect(SerialPin.P0, SerialPin.P1, BaudRate.BAUD_RATE115200)
serial.set_rx_buffer_size(32)
music.play_tone(262, music.beat(BeatFraction.WHOLE))

def on_forever():
    if green == 1:
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.WHITH)
    elif yellow == 1:
        flashYel()
    elif red == 1:
        flashRed3()
    elif blue == 1:
        flashBlue()
    elif white == 1:
        flashGrn()
    else:
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.WHITH)
basic.forever(on_forever)

def on_forever2():
    if blue == 1:
        music.play_melody("C5 G C5 G C5 G C5 G ", 240)
basic.forever(on_forever2)

def on_forever3():
    global motorLspeed, motorRspeed
    joyV = 0
    if joyV > 550:
        motorLspeed = Math.map(joyV, 550, 1023, 10, 255)
        motorRspeed = motorLspeed
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, motorLspeed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, motorRspeed)
    elif joyV < 450:
        motorLspeed = Math.map(joyV, 450, 0, 10, 255)
        motorRspeed = motorLspeed
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, motorLspeed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, motorRspeed)
    elif joyH < 450:
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, motorLspeed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, motorLspeed)
    elif joyH > 550:
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, motorLspeed)
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, motorLspeed)
    else:
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, 0)
basic.forever(on_forever3)
