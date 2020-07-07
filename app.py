{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask,request,url_for,redirect,render_template,jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pycaret.classification import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import pickle\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Transformation Pipeline and Model Sucessfully Loaded\n"
     ]
    }
   ],
   "source": [
    "model = load_model('deployment_28042020')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "cols = ['area_worst','concave points_mean','texture_worst','concave points_worst','perimeter_worst','area_se','symmetry_worst','concavity_worst','texture_mean','compactness_se']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template(\"home.html\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/predict',methods=['POST'])\n",
    "def predict():\n",
    "    int_features = [x for x in reques.form.values()]\n",
    "    final = np.array(int_features)\n",
    "    data_unseen = pd.DataFrame([final],columns = cols)\n",
    "    prediction = predict_model(model, data-data_unseen,round = 0)\n",
    "    prediction = int(prediction.Label[0])\n",
    "    return render_template('home.html',pred='Expected Diagnosis will be{}'.format(prediction) )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Transformation Pipeline and Model Sucessfully Loaded\n"
     ]
    }
   ],
   "source": [
    "deployment_28042020 = load_model('deployment_28042020')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Pipeline(memory=None,\n",
       "          steps=[('dtypes',\n",
       "                  DataTypes_Auto_infer(categorical_features=[],\n",
       "                                       display_types=True, features_todrop=[],\n",
       "                                       ml_usecase='classification',\n",
       "                                       numerical_features=[], target='diagnosis',\n",
       "                                       time_features=[])),\n",
       "                 ('imputer',\n",
       "                  Simple_Imputer(categorical_strategy='not_available',\n",
       "                                 numeric_strategy='mean',\n",
       "                                 target_variable=None)),\n",
       "                 ('new_levels1',\n",
       "                  New_Catagorical_...\n",
       "                 ('group', Empty()), ('nonliner', Empty()), ('scaling', Empty()),\n",
       "                 ('P_transform', Empty()), ('pt_target', Empty()),\n",
       "                 ('binn', Empty()), ('rem_outliers', Empty()),\n",
       "                 ('cluster_all', Empty()),\n",
       "                 ('dummy', Dummify(target='diagnosis')),\n",
       "                 ('fix_perfect', Remove_100(target='diagnosis')),\n",
       "                 ('clean_names', Clean_Colum_Names()),\n",
       "                 ('feature_select', Empty()), ('fix_multi', Empty()),\n",
       "                 ('dfs', Empty()), ('pca', Empty())],\n",
       "          verbose=False),\n",
       " XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,\n",
       "               colsample_bynode=1, colsample_bytree=0.9, gamma=0,\n",
       "               learning_rate=0.66, max_delta_step=0, max_depth=60,\n",
       "               min_child_weight=1, missing=nan, n_estimators=600, n_jobs=-1,\n",
       "               nthread=None, objective='binary:logistic', random_state=4256,\n",
       "               reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,\n",
       "               silent=None, subsample=0.5, verbosity=0)]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "deployment_28042020"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
