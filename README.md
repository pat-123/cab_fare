This project is about predicting the fare of a cab ride, given the coordinates of pick/drop off, along with the pickup timestamp

Few points worth mentioning regarding directory structure:
- train and test dataset is placed under data/raw/
- Processed data is placed under data/processed after computation
- Test predictions are available under data/submitted
-  *** Methods used in the notebook are placed under utils package
- Notebook is present in notebooks folder
- cab_fare is a package which load all initial packages(__init__.py) and sets data file paths under config.py
  ++ Abstracts the messy paths in the main notebook to here, so that cleaner view can be provided
- scripts folder is a placeholder for future purposes

-  Demonstrated model results with train_test_splits and also KFolds 

- write a OOPS style framework for running different ML regressor algo on the cleaned data and compare performance and choose the best ML model suited for this model

---------------------------------------------------
How to run this?
-----------------------------------------------------
- start Anaconda prompt and go to this folder's parent location and type jupyter notebook or just go inside the folder notebooks in the cur directory and type 'jupyter notebook Santander' on anaconda prompt.
- FYI- In the first option, notebook starts with the parent folder as the base location and you can navigate to different projects from there


------------------------------------------------------
SUMMARY
----------------------------------------------------
This project is about predicting the fare of a cab ride, given the coordinates of pick/drop off, along with the pickup timestamp

----------------------------------------------------
1.Exloratory data analysis
----------------------------------------------------
The major part of this project is cleaning data properly. Before testing any hypothesis, or any new col additions(feature engineering), we should always clean the data and try to get a reasonable corrleation of Independent var and dependent variables. 
So basically aim should be just get a reasonable correlation and then proceed to feature engineering, analysis, hypothesis checking and categorical varaiables

- If we dont remove the outliers in distance and fare prices and passenger counts , then the correlation b/w distance,passenger_count wit fare_amount is really low.

-- We have passenger counts >6 and a few are 0, and even fractional

-- we have distances which are costing the same as lesser distances with passenger count kept as a constant, which implies another factors like wait time, traffic congestion or renting the cab even for few days (for extremely high rents like 400,4343,5343 on the range closely lying on fare with cap of say 30)
External factors like dropoff timestamp, waiting time, cab type(luxury/hatch back/suv) are not provided.


--- But since we dont have any of such indepedent variables in this dataset, it is best to ignore the outliers, since they will confuse our model.

-- we have fare amounts very high on scale, so need to remove the outliers, as they cant be explained by the independent variales present in the set

-- we have passengr counts >10, which is not true even if your renting a minivan
---- In the subset with passenger counts =0, or >10, observed posotive corelation b/w distance and fare, implying legit observations and we would not want to loose those,
so passenger counts were replaced by the mode of passenger count of the observations, which had the same range of fares as this subset with bad passenger counts had. 
In this case it was passenger_count =1

Now after doing all the exploratory data anyalsis, our corr b/w distance and price was 0.76

-- Distance calculation
Euclidian, manhattan and geodesic distances were calculated , and euclidian had the strongest correlation with price, although all were very close in the competition

-- pickup timestamp analysis
Derived information like was the ride took on a weekend, month end/start, peak night times(10pm-4AM) , peak evening hours(5pm-8pm) , afternoon times or any other normal times, year end, year start
-- The rides on month start/end had higher average fares . Peak night times had greater fares slightly than peak evening hours in any time of the month
-- only evening rides in month start showed a little rise in price, followed by noon times in month start and ending

-- so overall  month start/end and peak night times recorded highest fares

----------------------------------------------------
2. Feature engineering
----------------------------------------------------
pickup_datetime is given, but it is in string format.
- first, convert datetime to timestamp object
- second, derive new features/predictors like month,date,year,peaktime or regular, noon/evening/night ride, season information, weekday,day of month

With these new features, derived information like if rides in evening/night have higher fare than other timings
- does month start/end have any effect on ride fare

------ Peak night times(11pm-4AM) recorded the highest mean fares
------ day/weekday has no effect
------- seasons have no effect either
------- time of the day like early morning or peak evening times had higher fares than the rest
-------- Also year wise also, higher fares are seen towards 2014,2015

----------------------------------------------------
3. Model creation
----------------------------------------------------
All numeric fields were normalized and passed to Linear regression model
- It give the lowest rmse value and highest model score(r2 coefficient)
Please check detailed report for further information
 
