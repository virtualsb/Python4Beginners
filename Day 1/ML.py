# # import data
# # clean the data
# # split the data into training/test
# # create the model
# # train the model
# # make prediction
# # evaluate and improve
#
#
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
#
# music_data = pd.read_csv('dataset/music.csv')
# print(music_data)
#
# X = music_data.drop(columns=['genre'])
# Y = music_data['genre']
#
# model = DecisionTreeClassifier()
#
# model.fit(X,Y)
#
# prediction = model.predict([[21,1]])
# print(prediction)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Import data
# Use raw string or forward slashes to avoid escape sequence issues
data_path = r'dataset\music.csv' # or use r'day1\dataset\music.csv'
music_data = pd.read_csv(data_path)

# 2. Clean the data
# Example: Drop rows with missing values (customize as needed)
music_data = music_data.dropna()

# 3. Split the data into training and test sets
# Assuming 'genre' is the target column
X = music_data.drop('genre', axis=1)
y = music_data['genre']

# Use stratified sampling to maintain class distribution
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y
)

# 4. Create the model
model = RandomForestClassifier(random_state=1)

# 5. Train the model
model.fit(X_train, y_train)

# 6. Make predictions
predictions = model.predict(X_test)

# 7. Evaluate the model
print("Accuracy:", accuracy_score(y_test, predictions))
print("Classification Report:\n", classification_report(y_test, predictions, zero_division=0))

# 8. Make a prediction based on user input
try:
    age_input = int(input("Enter age: "))
    gender_input = int(input("Enter gender (0 for female, 1 for male): "))

    input_df = pd.DataFrame([[age_input, gender_input]], columns=X.columns)

    predicted_genre = model.predict(input_df)[0]
    print(f"Predicted genre for a {age_input}-year-old (gender={gender_input}): {predicted_genre}")
except ValueError:
    print("Invalid input. Please enter numeric values for age and gender.")