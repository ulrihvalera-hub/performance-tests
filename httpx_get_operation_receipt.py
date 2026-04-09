import time

import httpx

body = {

    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users",json=body)
create_user_response_json = create_user_response.json()

open_debit_card_account_pyload = {
    "userId" : create_user_response_json["user"]["id"]
}

create_credit_account_response = httpx.post(
    "POST /api/v1/accounts/open-credit-card-account",json=open_debit_card_account_pyload
)
create_credit_account_response_data = create_credit_account_response.json()

make_purchase_operation = {
  "status": "IN PROGRESS",
  "amount": 77.99,
  "cardId": create_credit_account_response_data["account"]["cards"][0]["id"],
  "accountId": create_credit_account_response_data["account"]["id"],
  "category": "TAXI"
}
make_purchase_operation_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-purchase-operation",json=make_purchase_operation
)
make_purchase_operation_response_data = make_purchase_operation_response.json()

operation_recept_response = httpx.get(
    "http://localhost:8003/api/v1/operations/operation-receipt",
    json=make_purchase_operation_response_data["operation"]["id"]
)
operation_recept_response_data = operation_recept_response.json()

print(operation_recept_response_data)
print(operation_recept_response.status_code)