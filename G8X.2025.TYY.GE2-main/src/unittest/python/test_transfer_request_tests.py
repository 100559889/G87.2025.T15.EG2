"""Unit tests for TransferRequest class"""
import os
import sys
import unittest

# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append(project_root)

from uc3m_money.transfer_request import TransferRequest


class TestTransferRequest(unittest.TestCase):
    """Test cases for TransferRequest class"""

    def test_transfer_requests(self):
        """Method to run all test cases with logging"""
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
                "valid": True
            },
            # TC2 - Transfer with minimums (BV)
            {
                "id": "TC2",
                "description": "Transfer with minimums",
                "input": {
                    "from_iban": "ES6721000418450200051339",
                    "to_iban": "ES0621000418450200051348",
                    "concept": "12 chars ok",
                    "type": "ORDINARY",
                    "date": "05/03/2025",
                    "amount": 10.00
                },
                "valid": True
            },
            # TC3 - Transfer with maximums (BV)
            {
                "id": "TC3",
                "description": "Transfer with maximums",
                "input": {
                    "from_iban": "ES6721000418450200051339",
                    "to_iban": "ES0621000418450200051348",
                    "concept": "This is exactly thirty chars",
                    "type": "ORDINARY",
                    "date": "31/12/2050",
                    "amount": 10000.00
                },
                "valid": True
            },
            # TC4 - IBAN too short (EC & BV)
            {
                "id": "TC4",
                "description": "IBAN too short",
                "input": {
                    "from_iban": "ES672100041845020005133",
                    "to_iban": "ES0621000418450200051348",
                    "concept": "Pizza Night Food",
                    "type": "ORDINARY",
                    "date": "25/03/2025",
                    "amount": 15.75
                },
                "valid": False
            },
            # TC5 - IBAN too long (EC & BV)
            {
                "id": "TC5",
                "description": "IBAN too long",
                "input": {
                    "from_iban": "ES67210004184502000513392",
                    "to_iban": "ES0621000418450200051348",
                    "concept": "Pizza Night Food",
                    "type": "ORDINARY",
                    "date": "25/03/2025",
                    "amount": 15.75
                },
                "valid": False
            },
            # TC6 - Wrong country code (EC)
            {
                "id": "TC6",
                "description": "Wrong country code",
                "input": {
                    "from_iban": "NL6721000418450200051339",
                    "to_iban": "ES0621000418450200051348",
                    "concept": "Pizza Night Food",
                    "type": "ORDINARY",
                    "date": "25/03/2025",
                    "amount": 15.75
                },
                "valid": False
            },
            # TC7 - Non-numeric characters in IBAN (EC)
            {
                "id": "TC7",
                "description": "Non numeric characters in IBAN",
                "input": {
                    "from_iban": "ES672100GB£!450200051339",
                    "to_iban": "ES0621000418450200051348",
                    "concept": "Pizza Night Food",
                    "type": "ORDINARY",
                    "date": "25/03/2025",
                    "amount": 15.75
                },
                "valid": False
            },
            # TC8 - One word concept (EC)
            {
                "id": "TC8",
                "description": "One word concept",
                "input": {
                    "from_iban": "ES6721000418450200051339",
                    "to_iban": "ES0621000418450200051348",
                    "concept": "PizzaNight",
                    "type": "ORDINARY",
                    "date": "25/03/2025",
                    "amount": 15.75
                },
                "valid": False
            },
            # TC9 - Words not separated by a space in concept (EC)
            {
                "id": "TC9",
                "description": "Words not separated by a space",
                "input": {
                    "from_iban": "ES6721000418450200051339",
                    "to_iban": "ES0621000418450200051348",
                    "concept": "Loan-Mates",
                    "type": "ORDINARY",
                    "date": "25/03/2025",
                    "amount": 15.75
                },
                "valid": False
            },
            # TC10 - Invalid concept length - too short (EC & BV)
            {
                "id": "TC10",
                "description": "Concept too short",
                "input": {
                    "from_iban": "ES6721000418450200051339",
                    "to_iban": "ES0621000418450200051348",
                    "concept": "Short",
                    "type": "ORDINARY",
                    "date": "25/03/2025",
                    "amount": 15.75
                },
                "valid": False
            },
            # TC11 - Invalid concept length - too long (EC & BV)
            {
                "id": "TC11",
                "description": "Concept too long",
                "input": {
                    "from_iban": "ES6721000418450200051339",
                    "to_iban": "ES0621000418450200051348",
                    "concept": "This concept is way too long to be accepted",
                    "type": "ORDINARY",
                    "date": "25/03/2025",
                    "amount": 15.75
                },
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
                    "type": "SPEEDY",
                    "date": "25/03/2025",
                    "amount": 15.75
                },
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
                    "date": "25th-March-2025",
                    "amount": 15.75
                },
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
                    "date": "03/25/2025",
                    "amount": 15.75
                },
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
                    "date": "01/01/2020",
                    "amount": 15.75
                },
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
                    "date": "01/01/2051",
                    "amount": 15.75
                },
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
                    "amount": 9.99
                },
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
                    "amount": 10000.01
                },
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
                    "amount": "Fifty Quid"
                },
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
                    "amount": 15.755
                },
                "valid": False
            }
        ]

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


if __name__ == '__main__':
    unittest.main()