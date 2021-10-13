class InvalidGroupError(Exception):

    valid_codes: dict = {
        'valid_codes' : {
                "01": "Adm",
                "15": "Comercial",
                "30": "RH"
        }
    }

    def __init__(self, code) -> None:
        self.received_code = code

        self.message = {
            'valid_codes': self.valid_codes['valid_codes'],
            'received_code': self.received_code
        }

        super().__init__(self.message)
