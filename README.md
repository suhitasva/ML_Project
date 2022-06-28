# Predicting House Sale Prices - Ames, Iowa

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link" href="http://www.linkedin.com/in/suhita-acharya" target="_blank" rel="noreferrer noopener">LinkedIn</a></div>
<!-- /wp:button -->

<!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link" href="https://github.com/suhitasva">GitHub</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->

<!-- wp:heading {"level":1} -->
<h1>Introduction</h1>
<!-- /wp:heading -->

<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:paragraph -->
<p>Over the last two years, house sales prices have skyrocketed, and home buyers are paying more than the asking price to grab any available home in this real estate frenzy. A CNN Business <a href="https://www.cnn.com/2022/06/22/investing/premarket-stocks-trading/index.html" target="_blank" rel="noreferrer noopener" title="article">article</a> states that the National Association of Realtors said in a report on Wed June 22, 2022, that the median home price in May topped $400,000 for the first time, hitting a record of $407,600. That's up nearly 15% from a year ago. At this time, a tool that helps predict house sales prices based on its features, could prove to be handy. The said tool could assist realtors/mortgage lenders to render precise performance in such a cut-throat sales market.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The objective of this project is to create a machine learning model that can assist home realtors/mortgage lenders to determine a house’s sales price. I wanted the model to use existing information provided about the home; its features such as the number of bedrooms/bathrooms, basement size, garage size/capacity, etc. to predict the house sales price. Through this research, I also made some recommendations about some probable ways that may get the homeowners a high sales price. Several models were developed, and some were shortlisted to create an optimal price determination tool.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Factors affecting House Sales Price:</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Any house's sale price depends upon some universal factors that make the house more desirable among the pool of potential buyers. Some of these factors include:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Location</li><li>Usable Space</li><li>House Condition (external and internal)</li><li>Remodeling</li><li>The number of bedrooms/bathrooms</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>For this project, I decided to focus on the house properties only and how they can influence sales price. According to an <a href="https://www.opendoor.com/w/blog/factors-that-influence-home-value" target="_blank" rel="noreferrer noopener" title="article">article</a> by Opendoor, a home’s usable space (not garages, attics, and unfinished basements) matters when determining its value. Similarly, homes that are newer possibly remodeled, and in good condition appraise at a higher value.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Dataset Introduction</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The house sales data used in this project comes from a Kaggle dataset - <a href="https://www.kaggle.com/c/house-prices-advanced-regression-techniques" target="_blank" rel="noreferrer noopener" title="House Prices - Advanced Regression Techniques">House Prices - Advanced Regression Techniques</a>. This dataset includes sales price information for several homes in Ames, Iowa. Along with the sales price, we also get in this dataset 79 explanatory variables describing (almost) every aspect of the residential homes. Some of these variables give information on Lot Frontage/shape, neighborhood, house condition/quality, year remodeled, roof material, etc. The aim here is to use these unique descriptors in creating a model to best predict house prices. </p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>House Sales Price Analysis</h2>
<!-- /wp:heading -->

<!-- wp:gallery {"linkTo":"none"} -->
<figure class="wp-block-gallery has-nested-images columns-default is-cropped"><!-- wp:image {"id":85962,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img6-583883-ts7rIZTI.png" alt="" class="wp-image-85962"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":85961,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img7-327663-ZWwxkAqH.png" alt="" class="wp-image-85961"/></figure>
<!-- /wp:image --><figcaption class="blocks-gallery-caption"><strong>House Sale Prices - Before and After Log-Transformation</strong></figcaption></figure>
<!-- /wp:gallery -->

<!-- wp:paragraph -->
<p>In my quest to figure out what factors influence a house's sales price, the first thing that I looked at was how the distribution looked for all sale prices. Sales prices for the houses were right-skewed and required log transformation for a more Gaussian-like distribution. This step ensures that our model achieves the goal of linearity. I then conducted some exploratory data analysis to research relationships between the dataset variables and the house sales price. </p>
<!-- /wp:paragraph -->

<!-- wp:gallery {"linkTo":"none"} -->
<figure class="wp-block-gallery has-nested-images columns-default is-cropped"><!-- wp:image {"id":85915,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img1-640409-fuY9hSVG.png" alt="" class="wp-image-85915"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":85916,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img2-683246-NnHymk1t.png" alt="" class="wp-image-85916"/></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->

<!-- wp:paragraph -->
<p>What we can see from these graphs here is that there is a clear relationship between some of the numerical/categorical features and the sales prices. The higher the first floor and total above-ground living area, the higher the house's sales price will be. Similarly, if the sales price relation to some of the categorical features is looked at, we can gain some useful information. From the boxplots below, we can see that a house with a higher basement and overall house quality rating evaluation will surely command a higher sales price. </p>
<!-- /wp:paragraph -->

<!-- wp:gallery {"linkTo":"none"} -->
<figure class="wp-block-gallery has-nested-images columns-default is-cropped"><!-- wp:image {"id":85922,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img3-499299-WEMOV4jH.png" alt="" class="wp-image-85922"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":85921,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img4-414291-1maohIY5.png" alt="" class="wp-image-85921"/></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->

<!-- wp:heading -->
<h2>Data Preprocessing</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Next, before going into more detail on the data modeling let us first discuss how the data was preprocessed which is a crucial step in machine learning (several model types are sensitive to outliers). Upon initial evaluation, I notice some of the data variables had a lot of missing values. Missing values were imputed in the data accordingly. For example, I saw a lot of missing values in Pool QC and Fence categorical features, meaning the houses probably did not have a pool or a fence. In such cases, values were imputed as "No Pool" and "No Fence". For any missing numerical area-related missing values, the value of zero was added.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":85924,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img5-781811-dGVeZXXa.png" alt="" class="wp-image-85924"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>I also removed extreme outliers (something that can make our model prediction) from some of the features such as a single categorical value for the Utilities feature. Another thing that I changed in terms of preprocessing was that I changed the data type for some numerical columns with year, and month-related information to categories.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Feature Engineering</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>After the basic data preprocessing, I also created some numerical and categorical features and combined some categories into one for some categorical features.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>New Numerical Features:<ul><li>sold_age = Age of the house when it was sold.</li><li>Usable_space = Sum of basement, above ground, first and second floor areas.</li><li>yr_since_remod = Years since the remodeling was done.</li><li>Total_Halfbaths = Sum of all half baths.</li><li>Total_Fullbaths = Sum of all full baths.</li><li>Encl_Porch_tot = Sum of all enclosed porch areas.</li><li>BsmtFinSF = Sum of Type 1 and Type 2 finished basement area.</li></ul></li><li>New Categorical Features:<ul><li>remod_y_n: Whether house was remodeled or not.</li></ul></li><li>Combined values in categorical features:<ul><li>LandContour: replacing values other than Lvl to Notlvl.</li><li>Heating: replacing values other than GasA to Heat_other.</li><li>Electrical: replacing values other than SBrkr to Electr_other.</li><li>PavedDrive: replacing values other than Y to NP.</li></ul></li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>House Sales Price Analysis (New Features):</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>After creating the new features to understand the data better, I also studied the relationship of some of these features to the house sales prices. One of the interesting clear relationships that I uncovered was between House Sales Price and Usable Space Area. It looked like a house with greater usable space area, will cost much more than a house with a low area.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86043,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img8-016872-DeUCuFCY-1024x615.png" alt="" class="wp-image-86043"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Similarly, I also looked at how the sales price was related to whether the house was remodeled or not and the years since it was remodeled. It seems like the homes that were more recently remodeled had a higher median sales price than those that were remodeled 60 years ago. If we look at the boxplot below, we can see that although the average house sales price is lower for remodeled houses, some of the remodeled houses have commanded higher sales prices than ones that were not.</p>
<!-- /wp:paragraph -->

<!-- wp:gallery {"linkTo":"none"} -->
<figure class="wp-block-gallery has-nested-images columns-default is-cropped"><!-- wp:image {"id":86045,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img9-728049-3FL6XW4u.png" alt="" class="wp-image-86045"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":86044,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img10-718882-ecRCv05t.png" alt="" class="wp-image-86044"/></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->

<!-- wp:heading -->
<h2>Data Modeling</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Next, we will look at the regression models (both linear and tree-based models were attempted) attempted for this project. All the data was log-transformed and numerical features were standardized. Models were trained/evaluated on a 70:30 train-test split.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Linear Models:</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For the Linear models, categorical features were either label encoded or dummified (see below) based on the type of feature. For these models, variables with high multicollinearity were removed (based on VIF values) for example Roof Style, and Garage Type. The types of Linear models attempted are listed below:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Multiple Linear Regression (MLR)</li><li>Ridge and Lasso Regression</li><li>Support Vector Regression</li></ul>
<!-- /wp:list -->

<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:image {"align":"center","id":86055,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img11-304330-mtCJrmh0.png" alt="" class="wp-image-86055"/></figure></div>
<!-- /wp:image -->

<!-- wp:heading {"level":4} -->
<h4>Multiple Linear Regression (MLR):</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For the final MLR model, independent features were selected via Lasso regression (hyperparameter alpha was chosen by grid search cross-validation). List of selected features (Lasso alpha=0.01) is shown below.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86057,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img12-732938-hsTMtc1r.png" alt="" class="wp-image-86057"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>If we look at the residuals and prediction error plots for this model, we see that the residuals are fairly random and uniformly distributed and there is a decent linear agreement between the actual and predicted house sale price values. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86061,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img13-805682-q3B1EWzK-1024x412.png" alt="" class="wp-image-86061"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":4} -->
<h4><strong>Penalized Regression (PLR)</strong>:</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The results for the Ridge and Lasso PLR models are shown below. The only change to note is that, for the Lasso model, the data was normalized beforehand.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86078,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img14-677889-IxjNXyqA-1024x356.png" alt="" class="wp-image-86078"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>For both models, the residuals are uniformly distributed (low variation for the Ridge model), with a good agreement between the actual and the predicted house sales price values. The accuracy for both Ridge and the Lasso Regression models, (90.6% and 90% respectively) are decent and an improvement over the MLR model accuracy (87.6%).</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86079,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img15-840114-5xwbpg8Z-1024x383.png" alt="" class="wp-image-86079"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":86080,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img16-145146-lcSsZf7x-1024x397.png" alt="" class="wp-image-86080"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":4} -->
<h4><strong>Support Vector Regression Model (SVR):</strong></h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For the final SVR model, all the basic preprocessing steps were the same as other linear models. Some features with high multicollinearity were dropped. Some additional work was done in selecting model hyperparameters. Hyperparameters C (controls regularization; the strength of the regularization is inversely proportional to C), and epsilon (specifies the epsilon-tube within which no penalty is associated in the training loss function with points predicted within a distance epsilon from the actual value) were determined from plotting R<sup>2</sup> and errors for train and test data. Other hyperparameters (kernel coefficients gamma and kernel in this case) were selected by Grid Search CV.</p>
<!-- /wp:paragraph -->

<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:image {"align":"center","id":86099,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img17-491667-drQfqHem.png" alt="" class="wp-image-86099"/></figure></div>
<!-- /wp:image -->

<!-- wp:spacer {"height":"10px"} -->
<div style="height:10px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:paragraph -->
<p>In terms of uniform residual distribution, actual/expected sale price agreement and accuracy it seems like the SVR model fares much better than its other linear counterparts.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86102,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img18-897963-oZMGRdCb-1024x380.png" alt="" class="wp-image-86102"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3>Tree-based models</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For the tree-based models, categorical features were label-encoded only. Features with high multicollinearity were not dropped. The model hyperparameters which are listed below, were chosen by Grid Search CV. The types of tree-based models attempted are listed below:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Random Forest</li><li>XGBoost</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":4} -->
<h4>Random Forest (RF) model:</h4>
<!-- /wp:heading -->

<!-- wp:image {"align":"center","id":86261,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img3-240360-v9CWhYZj.png" alt="" class="wp-image-86261"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>For the final Random Forest model, the residual and prediction error plots provide us with impressive results. This model is an improvement over the other linear models; however, there seems to be a bit of a difference in the training and testing data accuracy, indicating overfitting.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86253,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img1-453515-X3W3pHFd-1024x573.png" alt="" class="wp-image-86253"/></figure>
<!-- /wp:image -->

<!-- wp:image {"align":"center","id":86254,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img2-619427-RTDS15mU.png" alt="" class="wp-image-86254"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Next, I also looked at the feature importances as provided by the final Random Forest Model to gain more information on which features were contributing to the results.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":86274,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img5-248249-MTqfDi8h-1024x588.png" alt="" class="wp-image-86274"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":4} -->
<h4>XGBoost Model:</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The next and the last model type that I attempted was the XGBoost. For this model type, I ran two different versions of this model. For one version, all features were used, and the other features were selected by Sklearn's Recursive Feature Selection (RFE). RFE is a feature selection algorithm that uses feature elimination to select features for the model to use. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As per Scikit Learn's <a href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html">documentation</a>, the estimator is trained on the initial set of features and the importance of each feature is obtained either through any specific attribute or callable. Then, the least important features are pruned from the current set of features. That procedure is recursively repeated on the pruned set until the desired number of features to select is eventually reached.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Lastly, the performances of both model types were compared with each other. For both models, the hyperparameter max_depth (the maximum depth of a tree) was determined from plotting R<sup>2</sup> and errors for train and test data. An eta (step size shrinkage used in update to prevent overfitting) hyperparameter value was selected to optimize performance. Other hyperparameters were selected by Grid Search CV.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86273,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img4-899026-ucw9ez2C.png" alt="" class="wp-image-86273"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The results for the XGBoost model with RFE selected features are displayed below. In the first graph below, we see the similarity between the predicted and expected house sale price value. The test dataset house sales values are in decent agreement with each other. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86285,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img7-436026-1fPR2Min.png" alt="" class="wp-image-86285"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The second graph shows the model importances as shown by the XGBoost model.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86301,"sizeSlug":"full","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-full"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img9-086589-u2RKzSiJ.png" alt="" class="wp-image-86301"/><figcaption><strong>XGBoost model feature importances</strong></figcaption></figure></div>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Final model evaluation metrics:</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The table below shows train and test data accuracy scores and errors for all the models attempted, including different versions for each. For all the model types, the final model had the RFE selected features, except for the XGBoost model for which the two different versions were run.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":86288,"sizeSlug":"large","linkDestination":"none"} -->
<div class="wp-block-image"><figure class="aligncenter size-large"><img src="https://nycdsa-blog-files.s3.us-east-2.amazonaws.com/2022/06/suhita-acharya/img8-534173-SE0TDOi5-1024x338.png" alt="" class="wp-image-86288"/></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Based on accuracies and RMSE (Root Mean Squared Error) scores, the SVR, XGBoost and XGBoost (RFE) models were shortlisted to be used for creation of the house sales price determination tool. These models were chosen because they were not overfitting and have relatively low errors scores.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If we look at the evidence provided by exploratory data analysis, we can see that overall house quality and usable available space inside the house matter when determining the final house sales price. Some other necessary characteristics that emerged while studying the data modeling results are listed below:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Overall condition that the house is in.</li><li>Finished Basement area (in square feet).</li><li>Total above ground living area (in square feet).</li><li>Whether the house has been remodeled or not.</li><li>Years since the house has been remodeled.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Based on what I have uncovered through the research in this project; the few things that I can recommend realtors/mortgage lenders do to possibly get a higher sales price are as follows:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Make sure the house on sale has more usable living space.</li><li>The realtor/mortgage lenders can check if the house, basement, and garage is are good condition and if evaluation rating is high. If not, steps need to be taken to correct this issue.</li><li>If the house basement is unfinished, recommend the seller consider getting it finished.</li><li>Recommending the seller for renovation if not done in a long time.</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>Future Work</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Something, I would like to do if given some more time with this data is to go back and do a more thorough data analysis and work to see if the models themselves can provide more insight not previously uncovered.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>References:</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>Paul R. La Monica, C., 2022. <em>Could a housing slump threaten the stock market and the entire economy?</em> [online] CNN. Available at: &lt;https://www.cnn.com/2022/06/22/investing/premarket-stocks-trading/index.html> [Accessed 27 June 2022].</li><li>Gomez, J., 2022. <em>8 critical factors that influence a home's value | Opendoor</em>. [online] Opendoor. Available at: &lt;https://www.opendoor.com/w/blog/factors-that-influence-home-value> [Accessed 27 June 2022].</li><li>Kaggle.com. 2022. <em>House Prices - Advanced Regression Techniques | Kaggle</em>. [online] Available at: &lt;https://www.kaggle.com/c/house-prices-advanced-regression-techniques> [Accessed 27 June 2022].</li><li>scikit-learn. 2022. <em>sklearn.feature_selection.RFE</em>. [online] Available at: &lt;https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html> [Accessed 27 June 2022].</li></ul>
<!-- /wp:list -->
