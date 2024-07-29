import flask
import stripe

class Pagamento(object):
    def __init__(self, produtos, preco_total_produtos) -> None:
        self.produtos = produtos
        self.preco_total_produtos = preco_total_produtos

        stripe.api_key = "sk_test_51PhWh5Bh7PZmW4kqG6hAxJ1ZWf0XMfOnXxV6qfsXIWgVqe0PQDfSAxU4QMRFhnFLNae1dxn6VT6916YatLIY80gA00Kn840RyN"

    
    def Pagar(self):
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'brl',
                    'product_data': {
                        'name': self.produtos,
                    },
                    'unit_amount': int(self.preco_total_produtos * 100),  # em centavos
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url="https://sports-gear-hub.onrender.com/pagamento-efetuado-sucesso",
            cancel_url="https://sports-gear-hub.onrender.com/pagamento-cancelado",
        )

        return flask.redirect(session.url)



