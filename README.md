# Image-Classification-in-Entomolgy
 <br>
<h3>ABSTRACT:</h3><br><br>
      This Machine Learning Model is a supervised learning model which is trained in order to classify different Insect specimens. It uses the Image classification, an integral part of Computer Vision applications. This project mainly focusses on TRADITIONAL METHODS of Machine learning with Computer Vision. <br>
      The supervised learning model used for this project is the RANDOM FOREST CLASSIFIER. <br><br> The four different classes are :
      <br>
      1) Beetle <br>
      2) Butterfly <br>
      3) Dragonfly <br>
      4) Grasshopper <br>
      <br>
      <div>
      <img src="Images/Beetle 13.jpg" width="200" height="200">
      <img src="Images/Butterly 16.jpg" width="200" height="200">
      <img src="Images/Grass Hopper 29.jpg" width="200" height="200">
      </div>
      <br> The DATASET used for this was multiple images downloaded from the internet for 4 different classes. These were downloaded, pre-processed and resized and later renamed to get continuity in the dataset.<br> <br> Using the algorithms and filters from Computer Vision and Digital Image processing, filter responses were recorded and were then used as features. 
 <br>
These were:<br>
      1) The pixel values from different channels.
      <br>
      2) The Gray scale pixel values from images.<br>
      3) Canny edge detection filter responses.<br>
      4) Sobel edge detection filter responses.<br>
      5) Scharr, Robert and Prewitts edge detection filter responses.<br>
      6) Gabor filter bank responses.<br>
 <br>
 
For the smooth execution of the project, Jupyter Notebook platform was used and PYTHON was the programming language used along with the multiple libraries and frameworks to support it.

<h3>Results:</h3><br><br>
      An average of 68.05% accuracy was seen in the model. The results are as follows.
      <br>
      <br>
     <img src="Images/accReport.png" width="1000" height="400">

<br><br> The classification of the class Beetle and Butterly was done with higher accuracy as compared to that of Grasshopper class and Dragonfly class. <br>
The confusion matrix showing the visualisation of the test results is as below.
<br>
<br>
<img src="Images/Confusion matrix.png" width="800" height="800">
      
