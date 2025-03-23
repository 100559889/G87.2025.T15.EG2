from datetime import datetime, timezone
import hashlib
import json

class AccountDeposit:
    # Class representing the information required for depositing money into an account

    def __init__(self, to_iban: str, deposit_amount: float):
        self.__alg = "SHA-256"
        self.__type = "DEPOSIT"
        self.__to_iban = to_iban
        self.__deposit_amount = deposit_amount
        justnow = datetime.now(timezone.utc)
        self.__deposit_date = datetime.timestamp(justnow)

    def to_json(self):
        """returns the object data in json format."""
        return {
            "alg": self.__alg,
            "type": self.__type,
            "to_iban": self.__to_iban,
            "deposit_amount": self.__deposit_amount,
            "deposit_date": self.__deposit_date,
            "deposit_signature": self.deposit_signature
        }

    def __signature_string(self):
        """Composes the string to be used for generating the key for the date."""
        return f'{{"alg":"{self.__alg}","typ":"{self.__type}","iban":"{self.__to_iban}","amount":{self.__deposit_amount},"deposit_date":{self.__deposit_date}}}'

    @property
    def to_iban(self):
        """Property that represents the product_id of the patient"""
        return self.__to_iban

    @to_iban.setter
    def to_iban(self, value):
        self.__to_iban = value

    @property
    def deposit_amount(self):
        """Property that represents the order_id"""
        return self.__deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, value):
        self.__deposit_amount = value

    @property
    def deposit_date(self):
        """Property that represents the phone number of the client"""
        return self.__deposit_date

    @deposit_date.setter
    def deposit_date(self, value):
        self.__deposit_date = value

    @property
    def deposit_signature(self):
        """Returns the sha256 signature of the date"""
        return hashlib.sha256(self.__signature_string().encode()).hexdigest()

    # Method to validate that the IBAN is a valid Spanish IBAN
    @staticmethod
    def validate_iban(iban: str):
        if not iban.startswith('ES'):
            return False
        if len(iban) != 24:
            return False
        if not iban[2:].isdigit():
            return False
        return True

    # Method to validate the deposit amount
    @staticmethod
    def validate_amount(amount: float):
        if amount <= 0:
            return False
        if not isinstance(amount, float):
            return False
        if len(str(amount).split('.')[1]) > 2:
            return False
        return True

    # Handles the deposit into account request
    @staticmethod
    def deposit_into_account(input_file: str):
        try:
            # Read the input file
            with open(input_file, 'r') as file:
                data = json.load(file)

            # Validate the input data
            if "IBAN" not in data or "AMOUNT" not in data:
                raise Exception("Invalid JSON structure")

            iban = data["IBAN"]
            amount_str = data["AMOUNT"]

            # Validate IBAN
            if not AccountDeposit.validate_iban(iban):
                raise Exception("Invalid IBAN")

            # Validate amount
            if not amount_str.startswith("EUR "):
                raise Exception("Invalid currency format")
            amount = float(amount_str[4:])
            if not AccountDeposit.validate_amount(amount):
                raise Exception("Invalid amount")

            # Create AccountDeposit object
            deposit = AccountDeposit(iban, amount)

            # Generate deposit signature
            deposit_signature = deposit.deposit_signature

            # Save deposit data to JSON file
            with open("deposits.json", "a") as file:
                file.write(json.dumps(deposit.to_json()) + "\n")

            return deposit_signature

        except FileNotFoundError:
            raise Exception("File not found")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON format")
        except Exception as e:
            raise Exception(f"Error processing deposit: {str(e)}")


def main():
    try:
        deposit_signature = AccountDeposit.deposit_into_account("input_deposit.json")
        print(f"Deposit successful! Deposit signature: {deposit_signature}")
    except Exception as e:
        print(f"Deposit failed: {str(e)}")

if __name__ == "__main__":
    main()