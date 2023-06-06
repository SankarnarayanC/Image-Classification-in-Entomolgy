# Image-Classification-in-Entomolgy
 <br>
<h3>ABSTRACT:</h3><br>
      This Machine Learning Model is a supervised learning model which is trained in order to classify different Insect specimens. It uses the Image classification, an integral part of Computer Vision applications. This project mainly focusses on TRADITIONAL METHODS of Machine learning with Computer Vision. <br>
      <br> Since LadyBugs tend to carry patterns/spots, they come in a variety, each of which is gravely important to maintain the balance in nature. They are also one of the great pollinators available. Ladybugs are mainly seen on vegetation which carry APHIDS - A pest that ruins the growth of plants. Since Ladybugs prey on Aphids, they are seen in huge numbers near them. It thus becomes very important to classify and identify these set of specimens on the field. This would ultimately benefit the private collectors and environmentalists to keep a track of their numbers. Thus identifying the pattern on the specimen and classification is what is done in this project.
      <br>
      <br> The supervised learning model used for this project is the RANDOM FOREST CLASSIFIER. <br><br> The four different classes are :
      <br>
      1) Transverse LadyBug <br>
      2) 7 Spotted LadyBug <br>
      3) 22 Spotted LadyBug <br>
      4) Polished LadyBug <br>
      <br>
      <div>
      <img src="Images/Beetle 13.jpg" width="190" height="200">
      <img src="Images/Butterly 16.jpg" width="190" height="200">
      <img src="Images/Grass Hopper 29.jpg" width="190" height="200">
      <img src="Images/Beetle 23.jpg" width="190" height="200">
      </div>
      <br> The DATASET used for this was multiple images downloaded from the internet for four different classes. These were downloaded, pre-processed and resized and later renamed to get continuity in the dataset.<br> <br> Using the algorithms and filters from Computer Vision and Digital Image processing, filter responses were recorded and were then used as features. 
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
 
For the smooth execution of the project, Jupyter Notebook platform was used and PYTHON was the programming language used along with multiple libraries and frameworks to support it.

<h3>Results:</h3><br>
      An average of 82.01% accuracy was seen in the model's performance during the testing of the validation set. The results recorded are as follows.
      <br>
      <br>
     <img src="Images/classification results-2.png" width="1000" height="400">

<br> The classification of the class 7 Spotted-Ladybug and Polished-Ladybug had a higher accuracy as compared to that of the 22 Spotted-Ladybug and Transverse-Ladybug classes. <br>
The confusion matrix showing the visualisation of the test results is shown below.
<br>
<br>
<div>
<img src="Images/Confusion Matrix-2.png" width="600" height="500">
 </div
<br>  
<br>
<h3>Future Updates/Improvements/Discussions:</h3><br>
     I plan to study and implement other important feature extracting filters and algorithms and thus try to improve the accuracy of the model. Along with that, I also plan to use already existing appropriate and suitable Datasets. Also planning to implement Image annotations on the same dataset with good quality annotations and use the same model (Random Forest Classifier) with some changes in it to get enhanced results with better accuracy. 
 <br>
 The main inference for lesser accuracy is that for a limited training set, it is very difficult to classify as the specimens tend to have the same morphological structure. Many of the specimens under the CLASS INSECTA look similar if their morphology is seen. Thus one will need a larger number of training image set to classify the images with higher accuracy. Thus methods like CNN (Deep learning) might give more accuracy and enhanced results.
