from app.exceptions import ConflictException


class InvalidSalesmanException(ConflictException):
    def __init__(self, msg: str = 'Salesman data is invalid or empty'):
        super().__init__(msg=msg)
