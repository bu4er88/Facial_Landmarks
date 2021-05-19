# Facial_Landmarks is built from scratch.
1. For better and faster learning custom Wing Loss was implemented and used during training the model.
2. There were only one type of data augmentation implemented: vertical flip. However it is also necessary to do 90-degree rotation and differet stratching for images with faces in order to get robust localization. 
3. During augmentation the coressponding landmarks' coordinates were rescaled.
4. Model has been trained on downsized images, thus landmarks' coordinates had to be rescaled accordingly. Also predicted coordinates were upsized according to the images' shapes.

# Models used:
1. "CNN-6"-like simple CNN with Wing Loss (https://arxiv.org/abs/1711.06753).
2. ResNet with 'imagenet' weights (finetuning was performed for all layers).
3. VGG with 'imagenet' weights (finetuning was performed for all layers).

# Results achieved
![TEST_IMAGES](https://user-images.githubusercontent.com/71853448/118872154-ee068a80-b8f0-11eb-8fda-6272bde0f890.png)

