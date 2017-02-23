import NeuroPy.NeuroPy as NP
import time

object1 = NP.NeuroPy("/dev/tty.MindWaveMobile-SerialPo", 9600, log=True)

object1.start()

time.sleep(5)

object1.stop()
