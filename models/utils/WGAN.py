import torch.nn as nn
import numpy as np

img_shape = (3, 64, 64)

class GeneratorBig(nn.Module):
    def __init__(self):
        super(GeneratorBig, self).__init__()

        def block(in_feat, out_feat, normalize=True):
            layers = [nn.Linear(in_feat, out_feat)]
            if normalize:
                layers.append(nn.BatchNorm1d(out_feat, 0.8))
            layers.append(nn.LeakyReLU(0.2, inplace=True))
            return layers

        self.model = nn.Sequential(
            *block(latent_dim, 128, normalize=False),
            *block(128, 512),
            *block(512, 2048),
            *block(2048, 6144),
            nn.Linear(6144, int(np.prod(img_shape))),
            nn.Tanh()
        )

    def forward(self, z):
        img = self.model(z)
        img = img.view(img.shape[0], *img_shape)
        return img
