import argparse,numpy as np
class Modulator:
    def __init__(self,rate,frequency,mix): self.rate=rate;self.frequency=frequency;self.mix=mix;self.phase=0.
    def process(self,x):
        phase=self.phase+2*np.pi*self.frequency*np.arange(len(x))/self.rate;self.phase=(self.phase+2*np.pi*self.frequency*len(x)/self.rate)%(2*np.pi)
        return x*((1-self.mix)+self.mix*np.sin(phase)[:,None])
def main():
    p=argparse.ArgumentParser();p.add_argument('--frequency',type=float,default=80);p.add_argument('--mix',type=float,default=.8);p.add_argument('--rate',type=int,default=48000);a=p.parse_args()
    if not 0<=a.mix<=1 or not 0<a.frequency<a.rate/2:p.error('Invalid parameters')
    import sounddevice as sd
    m=Modulator(a.rate,a.frequency,a.mix)
    def callback(indata,outdata,frames,time,status): outdata[:]=m.process(indata)
    with sd.Stream(samplerate=a.rate,channels=1,blocksize=256,callback=callback): input('Press Enter to stop (use headphones).')
if __name__=='__main__': main()
