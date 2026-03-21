import numpy as np

def manual_input():
    try:
        data = input("👉 Enter numbers (space-separated): ").strip()
        if not data:
            print("❌ No input provided.")
            return None

        arr = np.array(list(map(float, data.split())))
        return arr

    except ValueError:
        print("❌ Invalid input. Example: 10 20 30")
        return None


def csv_input():
    try:
        file_name = input("📂 Enter CSV file name (with .csv): ").strip()
        data = np.loadtxt(file_name, delimiter=',')

        # Flatten if it's multi-dimensional
        return data.flatten()

    except Exception as e:
        print("❌ Error reading file:", e)
        return None


def analyze(data):
    print("\n📊 --- Analysis ---")
    print(f"Count   : {len(data)}")
    print(f"Mean    : {np.mean(data):.2f}")
    print(f"Median  : {np.median(data):.2f}")
    print(f"Std Dev : {np.std(data):.2f}")
    print(f"Variance: {np.var(data):.2f}")
    print(f"Min     : {np.min(data)}")
    print(f"Max     : {np.max(data)}")


def correlation():
    print("\n🔗 Correlation Between Two Datasets")

    data1 = manual_input()
    if data1 is None:
        return

    data2 = manual_input()
    if data2 is None:
        return

    if len(data1) != len(data2):
        print("❌ Both datasets must have same length.")
        return

    corr_matrix = np.corrcoef(data1, data2)

    print("\n📈 Correlation Matrix:")
    print(corr_matrix)
    print(f"Correlation Value: {corr_matrix[0][1]:.2f}")


def main():
    while True:
        print("\n===== NumPy Data Toolkit =====")
        print("1. Manual Input Analysis")
        print("2. CSV File Analysis")
        print("3. Correlation Between Two Datasets")
        print("4. Exit")

        choice = input("👉 Choose option (1-4): ").strip()

        if choice == '1':
            data = manual_input()
            if data is not None:
                analyze(data)

        elif choice == '2':
            data = csv_input()
            if data is not None:
                analyze(data)

        elif choice == '3':
            correlation()

        elif choice == '4':
            print("👋 Exiting program.")
            break

        else:
            print("❌ Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
