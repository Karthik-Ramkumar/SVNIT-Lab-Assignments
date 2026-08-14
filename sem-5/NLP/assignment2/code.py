import json

from greedy import greedy_segment
from dynamic import dynamic_segment


with open("text_segmentation_dataset.json", "r") as file:
    data = json.load(file)

word_counts = data["word_counts"]
test_cases = data["test_cases"]

vocabulary = set(word_counts.keys())


def edit_distance(actual, predicted):

    m = len(actual)
    n = len(predicted)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if actual[i - 1] == predicted[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )

    return dp[m][n]


greedy_correct = 0
dynamic_correct = 0

greedy_edit_total = 0
dynamic_edit_total = 0


# Create output files
greedy_file = open("greedy_results.txt", "w")
dynamic_file = open("dynamic_results.txt", "w")


for number, case in enumerate(test_cases, 1):

    text = case["input"]
    actual = case["ground_truth"].split()

    # Run Greedy
    greedy_result = greedy_segment(text, vocabulary)

    # Run Dynamic Programming
    dynamic_result = dynamic_segment(text, word_counts)

    # Accuracy
    if greedy_result == actual:
        greedy_correct += 1

    if dynamic_result == actual:
        dynamic_correct += 1

    # Edit distance
    greedy_edit_total += edit_distance(actual, greedy_result)
    dynamic_edit_total += edit_distance(actual, dynamic_result)

    # Save Greedy result
    greedy_file.write(f"Test Case {number}\n")
    greedy_file.write(f"Input:      {text}\n")
    greedy_file.write(f"Correct:    {' '.join(actual)}\n")
    greedy_file.write(f"Predicted:  {' '.join(greedy_result)}\n")
    greedy_file.write(
        f"Edit Distance: {edit_distance(actual, greedy_result)}\n"
    )
    greedy_file.write("-" * 60 + "\n")

    # Save Dynamic result
    dynamic_file.write(f"Test Case {number}\n")
    dynamic_file.write(f"Input:      {text}\n")
    dynamic_file.write(f"Correct:    {' '.join(actual)}\n")
    dynamic_file.write(f"Predicted:  {' '.join(dynamic_result)}\n")
    dynamic_file.write(
        f"Edit Distance: {edit_distance(actual, dynamic_result)}\n"
    )
    dynamic_file.write("-" * 60 + "\n")


greedy_file.close()
dynamic_file.close()


# Results
total_cases = len(test_cases)

greedy_accuracy = (greedy_correct / total_cases) * 100
dynamic_accuracy = (dynamic_correct / total_cases) * 100

greedy_avg_edit = greedy_edit_total / total_cases
dynamic_avg_edit = dynamic_edit_total / total_cases



print("\nGreedy Longest-Match:")
print("Accuracy:", round(greedy_accuracy, 2), "%")
print("Average Edit Distance:", round(greedy_avg_edit, 2))

print("\nDynamic Programming:")
print("Accuracy:", round(dynamic_accuracy, 2), "%")
print("Average Edit Distance:", round(dynamic_avg_edit, 2))

