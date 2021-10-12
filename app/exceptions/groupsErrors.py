class InvalidGroupError(Exception):

    valide_options: dict = {
        'valide_options' : {
                "01": "Adm",
                "15": "Comercial",
                "30": "RH"
        }
    }

    def __init__(self, code) -> None:
        self.received_code = code

        self.message = {
            'valide_options': self.valide_options['valide_options'],
            'received_code': self.received_code
        }

        super().__init__(self.message)
