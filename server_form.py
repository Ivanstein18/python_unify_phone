from fastapi import FastAPI
from fastapi.responses import Response
from fastapi import Body, Form


app = FastAPI()


@app.post("/unify_phone_from_form")
def page(phone: str=Form(...)):

    phone_namber = phone

    phone_namber = list(phone_namber.strip())
    pn_modern = []

    for i in phone_namber:
        if i in '1234567890':
            pn_modern.append(i)

    if (pn_modern[0] == '7' or pn_modern[0] == '8') and pn_modern[1] == '9' and len(pn_modern) == 11:
        phone_n = f"8 ({''.join(pn_modern[1:4])}) {''.join(pn_modern[4:7])}-{''.join(pn_modern[7:9])}-{''.join(pn_modern[9:11])}"

    elif pn_modern[0] == '9' and len(pn_modern) == 10:
        phone_n = f"8 ({''.join(pn_modern[0:3])}) {''.join(pn_modern[3:6])}-{''.join(pn_modern[6:8])}-{''.join(pn_modern[8:10])}"

    else:
        phone_n = ''.join(pn_modern)

    return Response(phone_n, media_type= "text/html")