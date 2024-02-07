from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.contrallers.tag_creator_contraller import TagCreateContraller

class TagCreatorView:
    '''
    Responsabilty for interacting with HTTP
    '''
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_contraller = TagCreateContraller()

        body = http_request.body
        product_code = body["product_code"]

        # Logica de regra de negocios
        formatted_response = tag_creator_contraller.create(product_code)

        # Retorno de HTTP
        return HttpResponse(status_code=200, body=formatted_response)
