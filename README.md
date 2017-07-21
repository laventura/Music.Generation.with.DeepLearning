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
O'Neill's Irish Music dataset (Source: http://trillian.mit.edu/~jc/music/book/oneills/1850/X/ )
Cobb's Irish Music dataset (Source: http://cobb.ece.wisc.edu/irish/Tunebook.html )
Nottingham Music dataset (ABC version of Nottingham music dataset: http://abc.sourceforge.net/NMD/)
Irish Music -- combined from Cobb's and O'Neills. I wrote a scraper to scrape O'Neill's and Cobb's data from the sites, clean up the data, and combine them in one file.

#### Bob Dylan Songs

I scraped the Bob Dylan songs site (http://bobdylan.com/songs/), downloaded the lyrics separately and combined them in one text file. It comes down a mere 700KB dataset, which is tiny for the purposes of training an RNN.


### Char-RNN based Generator

The mechanics of the text generation uses a Char-RNN based generator. 

To create an RNN, specify the model_type as one 'lstm', 'rnn', or 'gru'. In general, the LSTM type networks have shown to be more effective (per Karpathy)

Specify these params:
- batch_size: sequences in a mini batch
- sequence_length: number of characters in a sequence
- n_cells: number of cells in the (hidden) RNN layers
- n_layers: number of layers in the RNN
- ckpt_name: unique name for the model; used to save the model or restore from it
- learning_rate: how fast or slow the network should learn (typically, 0.001, but can be set to 0.0001)

