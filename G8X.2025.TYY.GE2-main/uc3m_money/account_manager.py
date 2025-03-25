"""Module for managing accounts"""
import json
from datetime import datetime, timezone

class AccountManager:
    """Class for providing the methods for managing the accounts"""

    def __init__(self):
        pass

    @staticmethod
    def validate_iban(iban: str):
        """Returns True if the IBAN received is a valid Spanish IBAN, or False otherwise."""
        if not iban.startswith('ES'):
            return False
        if len(iban) != 24:
            return False
        if not iban[2:].isdigit():
            return False
        return True

    @staticmethod
    def calculate_balance(iban: str):
        try:
            # Validate the IBAN
            if not AccountManager.validate_iban(iban):
                raise Exception("The JSON data does not have valid values")

            # Load transactions from the JSON file
            with open("transactions.json", "r") as file:
                transactions = json.load(file)

            # Validate JSON structure
            if not all(isinstance(t, dict) and "IBAN" in t and "amount" in t for t in transactions):
                raise Exception("The JSON does not have the expected structure")

            # Calculate the balance
            balance = 0.0
            for transaction in transactions:
                if transaction["IBAN"] == iban:
                    try:
                        amount = float(transaction["amount"].replace(",", "."))
                        balance += amount
                    except ValueError:
                        raise Exception("The JSON data does not have valid values")

            # Save the balance data to a JSON file
            balance_data = {
                "IBAN": iban,
                "date": datetime.now(timezone.utc).timestamp(),
                "balance": balance
            }
            with open("balance.json", "a") as file:
                file.write(json.dumps(balance_data) + "\n")

            return True

        except FileNotFoundError:
            raise Exception("The data file is not found")
        except json.JSONDecodeError:
            raise Exception("The file is not in JSON format")
        except Exception as e:
            if str(e) not in ["The JSON does not have the expected structure",
                            "The JSON data does not have valid values"]:
                raise Exception(f"Error processing data: {str(e)}")
            raise

def main():
    manager = AccountManager()
    try:
        success = manager.calculate_balance("ES6721000418450200051339")
        if success:
            print("Balance calculated and saved successfully!")
    except Exception as e:
        print(f"Balance calculation failed: {str(e)}")

if __name__ == "__main__":
    main()