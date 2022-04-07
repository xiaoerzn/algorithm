def get_model():
   input_img = Input(shape=(28*28,))
   encoded = Dense(100, activation='relu')(input_img)
   decoded = Dense(784, activation='sigmoid')(encoded)
   autoencoder = Model(input=input_img, output=decoded)
   encoder = Model(input=input_img, output=encoded)
   autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
   return autoencoder,encoder