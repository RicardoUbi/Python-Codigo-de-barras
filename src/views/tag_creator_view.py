from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
    Responsabilty for interacting with HTTP
    '''
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        # body = http_request.body
        # product_code = body("product_code")

        # Logica de regra de negocios
        print(http_request)

        # Retorno de HTTP
        return HttpResponse(status_code=200, body={"hello": "world"})
