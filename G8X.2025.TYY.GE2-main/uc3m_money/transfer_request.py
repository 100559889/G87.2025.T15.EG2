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
        """Property representing the type of transfer: REGULAR, IMMEDIATE or URGENT """
        return self.__transfer_type
    @transfer_type.setter
    def transfer_type(self, value):
        self.__transfer_type = value

    @property
    def transfer_amount(self):
        """Property representing the transfer amount"""
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

# Method to run all test cases
def run_tests():

    test_cases = [
        # TC1 - Valid transfer request (EC)
        {
            "id": "TC1",
            "description": "Valid transfer request",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "25/03/2025",
                "amount": 15.75
            },
            "expected": "Transfer code",
            "valid": True
        },
        # TC2 - Transfer with minimums (BV)
        {
            "id": "TC2",
            "description": "Transfer with minimums",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "05/03/2025",  # Minimum date
                "amount": 10.00  # Minimum amount
            },
            "expected": "Transfer code",
            "valid": True
        },
        # TC3 - Transfer with maximums (BV)
        {
            "id": "TC3",
            "description": "Transfer with maximums",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "31/12/2050",  # Maximum date
                "amount": 10000.00  # Maximum amount
            },
            "expected": "Transfer code",
            "valid": True
        },
        # TC4 - IBAN too short (EC & BV)
        {
            "id": "TC4",
            "description": "IBAN too short",
            "input": {
                "from_iban": "ES672100041845020005133",  # 23 chars
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "25/03/2025",
                "amount": 15.75
            },
            "expected": "Exception",
            "valid": False
        },
        # TC5 - IBAN too long (EC & BV)
        {
            "id": "TC5",
            "description": "IBAN too long",
            "input": {
                "from_iban": "ES67210004184502000513392",  # 25 chars
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "25/03/2025",
                "amount": 15.75
            },
            "expected": "Exception",
            "valid": False
        },
        # TC6 - Wrong country code (EC)
        {
            "id": "TC6",
            "description": "Wrong country code",
            "input": {
                "from_iban": "NL6721000418450200051339",  # NL instead of ES
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "25/03/2025",
                "amount": 15.75
            },
            "expected": "Exception",
            "valid": False
        },
        # TC7 - Non-numeric characters in IBAN (EC)
        {
            "id": "TC7",
            "description": "Non numeric characters in IBAN",
            "input": {
                "from_iban": "ES672100GB£!450200051339",  # Invalid chars
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "25/03/2025",
                "amount": 15.75
            },
            "expected": "Exception",
            "valid": False
        },
        # TC8 - One word concept (EC)
        {
            "id": "TC8",
            "description": "One word concept",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "PizzaNight",  # One word
                "type": "ORDINARY",
                "date": "25/03/2025",
                "amount": 15.75
            },
            "expected": "Exception",
            "valid": False
        },
        # TC9 - Words not separated by a space in concept (EC)
        {
            "id": "TC9",
            "description": "Words not separated by a space",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Loan-Mates",  # Hyphen instead of space
                "type": "ORDINARY",
                "date": "25/03/2025",
                "amount": 15.75
            },
            "expected": "Exception",
            "valid": False
        },
        # TC10 - Invalid concept length - too short (EC & BV)
        {
            "id": "TC10",
            "description": "Concept too short",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Mate Loan",  # 9 chars
                "type": "ORDINARY",
                "date": "25/03/2025",
                "amount": 15.75
            },
            "expected": "Exception",
            "valid": False
        },
        # TC11 - Invalid concept length - too long (EC & BV)
        {
            "id": "TC11",
            "description": "Concept too long",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "I asked my mates for some money tn",  # 31 chars
                "type": "ORDINARY",
                "date": "25/03/2025",
                "amount": 15.75
            },
            "expected": "Exception",
            "valid": False
        },
        # TC12 - Invalid type (EC)
        {
            "id": "TC12",
            "description": "Invalid transfer type",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "SPEEDY",  # Invalid type
                "date": "25/03/2025",
                "amount": 15.75
            },
            "expected": "Exception",
            "valid": False
        },
        # TC13 - Invalid date format (EC)
        {
            "id": "TC13",
            "description": "Invalid date format",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "25th-March-2025",  # Invalid format
                "amount": 15.75
            },
            "expected": "Exception",
            "valid": False
        },
        # TC14 - Invalid date (EC)
        {
            "id": "TC14",
            "description": "Invalid date",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "03/25/2025",  # MM/DD/YYYY format
                "amount": 15.75
            },
            "expected": "Exception",
            "valid": False
        },
        # TC15 - Past date (EC & BV)
        {
            "id": "TC15",
            "description": "Past date",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "04/03/2025",  # Past date
                "amount": 15.75
            },
            "expected": "Exception",
            "valid": False
        },
        # TC16 - Future date (EC & BV)
        {
            "id": "TC16",
            "description": "Date after 2050",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "01/01/2051",  # After 2050
                "amount": 15.75
            },
            "expected": "Exception",
            "valid": False
        },
        # TC17 - Below minimum amount (EC & BV)
        {
            "id": "TC17",
            "description": "Below minimum amount",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "25/03/2025",
                "amount": 9.99  # Below minimum
            },
            "expected": "Exception",
            "valid": False
        },
        # TC18 - Above maximum amount (EC & BV)
        {
            "id": "TC18",
            "description": "Above maximum amount",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "25/03/2025",
                "amount": 10000.01  # Above maximum
            },
            "expected": "Exception",
            "valid": False
        },
        # TC19 - Non float amount (EC)
        {
            "id": "TC19",
            "description": "Non float amount",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "25/03/2025",
                "amount": "Fifty Quid"  # Not a float
            },
            "expected": "Exception",
            "valid": False
        },
        # TC20 - More than two decimal places (EC)
        {
            "id": "TC20",
            "description": "More than two decimal places",
            "input": {
                "from_iban": "ES6721000418450200051339",
                "to_iban": "ES0621000418450200051348",
                "concept": "Pizza Night Food",
                "type": "ORDINARY",
                "date": "25/03/2025",
                "amount": 15.755  # Three decimal places
            },
            "expected": "Exception",
            "valid": False
        }
    ]

    # Run all test cases
    for test in test_cases:
        print(f"\nRunning test {test['id']}: {test['description']}")
        try:
            result = TransferRequest.transfer_request(
                from_iban=test["input"]["from_iban"],
                to_iban=test["input"]["to_iban"],
                concept=test["input"]["concept"],
                transfer_type=test["input"]["type"],
                date=test["input"]["date"],
                amount=test["input"]["amount"]
            )

            if test["valid"]:
                print(f"PASSED: Got transfer code {result}")
            else:
                print(f"FAILED: Expected exception but got transfer code {result}")
        except Exception as e:
            if test["valid"]:
                print(f"FAILED: Expected transfer code but got exception: {str(e)}")
            else:
                print(f"PASSED: Got expected exception: {str(e)}")


if __name__ == "__main__":
    run_tests()