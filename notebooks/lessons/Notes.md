
# supervised ML
# *ML Algorithms

1- linear regression (linear model)

2- classification:
 - binary (Logistic Regression)(linear model):(Scikit-learn)
   .clean the dataset
   .get the target var(y)
   .understand the data
   .classify the columns by dtype
   .find the most important feature that affect the target var.(mutual info)
   .apply one-hot encoding (in categorical features)
   . train the model with train,val
   .find the acc
   .check if the decision value is the best or need to change it
  - Decision trees
  - Random forests

# *Deep learning:(Tensorflow and keras)
 - Neural networks
 - Convolutional Neural Networks (CNNs): used for images.
 - Recurrent Neural Networks (RNNs)
 - Transformers (BERT, GPT)
 - Autoencoders
 - GANs

//////////////////////////////////////////////////////////

# *Deep learning:(pytorch)
automatic differentiation (autograd)
automatically computes gradients
Gradients are required for backpropagation, which updates neural network weights during training

gradients -> backpropagation (updates neural network weights during training)

During training:
x would be weights of a neural network.
y would be the loss.
y.backward() computes gradients.
Optimizer uses x.grad to update the weights.




//////////////////////////////////////////////////////////

Building Blocks of Convolutional Neural Networks (CNNs):-
1. Introduction:-
Convolutional Neural Networks (CNNs) are a special type of deep learning architecture designed mainly for image data. They automatically learn spatial features like edges, textures, shapes, and objects. A CNN is built using multiple specialized layers, each responsible for extracting and transforming information.

2. Main Building Blocks of CNN:-
# (a) Input Layer 
Accepts raw image data. 
Images are usually represented as Height × Width × Channels 
Example: RGB image = 128 × 128 × 3
# (b) Convolutional Layer (Conv Layer) 
This is the most important layer in CNN. 
It applies filters/kernels (small matrices, e.g., 3×3 or 5×5) to detect local patterns such as: 
Edges 
Corners 
Textures 
The operation performed is convolution, generating a feature map.
Formula for output size: 
Output = ( W − K + 2 P ) S + 1 
Where: 
W = Input width 
K = Kernel size 
P = Padding 
S = Stride
# (c) Activation Function (ReLU):-
Applies non-linearity to the feature maps. 
ReLU (Rectified Linear Unit) is most commonly used:
f(x)=max(0,x)
Note:-ReLU helps the network learn complex patterns and reduces the vanishing gradient problem.
# (d) Pooling Layer (Downsampling Layer):-
Reduces spatial size of feature maps. 
Common types: 
Max pooling: Selects maximum pixel value 
Average pooling: Computes the average value 
Example: 2×2 Max Pooling ↓ reduces size by half. 
Purpose: 
Reduces computation 
Prevents overfitting 
Makes features more invariant to translation
# (e) Dropout Layer:-
Randomly drops neurons during training (e.g., 20–50%). 
Prevents overfitting and improves generalization.
(f) Fully Connected Layer (Dense Layer) 
Final part of CNN, acts like a traditional neural network. 
Converts extracted features into final classification output.
# (g) Output Layer:-
Uses Softmax activation for multi-class classification: 

3. Flow of CNN Architecture:-
Input Image → Convolution → ReLU → Pooling → Convolution → ReLU → Pooling → Flatten → Fully Connected Layer → Output

4. Applications of CNN:- 
Image classification (cats vs dogs, medical diagnosis) 
Face recognition 
Object detection (YOLO, Faster R-CNN) 
Autonomous vehicles 
Handwritten digit recognition (MNIST dataset)

5. Advantages:-
Automatic feature extraction 
Works well with image data 
High accuracy for vision-based tasks

6. Conclusion:-
The building blocks of CNN work together to extract hierarchical features from edges to complex shapes leading to highly accurate image classification. CNNs are now a core technology in AI-driven image applications.