"""MODULE: transfer_request. Contains the transfer request class"""
import hashlib
import json
from datetime import datetime, timezone

class TransferRequest:
    """Class representing a transfer request"""
    def __init__(self,
                 from_iban: str,
                 transfer_type: str,
                 to_iban: str,
                 transfer_concept: str,
                 transfer_date: str,
                 transfer_amount: float):
        self.__from_iban = from_iban
        self.__to_iban = to_iban
        self.__transfer_type = transfer_type
        self.__concept = transfer_concept
        self.__transfer_date = transfer_date
        self.__transfer_amount = transfer_amount
        justnow = datetime.now(timezone.utc)
        self.__time_stamp = datetime.timestamp(justnow)

    def __str__(self):
        return "Transfer:" + json.dumps(self.__dict__)

    def to_json(self):
        """Returns the object information in json format"""
        return {
            "from_iban": self.__from_iban,
            "to_iban": self.__to_iban,
            "transfer_type": self.__transfer_type,
            "transfer_amount": self.__transfer_amount,
            "transfer_concept": self.__concept,
            "transfer_date": self.__transfer_date,
            "time_stamp": self.__time_stamp,
            "transfer_code": self.transfer_code
        }


    # Validate that the IBAN is a valid Spanish IBAN
    @staticmethod
    def validate_iban(iban: str):
        if not iban.startswith('ES'):
            return False
        if len(iban) != 24:
            return False
        if not iban[2:].isdigit():
            return False
        return True

    # Concept validation
    @staticmethod
    def validate_concept(concept: str):
        if not concept or len(concept) < 10 or len(concept) > 30:
            return False
        if len(concept.split()) < 2:
            return False
        return True

    # Validating the date and time
    @staticmethod
    def validate_date(date_str: str):
        try:
            date = datetime.strptime(date_str, "%d/%m/%Y")
            if date.year < 2025 or date.year > 2050:
                return False
            if date < datetime.now():
                return False
            return True
        except ValueError:
            return False


    # Validating the transfer amount
    @staticmethod
    def validate_amount(amount: float):
        if amount < 10.00 or amount > 10000.00:
            return False
        if not isinstance(amount, float):
            return False
        if len(str(amount).split('.')[1]) > 2:
            return False
        return True


    @property
    def from_iban(self):
        """Sender's iban"""
        return self.__from_iban
    @from_iban.setter
    def from_iban(self, value):
        self.__from_iban = value

    @property
    def to_iban(self):
        """receiver's iban"""
        return self.__to_iban
    @to_iban.setter
    def to_iban(self, value):
        self.__to_iban = value

    @property
    def transfer_type(self):
        """Property representing the type of transfer: REGULAR, INMEDIATE or URGENT """
        return self.__transfer_type
    @transfer_type.setter
    def transfer_type(self, value):
        self.__transfer_type = value

    @property
    def transfer_amount(self):
        """Property respresenting the transfer amount"""
        return self.__transfer_amount
    @transfer_amount.setter
    def transfer_amount(self, value):
        self.__transfer_amount = value

    @property
    def transfer_concept(self):
        """Property representing the transfer concept"""
        return self.__concept
    @transfer_concept.setter
    def transfer_concept(self, value):
        self.__concept = value

    @property
    def transfer_date(self):
        """Property representing the transfer's date"""
        return self.__transfer_date
    @transfer_date.setter
    def transfer_date(self, value):
        self.__transfer_date = value

    @property
    def time_stamp(self):
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def transfer_code(self):
        """Returns the MD5 signature (transfer code)."""
        return hashlib.md5(str(self).encode()).hexdigest()


    # Handles the transfer request
    @staticmethod
    def transfer_request(from_iban: str, to_iban: str, concept: str, transfer_type: str, date: str, amount: float):

        # Validate inputs
        if not TransferRequest.validate_iban(from_iban):
            raise Exception("Invalid from_iban")
        if not TransferRequest.validate_iban(to_iban):
            raise Exception("Invalid to_iban")
        if not TransferRequest.validate_concept(concept):
            raise Exception("Invalid concept")
        if transfer_type not in ["ORDINARY", "URGENT", "IMMEDIATE"]:
            raise Exception("Invalid transfer type")
        if not TransferRequest.validate_date(date):
            raise Exception("Invalid date")
        if not TransferRequest.validate_amount(amount):
            raise Exception("Invalid amount")

        # Create TransferRequest object
        transfer = TransferRequest(from_iban, transfer_type, to_iban, concept, date, amount)

        # Generate transfer code
        transfer_code = transfer.transfer_code

        # Save transfer data to JSON file
        with open("transfers.json", "a") as file:
            file.write(json.dumps(transfer.to_json()) + "\n")

        return transfer_code


def main():
    try:
        # Example transfer request
        transfer_code = TransferRequest.transfer_request(
            from_iban="ES6721000418450200051339",
            to_iban="ES0621000418450200051348",
            concept="Pizza Night Food",
            transfer_type="ORDINARY",
            date="25/03/2025",
            amount=15.75
        )
        print(f"Transfer successful! Transfer code: {transfer_code}")
    except Exception as e:
        print(f"Transfer failed: {str(e)}")

if __name__ == "__main__":
    main()