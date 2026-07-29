from utils.loader import inventory_report, workforce

print("Inventory Columns:")
print(inventory_report.columns.tolist())

print("\nWorkforce Columns:")
print(workforce.columns.tolist())