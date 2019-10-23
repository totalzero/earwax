import Tolk

Tolk.load()
name = Tolk.detect_screen_reader()
Tolk.output("tolk dziala, twoj screen reader to: %s" %(name))