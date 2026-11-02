# Autoencoders

Autoencoders are neural networks that compress input data into a smaller representation and then reconstruct it, helping the model learn important patterns efficiently. Their key uses include:

- Helps remove unwanted noise from data and improve quality.
- Identifies unusual patterns or anomalies in data.
- Extracts important features for better model performance.

## Architecture

An autoencoder’s architecture consists of three main components that work together to compress and then reconstruct data which are as follows:

### Encoder

It compress the input data into a smaller, more manageable form by reducing its dimensionality while preserving important information. It has three layers which are:

- Input Layer: Here the original data enters the network. It can be images, text features or any other structured data.
- Hidden Layers: These layers perform a series of transformations on the input data. Each hidden layer applies weights and activation functions to capture important patterns, progressively reducing the data's size and complexity.
- Output (Latent Space): The encoder outputs a compressed vector known as the latent representation or encoding. This vector captures the important features of the input data in a condensed form helps in filtering out noise and redundancies.

## Bottleneck (Latent Space)

The bottleneck is the smallest layer in the network that holds a compressed representation of the input data. It forces the model to keep only the most important features, helping it learn key patterns and improve generalization.

## Decoder

It is responsible for taking the compressed representation from the latent space and reconstructing it back into the original data form.

- Hidden Layers: Progressively expand the latent vector back into a higher-dimensional space. Through successive transformations decoder attempts to restore the original data shape and details
- Output Layer: Produces the reconstructed output which aims to closely resemble the original input. The quality of reconstruction depends on how well the encoder-decoder pair can minimize the difference between the input and output during training.
