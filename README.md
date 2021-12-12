# [WGAN] Generating houses

Hello! This is how we reused the original implementation of ![WGAN](https://arxiv.org/abs/1701.07875) from ![this repo](https://github.com/eriklindernoren/PyTorch-GAN/tree/master/implementations/wgan) for generating custom pictures of houses. 

## Dataset

To get our pictures, we used ![selenium](https://github.com/SeleniumHQ/selenium) for python and Google Image Search. Our crawler is ![here](https://github.com/Dmmc123/wgan_houses/blob/main/Crawler.ipynb). Initially, our crawled pictures look like this (resized in 64x64 format):

![image](https://user-images.githubusercontent.com/54360024/145727574-b0db3573-187c-401e-906d-95eb5dc8cffb.png)

## Training

Hyper-parameters and algorithms do not differ much from the one presented in ![original paper](https://arxiv.org/abs/1701.07875), which is implemented in ![this notebook](https://github.com/Dmmc123/wgan_houses/blob/main/models/WGAN.ipynb), or ![original tutorial](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html) which is implemented in ![this notebook](https://github.com/Dmmc123/wgan_houses/blob/main/models/DCGAN.ipynb).

## Set-up

1. First things first, make sure you have last version of our ![generator](https://drive.google.com/file/d/1-4OGlyFqEcRA9ayx1WLlUjAoQ2jdW34F/view?usp=sharing) and ![discriminator](https://drive.google.com/file/d/1-3yLZP5J3RVmREU72hOsoTWfJ1KWBvgu/view?usp=sharing) modules on your Google Drive

2. Then clone this repo:

```
git clone https://github.com/Dmmc123/wgan_houses.git
```

3. Use notebooks accordingle to crawl data or re-train the models 
