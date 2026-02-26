import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.DataFrame({
    "Age":[25,45,35,50,23,52,40,60],
    "Cholesterol":[180,250,200,300,170,280,220,310],
    "BP":[120,140,130,150,115,160,135,170],
    "Disease":[0,1,0,1,0,1,0,1]
})

X = df[["Age","Cholesterol","BP"]]
y = df["Disease"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test,pred))