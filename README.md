# Music.Generation.with.DeepLearning

Generating Irish Folk Tunes and Lyrics - using LSTM¶
This project uses Long Short-term Memory (LSTM) -based recurrent neural network (RNN) to generate music and lyrics using the Irish Folk Music dataset. Additionally, it also generates "Bob Dylan-esque" lyrics, using all of Bob Dylan's songs. 


## Summary
We use the power of Deep Learning to train LSTM Networks to creatively generate Irish Folk Tunes and Bob Dylan lyrics

### Results

TLDR:
[![See video on YouTube]](https://www.youtube.com/watch?v=WsdJ6LP6f-E&feature=youtu.be)

See the video at: [here](Generating-Music-via-RNNs-Atul_Acharya.mp4)

### Write-up

### Datasets

#### Irish Folk Music 

As a lover of folk tunes, particularly Irish tunes, I found these datasets immensely helpful.
- **O'Neill's Irish Music dataset** (Source: http://trillian.mit.edu/~jc/music/book/oneills/1850/X/ )
- **Cobb's Irish Music dataset** (Source: http://cobb.ece.wisc.edu/irish/Tunebook.html )
- **Nottingham Music dataset** (ABC version of Nottingham music dataset: http://abc.sourceforge.net/NMD/)

I wrote a scraper to scrape O'Neill's and Cobb's data from the sites, clean up the data, and combine them in one file.

#### Bob Dylan Songs

I scraped the Bob Dylan songs site (http://bobdylan.com/songs/), downloaded the lyrics separately and combined them in one text file. It comes down a mere 700KB dataset, which is tiny for the purposes of training an RNN.

For copyright reasons, Bob Dylan's lyrics are not included in this repo.


### Char-RNN based Generator

The mechanics of the text generation uses a Char-RNN based generator, as decribed by Andrej Karpathy (http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

To create an RNN, specify the model_type as one 'lstm', 'rnn', or 'gru'. In general, the LSTM type networks have shown to be more effective (per Karpathy)

Specify these params:
- batch_size: sequences in a mini batch
- sequence_length: number of characters in a sequence
- n_cells: number of cells in the (hidden) RNN layers
- n_layers: number of layers in the RNN
- ckpt_name: unique name for the model; used to save the model or restore from it
- learning_rate: how fast or slow the network should learn (typically, 0.001, but can be set to 0.0001)

### ABC Music Format

The ABC Music format is a text-based music format. 

Here's one such tune, called **Julia Delaney** in ABC format: [See a youtube sample here: https://www.youtube.com/watch?v=DUZ6zei3fRU]
```
X:174
T:Julia Delaney
Z: id:dc-reel-161
M:C
L:1/8
K:D Minor
A|dcAG F2DF|E2CE F2DF|dcAG F2DF|Add^c defe|!
dcAG F2DF|E2CE F2DF|dcAG F2DF|Add^c d3:|!
e|fede fagf|ecgc acgc|fede fagf|edcA Adde|!
fede fagf|ecgc acgc|fedf edcA|Add^c d3:|!
```

As can be seen, the format is incredibly compact. Each line begins with a single letter field (except for notes). ABC notation for music (link: http://abcnotation.com/) 

- X denotes a reference number
- M denotes Meter
- K denotes the Key
- L denotes the beats
- T denotes the Title
- Z denotes the transcription The rest are notes that denote the melody for the song.

As one can see, this text data is useful to train an RNN to generate a similarly structed .abc, which can then be converted into .MIDI format, and from there to .WAV or .OGG format to play.


## References
A few of the references that helped me. More useful for future work.

* Andrej Karpathy - Unreasonable Effectiveness of RNN https://karpathy.github.io/2015/05/21/rnn-effectiveness/
* Music Generation using RNN — with char-rnn https://maraoz.com/2016/02/02/abc-rnn/
* Analyzing Deep Learning Tools for Music Generation — Asimov Institute http://www.asimovinstitute.org/analyzing-deep-learning-tools-music/
* Hexahedria - Daniel Johnson — Composing Music with RNN http://www.hexahedria.com/2015/08/03/composing-music-with-recurrent-neural-networks/
* Kyle McDonald — Creative AI - Return to ML - https://medium.com/@kcimc/a-return-to-machine-learning-2de3728558eb#.66hboziec
* Folk Music Generation — Bob Sturm https://highnoongmt.wordpress.com/2015/05/22/lisls-stis-recurrent-neural-networks-for-folk-music-generation/
WaveNet — DeepMind — Keras Implementation - https://github.com/basveeling/wavenet/
