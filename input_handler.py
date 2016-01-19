from pyglet.window import key


class InputHandler(key.KeyStateHandler):
    inputs = [0]*16

    keys = {
        key._0: 0x0,
        key._1: 0x1,
        key._2: 0x2,
        key._3: 0x3,
        key._4: 0x4,
        key._5: 0x5,
        key._6: 0x6,
        key._7: 0x7,
        key._8: 0x8,
        key._9: 0x9,
        key.A: 0xA,
        key.B: 0xB,
        key.C: 0xC,
        key.D: 0xD,
        key.E: 0xE,
        key.F: 0xF
    }

    def __init__(self, screen):
        screen.push_handlers(self)

    def on_key_press(self, symbol, modifiers):
        if (symbol in self.keys):
            self.inputs[self.keys[symbol]] = True

    def on_key_release(self, symbol, modifiers):
        if (symbol in self.keys):
            self.inputs[self.keys[symbol]] = False

    def is_pressed(self, key):
        return self.inputs[key]