import unittest
from bencode_bdecode import bencode, bdecode, get_bytes


class TestBencodeBdecode(unittest.TestCase):
    def test_bencode(self):
        # str
        self.assertEqual(bencode(""), get_bytes("0:"))
        self.assertEqual(bencode("hello world!"), get_bytes("12:hello world!"))
        self.assertEqual(bencode("bencode"), get_bytes("7:bencode"))

        # int
        self.assertEqual(bencode(0), get_bytes("i0e"))
        self.assertEqual(bencode(42), get_bytes("i42e"))
        self.assertEqual(bencode(-42), get_bytes("i-42e"))

        # list
        self.assertEqual(bencode([]), get_bytes("le"))
        self.assertEqual(bencode(["bencode", -42]),
                         get_bytes("l7:bencodei-42ee"))

        # dict
        self.assertEqual(bencode({}), get_bytes("de"))
        self.assertEqual(bencode({"wiki": "bencode", "meaning": 42}),
                         get_bytes("d7:meaningi42e4:wiki7:bencodee"))

    def test_bdecode(self):
        self.assertIs(bdecode(""), True)


# Run the tests when the file is run directly
if __name__ == '__main__':
    unittest.main()
