import pandas as pd

def analyze_data(file_path):
    df = pd.read_csv(file_path)

    df.drop_duplicates(inplace=True)
    df.fillna(df.select_dtypes(include="number").mean(), inplace=True)

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(include="object").columns.tolist()

    analysis = {
        "summary_stats": df[numeric_cols].describe().to_dict(),
        "correlations": df[numeric_cols].corr().to_dict(),
        "top_values": {},
        "numeric_cols": numeric_cols,
        "categorical_cols": categorical_cols,
        "dataframe": df
    }

    for col in categorical_cols[:5]:
        analysis["top_values"][col] = df[col].value_counts().head(5).to_dict()

    return analysis