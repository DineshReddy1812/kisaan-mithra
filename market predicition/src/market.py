import pandas as pd
import os
import joblib
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split, GridSearchCV

# ✅ Dataset file path
file_path = r"C:\Users\Gowtham37\cleaned_datasetof market analysis.xlsx"

# ✅ Check if file exists
if not os.path.exists(file_path):
    print(f"❌ Error: The file '{file_path}' was not found.")
    exit()

# ✅ Load dataset
df = pd.read_excel(file_path)

# ✅ Handle missing values
df.fillna(df.median(numeric_only=True), inplace=True)

# ✅ Convert categorical columns ("state" & "crop") to numerical values
df = pd.get_dummies(df, columns=["state", "crop"], drop_first=False)

# ✅ Define input features (X) and target variables (Y)
X = df.drop(columns=["costcultivation", "price"])
y_cost = df["costcultivation"]
y_price = df["price"]

# ✅ Split dataset
X_train, X_test, y_cost_train, y_cost_test = train_test_split(X, y_cost, test_size=0.2, random_state=42)
X_train, X_test, y_price_train, y_price_test = train_test_split(X, y_price, test_size=0.2, random_state=42)

# ✅ Define the Gradient Boosting Model
model = GradientBoostingRegressor()

# ✅ Hyperparameter tuning
param_grid = {
    "n_estimators": [100],  
    "learning_rate": [0.1],  
    "max_depth": [5]  
}

grid_search_cost = GridSearchCV(model, param_grid, cv=3, scoring="neg_mean_absolute_error", n_jobs=-1, verbose=1)
grid_search_price = GridSearchCV(model, param_grid, cv=3, scoring="neg_mean_absolute_error", n_jobs=-1, verbose=1)

# ✅ Train models
grid_search_cost.fit(X_train, y_cost_train)
grid_search_price.fit(X_train, y_price_train)

# ✅ Save models
os.makedirs("models", exist_ok=True)
joblib.dump(grid_search_cost.best_estimator_, "models/cost_model.pkl")
joblib.dump(grid_search_price.best_estimator_, "models/price_model.pkl")
print("\n✅ Models saved in the 'models/' directory")

# ✅ Get user input
state_input = input("\nEnter State: ").strip()
crop_input = input("Enter Crop: ").strip()

# ✅ Create a dataframe for prediction
user_input = pd.DataFrame(columns=X.columns, data=[[0] * len(X.columns)])

# ✅ Set categorical values
for col in X.columns:
    if col == f"state_{state_input}":
        user_input[col] = 1
    elif col == f"crop_{crop_input}":
        user_input[col] = 1

# ✅ Make predictions
cost_prediction = grid_search_cost.best_estimator_.predict(user_input)[0]
price_prediction = grid_search_price.best_estimator_.predict(user_input)[0]

# ✅ Display results
print("\n✅ Estimated Cost of Cultivation (INR):", round(cost_prediction, 2))
print("💰 Expected Earnings from Selling Yield (INR):", round(price_prediction, 2))