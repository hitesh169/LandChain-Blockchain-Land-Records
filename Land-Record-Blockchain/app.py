
from flask import Flask, render_template, request, redirect, url_for, flash
from blockchain import LandBlockchain

app = Flask(__name__)
app.secret_key = "land-record-mini-project-key"

blockchain = LandBlockchain()


def get_land_records():
    records = {}

    for block in blockchain.chain:
        land_id = block["land_id"]

        if land_id == "GENESIS":
            continue

        if block["action"] == "REGISTER":
            records[land_id] = {
                "land_id": land_id,
                "location": block["details"]["location"],
                "area": block["details"]["area_sq_meters"],
                "owner": block["details"]["owner"]
            }

        elif block["action"] == "TRANSFER" and land_id in records:
            records[land_id]["owner"] = block["details"]["new_owner"]

    return records


def get_ownership_history(land_id):
    history = []

    for block in blockchain.chain:
        if block["land_id"] != land_id:
            continue

        if block["action"] == "REGISTER":
            history.append({
                "action": "Land Registered",
                "owner": block["details"]["owner"],
                "timestamp": block["timestamp"],
                "hash": block["hash"]
            })

        elif block["action"] == "TRANSFER":
            history.append({
                "action": "Ownership Transferred",
                "owner": block["details"]["new_owner"],
                "timestamp": block["timestamp"],
                "hash": block["hash"]
            })

    return history


@app.route("/")
def index():
    return render_template(
        "index.html",
        lands=get_land_records(),
        chain=blockchain.chain,
        valid=blockchain.verify_chain()
    )


@app.route("/register", methods=["POST"])
def register():
    land_id = request.form.get("land_id", "").strip()
    location = request.form.get("location", "").strip()
    owner = request.form.get("owner", "").strip()
    area = request.form.get("area", "").strip()

    if not all([land_id, location, owner, area]):
        flash("Please fill in all fields.", "error")
        return redirect(url_for("index"))

    if not land_id.isalnum() or len(land_id) > 30:
        flash("Land ID must contain only letters and numbers.", "error")
        return redirect(url_for("index"))

    try:
        area_value = float(area)
        if not 0 < area_value <= 1_000_000_000:
            raise ValueError
    except ValueError:
        flash("Enter a valid positive land area.", "error")
        return redirect(url_for("index"))

    records = get_land_records()

    if land_id in records:
        flash("This Land ID is already registered.", "error")
        return redirect(url_for("index"))

    blockchain.add_record(
        land_id,
        "REGISTER",
        {
            "location": location,
            "area_sq_meters": area_value,
            "owner": owner
        }
    )

    flash("Land registered successfully!", "success")
    return redirect(url_for("index"))


@app.route("/transfer", methods=["POST"])
def transfer():
    land_id = request.form.get("land_id", "").strip()
    current_owner = request.form.get("current_owner", "").strip()
    new_owner = request.form.get("new_owner", "").strip()

    records = get_land_records()
    land = records.get(land_id)

    if not land:
        flash("Land record not found.", "error")
    elif land["owner"] != current_owner:
        flash("Current owner does not match the registered owner.", "error")
    elif not new_owner:
        flash("Enter the new owner's name.", "error")
    elif new_owner == current_owner:
        flash("The new owner must be different.", "error")
    else:
        blockchain.add_record(
            land_id,
            "TRANSFER",
            {
                "old_owner": current_owner,
                "new_owner": new_owner
            }
        )
        flash("Ownership transfer recorded!", "success")

    return redirect(url_for("index"))


@app.route("/history/<land_id>")
def history(land_id):
    records = get_land_records()
    land = records.get(land_id)

    if not land:
        flash("Land record not found.", "error")
        return redirect(url_for("index"))

    return render_template(
        "history.html",
        land=land,
        history=get_ownership_history(land_id)
    )


@app.route("/verify")
def verify():
    is_valid = blockchain.verify_chain()

    return render_template(
        "verify.html",
        valid=is_valid,
        block_count=len(blockchain.chain),
        chain=blockchain.chain
    )


if __name__ == "__main__":
    app.run(debug=True)
