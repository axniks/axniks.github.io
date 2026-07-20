from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

WHATSAPP_URL = (
    "https://api.whatsapp.com/send?text="
    "Hi%20Ratio%2C%20I%20need%20help%20with%20an%20employment%20issue."
)


@app.context_processor
def inject_globals() -> dict:
    return {
        "year": datetime.utcnow().year,
        "whatsapp_url": WHATSAPP_URL,
    }


@app.get("/")
@app.get("/index.html")
def home():
    return render_template(
        "index.html",
        title="EmployerHub | Employment guidance on WhatsApp",
        description="EmployerHub helps small businesses handle employment issues in minutes, powered by Ratio AI.",
        active_page="home",
    )


@app.get("/service-partner")
@app.get("/service-partner.html")
def service_partner():
    return render_template(
        "service_partner.html",
        title="Service Partner Page | EmployerHub",
        description="Service partner page for organisations that want to offer EmployerHub, powered by Ratio.",
        active_page="service_partner",
    )


@app.get("/solicitor-partner")
@app.get("/solicitor-partner.html")
def solicitor_partner():
    return render_template(
        "solicitor_partner.html",
        title="Solicitor Partnerships | EmployerHub",
        description="Partner with EmployerHub and receive qualified employment-risk leads from Ratio triage.",
        active_page="solicitor_partner",
    )


@app.get("/investors")
@app.get("/investors.html")
def investors():
    return render_template(
        "investors.html",
        title="EmployerHub and Ratio | Axniks",
        description="EmployerHub is the customer-facing service powered by Ratio, Axniks' intelligence layer for employment risk triage.",
        active_page="investors",
    )


@app.get("/privacy")
@app.get("/privacy.html")
def privacy():
    return render_template(
        "privacy.html",
        title="Privacy Policy | Axniks Ltd",
        description="Privacy Policy for Axniks Ltd and Ratio.",
        active_page="privacy",
    )


if __name__ == "__main__":
    app.run(debug=True)
