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
        # Validate inputs during initialization
        if not self.validate_iban(from_iban):
            raise ValueError("Invalid from_iban")
        if not self.validate_iban(to_iban):
            raise ValueError("Invalid to_iban")
        if not self.validate_concept(transfer_concept):
            raise ValueError("Invalid concept")
        if transfer_type not in ["ORDINARY", "URGENT", "IMMEDIATE"]:
            raise ValueError("Invalid transfer type")
        if not self.validate_date(transfer_date):
            raise ValueError("Invalid date")
        if not self.validate_amount(transfer_amount):
            raise ValueError("Invalid amount")

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
        if not isinstance(iban, str):
            return False
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
        if not isinstance(concept, str):
            return False
        if len(concept) < 10 or len(concept) > 30:
            return False
        if len(concept.split()) < 2:
            return False
        # Allow hyphenated words but not as word separators
        if any(char in concept for char in ['_', ',']):
            return False
        return True

    # Validating the date and time
    @staticmethod
    def validate_date(date_str: str):
        try:
            # Parse the input date
            date = datetime.strptime(date_str, "%d/%m/%Y")

            # Define the minimum and maximum allowed dates
            min_date = datetime.strptime("05/03/2025", "%d/%m/%Y")
            max_date = datetime.strptime("31/12/2050", "%d/%m/%Y")

            # Check if date is within the allowed range
            if date < min_date or date > max_date:
                return False

            return True
        except ValueError:
            return False

    # Validating the transfer amount
    @staticmethod
    def validate_amount(amount):
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            return False

        if amount < 10.00 or amount > 10000.00:
            return False

        # Check for exactly 2 decimal places
        if not isinstance(amount, float) or round(amount, 2) != amount:
            return False

        return True

    @property
    def from_iban(self):
        """Sender's iban"""
        return self.__from_iban

    @property
    def to_iban(self):
        """receiver's iban"""
        return self.__to_iban

    @property
    def transfer_type(self):
        """Property representing the type of transfer: REGULAR, IMMEDIATE or URGENT """
        return self.__transfer_type

    @property
    def transfer_amount(self):
        """Property representing the transfer amount"""
        return self.__transfer_amount

    @property
    def transfer_concept(self):
        """Property representing the transfer concept"""
        return self.__concept

    @property
    def transfer_date(self):
        """Property representing the transfer's date"""
        return self.__transfer_date

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
        # Create TransferRequest object (validation happens in __init__)
        transfer = TransferRequest(from_iban, transfer_type, to_iban, concept, date, amount)

        # Generate transfer code
        transfer_code = transfer.transfer_code

        # Save transfer data to JSON file
        with open("transfers.json", "a") as file:
            file.write(json.dumps(transfer.to_json()) + "\n")

        return transfer_code