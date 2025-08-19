sequenceDiagram
    actor User

    participant Cart
    participant paymentService
    participant Storage

    User ->> Cart : select products
    User ->> Cart : remove products
    Cart -->> User : recomend products
    
    Cart ->> paymentService : buy
    paymentService -->> User : proceed payment
    User ->> paymentService : pay
    Cart -x Storage : remove products
    
