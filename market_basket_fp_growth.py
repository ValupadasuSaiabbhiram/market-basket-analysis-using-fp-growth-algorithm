import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules

# Step 1: Load CSV file and prepare transactions list
def load_transactions_from_csv(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split by comma and strip whitespace
            transaction = [item.strip() for item in line.strip().split(',') if item]
            transactions.append(transaction)
    return transactions

# Step 2: Encode transactions
def encode_transactions(transactions):
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    return pd.DataFrame(te_ary, columns=te.columns_)

# Step 3: Run FP-Growth algorithm
def run_fp_growth(df, min_support=0.3):
    return fpgrowth(df, min_support=min_support, use_colnames=True)

# Step 4: Generate association rules
def generate_rules(frequent_itemsets, metric="confidence", min_threshold=0.6):
    return association_rules(frequent_itemsets, metric=metric, min_threshold=min_threshold)

# Main Execution
if __name__ == "__main__":
    csv_file = 'transactions.csv'
    transactions = load_transactions_from_csv(Assignment-1_Data.csv)
    
    print("Transactions:")
    for t in transactions:
        print(t)

    df = encode_transactions(transactions)
    
    print("\nOne-Hot Encoded DataFrame:")
    print(df)

    frequent_itemsets = run_fp_growth(df)
    print("\nFrequent Itemsets:")
    print(frequent_itemsets)

    rules = generate_rules(frequent_itemsets)
    rules = rules.sort_values(by="lift", ascending=False)

    print("\nAssociation Rules:")
    print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
