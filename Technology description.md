目的: 通过比较不同时期航空影像中的建筑面积, 反映农村人口与经济发展

数据: 谷歌地球历史影像 2010, 2014, 2017, 2021四个时期

方法: 通过标注一定数量航空图像, 训练深层神经网络模型, 利用模型进行自动的建筑物分割, 依据图像的分辨率与预测语意分割图, 计算出分水镇的建筑面积. 神经网络框架采用state-of-art的U-Net模型. 全镇面积214.6km2, 像素分辨率0.51m, 总的图像分辨率为39012x44540, 图像被裁剪到256x256分辨率, 单个时期的图像数量为11237张. 分别从四个时期从随机抽选出300张包含房屋的图像crop作为训练集, 利用roboflow网页应用进行手动标注, 剩余图像作为验证集与测试集.

模型: 采用U-Net作为神经网络框架, 输入通道为256x256x3, 输出结果为房屋和背景. 整个模型利用PyTorch深度学习库实现, 编程语言为Python, 利用GPU加速模型训练. 模型的评估采用F1-score作为评价指标. 公式如下:

![image-20230209234045292](/Users/morin/Library/Application Support/typora-user-images/image-20230209234045292.png)

![image-20230209234055431](/Users/morin/Library/Application Support/typora-user-images/image-20230209234055431.png)

![image-20230209234102558](/Users/morin/Library/Application Support/typora-user-images/image-20230209234102558.png)

We can calculate buildings areas to indicate economical developement and living condition in rural areas. A common way is to utilize computer vision technology to implement automatic building segmentation. Recently, deep convolutional neural networks (CNNs) have shown the best performance and become the state-of-art models in the field of image segmentation. The U-Net architecture, a fast and precise convolutional network, is utilized in this paper for image segmentation.  The land area in Fenshui town is 214.6 km^2, we download 4 different historical aerial images in 2010, 2014, 2017, 2021, respectively. Pixel resolution is 0.51m and a large image is cropped into 11237 256x256 resolution images per time period. A major challenge of deep learning methods is that they are extremly data hungry. To adapt in different backgrounds and image conditions, the model is trained on manually labelled data and then can be used to predict on remain data. All images are splitted into training, validating and testing parts, respectively. To get more precise result from different sensing period of time, we randomly select 300 images as the trainning data for each time period and collect totally 1200 images which contains buildings. And we use roboflow web application to manully label these images. The images are the input of the U-Net model, and the output is the 2-value classification which turns out building and background. The neural architecture is implementd by PyTorch library using Python programming language. F1-score is the main index to evalute results.



This study aims to assess the economic development and living conditions in rural areas by calculating building areas. One method to achieve this is through the use of computer vision technology and automatic building segmentation. Deep convolutional neural networks (CNNs), specifically the U-Net architecture, have been proven to be the state-of-the-art models for image segmentation and are utilized in this paper.

The study focuses on Fenshui town, which has a land area of 214.6 km^2. Four different historical aerial images from the years 2010, 2014, 2017, and 2021 were obtained and processed, with a pixel resolution of 0.51m. To accommodate the large images, each image was cropped into 11237 256x256 resolution images per time period.

One major challenge of deep learning methods is their need for vast amounts of data. To address this, the U-Net model was trained on manually labeled data to adapt to various image backgrounds and conditions. The images were divided into training, validation, and testing sets, with 300 randomly selected images per time period used as training data, totaling 1200 images containing buildings. These images were labeled using the roboflow web application and served as input to the U-Net model. The output was a 2-value classification of buildings and background.

The U-Net architecture was implemented using the PyTorch library and Python programming language. The F1-score was used as the main index to evaluate the results.



## IMPROVED BY ChatGPT

This study aims to assess economic development and living conditions in rural areas by calculating building areas. One method to do this is by using computer vision technology and automatic building segmentation. Deep convolutional neural networks (CNNs), particularly the U-Net architecture, are proven to be the state-of-the-art models for image segmentation and are used in this study.

The study focuses on Fenshui town, which has a land area of 214.6 km^2. Four historical aerial images from the years 2010, 2014, 2017, and 2021 are obtained and processed, with a pixel resolution of 0.51m. To accommodate the large images, each image is cropped into 11237 256x256 resolution images per time period.

One major challenge of deep learning methods is their need for vast amounts of data. To address this, the U-Net model is trained on manually labeled data to adapt to various image backgrounds and conditions. The images are divided into training, validation, and testing sets, with 300 randomly selected images per time period used as training data, totaling 1200 images containing buildings. These images are labeled using the roboflow web application and serve as input to the U-Net model. The output is a 2-value classification of buildings and background. The U-Net is considered a complex and extensive non-linear functional model that takes data as input, encodes it, and processes it through the network to generate the output. The discrepancy between the expected output and the actual output produces the loss, which is then used by the backpropagation algorithm to calculate the gradient of the neural network parameters. These parameters are subsequently optimized with each training epoch. The U-Net architecture is implemented using the PyTorch library and Python programming language. The F1-score is used as the main index to evaluate the results.