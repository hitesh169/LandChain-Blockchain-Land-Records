
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone


class LandBlockchain:
    def __init__(self, filename="blockchain_data.json"):
        self.filename = Path(filename)

        if self.filename.exists():
            self.chain = json.loads(
                self.filename.read_text(encoding="utf-8")
            )

            if not self.verify_chain():
                raise ValueError("Blockchain integrity check failed!")

        else:
            self.chain = []
            self.create_block(
                index=0,
                land_id="GENESIS",
                action="GENESIS",
                details={
                    "message": "Land Record Blockchain initialized"
                },
                previous_hash="0"
            )

    @staticmethod
    def calculate_hash(block):
        encoded = json.dumps(
            block, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")

        return hashlib.sha256(encoded).hexdigest()

    def save_chain(self):
        self.filename.write_text(
            json.dumps(self.chain, indent=4),
            encoding="utf-8"
        )

    def create_block(
        self, index, land_id, action, details, previous_hash
    ):
        block = {
            "index": index,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "land_id": land_id,
            "action": action,
            "details": details,
            "previous_hash": previous_hash
        }

        block["hash"] = self.calculate_hash(block)
        self.chain.append(block)
        self.save_chain()

        return block

    def add_record(self, land_id, action, details):
        previous_block = self.chain[-1]

        return self.create_block(
            index=len(self.chain),
            land_id=land_id,
            action=action,
            details=details,
            previous_hash=previous_block["hash"]
        )

    def verify_chain(self):
        if not self.chain:
            return False

        for i, block in enumerate(self.chain):
            original_data = {
                key: value
                for key, value in block.items()
                if key != "hash"
            }

            if block["hash"] != self.calculate_hash(original_data):
                return False

            if i == 0:
                if block["previous_hash"] != "0":
                    return False
                if block["action"] != "GENESIS":
                    return False
            else:
                if block["index"] != i:
                    return False

                if block["previous_hash"] != self.chain[i - 1]["hash"]:
                    return False

        return True
