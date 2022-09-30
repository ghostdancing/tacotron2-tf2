import matplotlib.pyplot as plt

def ARPA(text):
    out = ''
    for word_ in text.split(" "):
        word=word_; end_chars = ''
        while any(elem in word for elem in r"!?,.;") and len(word) > 1:
            if word[-1] == '!': end_chars = '!' + end_chars; word = word[:-1]
            if word[-1] == '?': end_chars = '?' + end_chars; word = word[:-1]
            if word[-1] == ',': end_chars = ',' + end_chars; word = word[:-1]
            if word[-1] == '.': end_chars = '.' + end_chars; word = word[:-1]
            if word[-1] == ';': end_chars = ';' + end_chars; word = word[:-1]
            else: break
        try: word_arpa = thisdict[word.upper()]
        except: word_arpa = ''
        if len(word_arpa)!=0: word = "{" + str(word_arpa) + "}"
        out = (out + " " + word + end_chars).strip()
    if out[-1] != "␤": out = out + "␤"
    return out

thisdict = {}
def get_arpa_dict(filename):
    for line in reversed((open(filename, "r").read()).splitlines()):
        thisdict[(line.split(" ",1))[0]] = (line.split(" ",1))[1].strip()
    return thisdict

graph_scale = 1
alignment_graph_width = 1800
alignment_graph_height = 720
colormap = 'inferno'
def plot_data(data, info=None):
    fig, axes = plt.subplots(1, len(data), figsize=(int(alignment_graph_width*graph_scale/100), int(alignment_graph_height*graph_scale/100)))
    for i in range(len(data)):
        axes[i].imshow(data[i], aspect='auto', origin='lower', 
                       interpolation='none', cmap=colormap)
    axes[0].set(xlabel="Frames", ylabel="Channels")
    axes[1].set(xlabel="Decoder timestep", ylabel="Encoder timestep")
    fig.canvas.draw()
    plt.show()


waveglow_gdrive_ids = ['1DMyL3RxFqAVhH60VCLnVaDt2YJb2RCfz', '10wDUQ3HAKhdNgnqZC3PBDBZ12PADZWAU', '14ajSxb4yJXQnv_nf9O89dIWcfdvUFFZo', '1H707kelxad-DuWBBmDGgR48b5KCS0ta8', '1lDzc_asOMCrf86XcfHKTSCnYBojb0VR-', '1Rmm81f6-NJQ-6T2JCtwS6XZedrrXoW0E', '1sMYb2HixSOSEHR1mOoBkXMHOlJ4vAV-m', '1lDRZtuPoYObMen9klwSIQPQ5lLkpp3mi', '1F__M3bwVuZkeHFULkoQgef8QB5Tx6_24', '14DJNfpPUnSNOfamRQzKgqaU4Y87zE3-c', '1_AjAgDGm_bf0t4-yznCoD0foPKyp4YPW']
arpa_dictionary_mega_url = 'https://mega.nz/file/aJJ0mQiT#u9NQ9-rL53Tv0z__9SvCiLznJDLq1lyoAuEiy7CwiCM'

from mega import Mega
from importlib import reload
def download_arpa_dict(destination, url=arpa_dictionary_mega_url):
    mega = Mega()
    mega_login = mega.login() # anonymous account
    mega_login.download_url(arpa_dictionary_mega_url, destination)
    reload(Mega)
    
# 