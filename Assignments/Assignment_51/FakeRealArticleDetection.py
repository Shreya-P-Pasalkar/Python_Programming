#########################################################################################
#   Required Modules
#########################################################################################
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#########################################################################################
#   Function Name : DisplayStart
#   Description   : It is used to display header
#   Input         : Info
#   Output        : None
#   Date          : 03/05/2026
#   Author        : Shreya Pramod Pasalkar 
#########################################################################################
def DisplayStart(Info) :
    Border = "="*100

    print(Border)
    print(f"{Info.center(100)}")
    print(Border)

#########################################################################################
#   Function Name : DisplayEnd
#   Description   : It is used to display header (at the end)
#   Input         : None
#   Output        : None
#   Date          : 03/05/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def DisplayEnd() :
    Border = "- - "*25

    print(Border,"\n")

#########################################################################################
#   Function Name : LoadDataset
#   Description   : It is used to load dataset 
#   Input         : None
#   Output        : Dataframe
#   Date          : 03/05/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def LoadDataset() :
    df_fake = pd.read_csv("Fake.csv")
    df_true = pd.read_csv("True.csv")

    print("Both Datasets Loaded Successfully!\n")

    return df_fake,df_true

#########################################################################################
#   Function Name : CreateSingleDF
#   Description   : It is used to create a single dataframe from two df's
#   Input         : df_fake, df_true
#   Output        : Dataframe
#   Date          : 03/05/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def CreateSingleDF(df_fake, df_true) :
    # Adding Label Column to both the csv's
    df_fake["Label"] = 0
    df_true["Label"] = 1

    print("Head of Fake.csv after Label Column : ")
    print(f"{df_fake.head()}\n")

    print("-"*80)

    print("\nHead of True.csv after Label Column : ")
    print(df_true.head())

    # Concatenate Two Dataframes
    df_final = pd.concat([df_fake,df_true],ignore_index = True)     # ignore_indes resets the index

    df_final.to_csv("Final_BeforeShuffle.csv",index = False)

    # Shuffling rows of Contantenated DF 
    df_final = df_final.sample(frac = 1, ignore_index = True)     # Frac set to 1 to shuffle all rows

    df_final.to_csv("Final_AfterShuffle.csv",index = False)

    print("-"*80)
    print("Dataframe created successfully!")

    return df_final

#########################################################################################
#   Function Name : EDA
#   Description   : It is used to perform Exploratory Data Analysis
#   Input         : Dataframe
#   Output        : None
#   Date          : 03/05/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def EDA(df) :
    ############################################################################

    # First 5 rows of the Dataset
    print("-"*80)
    print("First 5 rows of the Dataset : ")
    print("-"*80)
    print(df.head())
    print("-"*80)
    print()

    ############################################################################

    # Columns in dataset
    print("-"*80)
    print("Columns in the dataset : ")
    print("-"*80)
    print(df.columns.tolist())
    print("-"*80)
    print()

    ############################################################################

    # Statistics of dataset
    print("-"*80)
    print("Statistics of Dataset : ")
    print("-"*80)
    print(df.describe())
    print("-"*80)
    print()

    ############################################################################

    # Missing Values 
    print("-"*80)
    print("Missing Values : ")
    print("-"*80)
    print(df.isnull().sum())
    print("-"*80)
    print()

#########################################################################################
#   Function Name : DataPreprocessing
#   Description   : It is used to perform data preprocessing
#   Input         : Dataframe
#   Output        : Dataframe
#   Date          : 03/05/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def DataPreprocessing(df) :
    # Handling Null Values
    print("-"*80)
    print("Missing Values : ")
    print("-"*80)
    print(df.isnull().sum())
    print("-"*80)
    print()
    print("No missing Values!\n")

    # Selecting required columns only
    print("-"*80)
    print("Columns : ")
    print(df.columns.tolist())
    print("-"*80)

    print("Dropping unneccessary columns : \n")

    print(f"Columns before dropping columns : \n{df.columns.tolist()}\n")
    df = df.drop(columns = ['title', 'subject', 'date'])
    print(f"Columns after dropping columns : \n{df.columns.tolist()}\n")

    print("-"*80)
    print("Preprocessing done successfully!")
    print("-"*80)

    return df

#########################################################################################
#   Function Name : FeatureExtraction
#   Description   : It is used to perform Feature Extraction
#   Input         : Dataframe
#   Output        : None
#   Date          : 03/05/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def FeatureExtraction(df) :
    Vectorizer = TfidfVectorizer(stop_words = 'english')
    X = Vectorizer.fit_transform(df['text'])

    Y = df['Label'].values

    print("Shape of extracted features : ",X.shape)
    print("Feature extraction completed successfully!")

    return X,Y

#########################################################################################
#   Function Name : TrainTestSplit
#   Description   : It is used to split data into training and testing
#   Input         : Dataframe
#   Output        : X_train,X_test,Y_train,Y_test
#   Date          : 03/05/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def TrainTestSplit(X,Y) :
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2)

    print("Training and Testing data aplitted successfully!")

    return X_train,X_test,Y_train,Y_test

#########################################################################################
#   Function Name : TrainIndividualModel
#   Description   : It is used to split data into training and testing
#   Input         : X_train,Y_train
#   Output        : Model_LR,Model_DT
#   Date          : 03/05/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def TrainIndividualModel(X_train,Y_train) :
    Model_LR = LogisticRegression(max_iter=5000)
    Model_DT = DecisionTreeClassifier(random_state= 42)

    Model_LR.fit(X_train,Y_train)
    Model_DT.fit(X_train,Y_train)

    print("Logistic Regression Model trained successfully!")
    print("Decision Tree Classifier Model trained successfully!")

    return Model_LR,Model_DT

#########################################################################################
#   Function Name : Voting
#   Description   : It is used to perform hard and soft voting
#   Input         : Model_LR,Model_DT
#   Output        : Hard_Model, Soft_Model
#   Date          : 03/05/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def Voting(Model_LR,Model_DT) :
    Hard_Model = VotingClassifier(
                                    estimators= [
                                        ('lr',Model_LR),
                                        ('dt',Model_DT)
                                    ],
                                    voting= 'hard'
                                )
    
    print("Hard Voting done successfully!")
    
    Soft_Model = VotingClassifier(
                                    estimators= [
                                        ('lr',Model_LR),
                                        ('dt',Model_DT)
                                    ],
                                    voting= 'soft'
                                )
    
    print("Soft Voting done successfully!")
    
    return Hard_Model, Soft_Model  

#########################################################################################
#   Function Name : ModelTrainTest
#   Description   : It is used to train and test models
#   Input         : Hard_Model, Soft_Model
#   Output        : Pred_Hard, Pred_Soft
#   Date          : 03/05/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def ModelTrainTest(Hard_Model, Soft_Model, X_train,X_test, Y_train) :
    Hard_Model.fit(X_train, Y_train)
    Soft_Model.fit(X_train, Y_train)

    print("Model trained successfully!")

    Pred_Hard = Hard_Model.predict(X_test)
    Pred_Soft = Soft_Model.predict(X_test)

    print("Model tested successfully!")

    return Pred_Hard, Pred_Soft

#########################################################################################
#   Function Name : ModelEvaluation
#   Description   : It is used to train and test models
#   Input         : Pred_Hard, Pred_Soft, Y_test
#   Output        : Nothing
#   Date          : 03/05/2026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def ModelEvaluation(Pred_Hard, Pred_Soft, Y_test) :
    print(f"Hard Voting Accuracy : {accuracy_score(Pred_Hard, Y_test)}")
    print(f"Soft Voting Accuracy : {accuracy_score(Pred_Soft, Y_test)}")

    # Confusion Matrix Display
    print("-"*80)
    print("\nConfusion Matrix Display : ")

    # for Hard Voting
    cm1 = confusion_matrix(Y_test,Pred_Hard)
    Display = ConfusionMatrixDisplay(confusion_matrix= cm1, display_labels=["0 : Fake", "1 : Real"])
    Display.plot(cmap= "Greens")
    plt.title("Confusion Matrix for Hard Voting")
    plt.show()
    print("Confusion Matrix for Hard Voting displayed successfully!")

    # for Soft Voting
    cm2 = confusion_matrix(Y_test,Pred_Soft)
    Display = ConfusionMatrixDisplay(confusion_matrix= cm2, display_labels=["0 : Fake", "1 : Real"])
    Display.plot(cmap= "Blues")
    plt.title("Confusion Matrix for Soft Voting")
    plt.show()
    print("Confusion Matrix for Soft Voting displayed successfully!")

#########################################################################################
#   Function Name : main
#   Description   : Entry-point funtion
#   Input         : None
#   Output        : None
#   Date          : 03/05/026
#   Author        : Shreya Pramod Pasalkar
#########################################################################################
def main() :
    # Step 1 : Load Dataset
    DisplayStart("Step 1 : Load Dataset")
    df_fake, df_true = LoadDataset()
    DisplayEnd()

    # Step 2 : Create Single Dataframe
    DisplayStart("Step 2 : Create Single Dataframe")
    df = CreateSingleDF(df_fake, df_true)
    DisplayEnd()

    # Step 3 : Exploratory Data Analysis
    DisplayStart("Step 3 : Exploratory Data Analysis")
    EDA(df)
    DisplayEnd()

    # Step 4 : Data Preprocessing
    DisplayStart("Step 4 : Data Preprocessing")
    DataPreprocessing(df)
    DisplayEnd()

    # Step 5 : Feature Extraction
    DisplayStart("Step 5 : Feature Extraction")
    X,Y = FeatureExtraction(df)
    DisplayEnd()

    # Step 6 : Train Test Split
    DisplayStart("Step 6 : Train Test Split")
    X_train,X_test,Y_train,Y_test = TrainTestSplit(X,Y)
    DisplayEnd()

    # Step 7 : Training Individual Models
    DisplayStart("Step 7 : Training Individual Models")
    Model_LR,Model_DT = TrainIndividualModel(X_train,Y_train)
    DisplayEnd()

    # Step 8 : Hard and Soft Voting
    DisplayStart("Step 8 : Hard and Soft Voting")
    Hard_Model, Soft_Model = Voting(Model_LR,Model_DT)
    DisplayEnd()

    # Step 9 : Model Training and Testing
    DisplayStart("Step 9 : Model Training and Testing")
    Pred_Hard, Pred_Soft = ModelTrainTest(Hard_Model, Soft_Model, X_train,X_test, Y_train)
    DisplayEnd()

    # Step 10 : Model Evaluation
    DisplayStart("Step 10 : Model Evaluation")
    ModelEvaluation(Pred_Hard, Pred_Soft, Y_test)
    DisplayEnd()

    DisplayStart("THANK YOU FOR USING OUR APPLICATION!!!")

#########################################################################################
#   Starter
#########################################################################################
if __name__ == "__main__" :
    main()