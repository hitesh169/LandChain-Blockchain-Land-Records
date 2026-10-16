
import json
from pathlib import Path
from blockchain import LandBlockchain

TEST_FILE = Path("tamper_test_chain.json")

# Remove an old test file so the test starts fresh.
if TEST_FILE.exists():
    TEST_FILE.unlink()

# Build an independent test blockchain.
bc = LandBlockchain(str(TEST_FILE))

bc.add_record(
    "LAND999",
    "REGISTER",
    {
        "location": "Test Plot",
        "area_sq_meters": 100,
        "owner": "Rahul"
    }
)

print("Before tampering:", bc.verify_chain())

# Simulate someone changing a stored land record.
data = json.loads(TEST_FILE.read_text(encoding="utf-8"))
data[1]["details"]["owner"] = "Fake Owner"

TEST_FILE.write_text(
    json.dumps(data, indent=4),
    encoding="utf-8"
)

# Check the altered file using a fresh blockchain instance.
try:
    LandBlockchain(str(TEST_FILE))
    print("After tampering: True (unexpected)")
except ValueError:
    print("After tampering: False (tampering detected)")

# Remove the temporary test file.
TEST_FILE.unlink(missing_ok=True)
