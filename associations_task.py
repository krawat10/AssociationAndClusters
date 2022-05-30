import json
from collections import defaultdict
from Models.Grade import Grade
from Models.Transaction import Transaction
from utils import flatten


def associations_task():
    grouped_grades = defaultdict(list)
    transactions = []
    products_with_min_support = []
    min_support = 0.015

    with open('data_appl.json') as read_file:
        data = json.load(read_file)

    grades = [Grade(row['gradingCompany'], row['date'], row['newGrade']) for row in data]

    # Group grades by date
    for obj in grades:
        grouped_grades[obj.date].append(obj)

    for date in grouped_grades.keys():
        indexes = [grade.idx for grade in grouped_grades[date]]  # Get indexes for a given day
        transactions.append(Transaction(indexes))  # Create Transaction for a given day

    # Get max amount of items in one transaction
    max_set = max([transaction.items_number() for transaction in transactions])

    for current_set_len in range(1, max_set + 1):
        # Get all available combinations of n-elements sets
        combinations = flatten([transaction.get_combinations(current_set_len) for transaction in transactions])
        unique_combinations = [list(x) for x in set(tuple(x) for x in combinations)]

        for unique_combination in unique_combinations:
            transaction_count = len([transaction for transaction in transactions if transaction.contain(unique_combination)])

            # If combination has min support
            if transaction_count / len(transactions) >= min_support:
                products_with_min_support.append(unique_combination)

    for product_with_min_support in products_with_min_support:
        print(product_with_min_support)