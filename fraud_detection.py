# TrustRoute AI - Fraud Detection Prototype

class DeliveryUser:
    def __init__(self, user_id, speed, route_repeat, active_hours,
                 mock_gps, emulator, multiple_accounts):
        self.user_id = user_id
        self.speed = speed
        self.route_repeat = route_repeat
        self.active_hours = active_hours
        self.mock_gps = mock_gps
        self.emulator = emulator
        self.multiple_accounts = multiple_accounts


# ---------------- Device Integrity ----------------
def device_integrity_score(user):
    score = 100

    if user.mock_gps:
        score -= 40
    if user.emulator:
        score -= 30

    return max(score, 0)


# ---------------- Behavioral AI ----------------
def behavioral_score(user):
    score = 100

    # Unrealistic speed check
    if user.speed > 80:
        score -= 30

    # Repeated route detection
    if user.route_repeat:
        score -= 20

    # Non-human activity pattern
    if user.active_hours > 16:
        score -= 20

    return max(score, 0)


# ---------------- Account Linking ----------------
def account_linking_score(user):
    score = 100

    if user.multiple_accounts:
        score -= 40

    return max(score, 0)


# ---------------- Trust Score Engine ----------------
def calculate_trust_score(user):
    d_score = device_integrity_score(user)
    b_score = behavioral_score(user)
    a_score = account_linking_score(user)

    # Weighted scoring
    trust_score = (0.4 * d_score) + (0.4 * b_score) + (0.2 * a_score)

    return int(trust_score)


# ---------------- Decision Layer ----------------
def decision_action(trust_score):
    if trust_score >= 80:
        return "Normal"
    elif trust_score >= 50:
        return "Monitor"
    elif trust_score >= 20:
        return "Restrict"
    else:
        return "Verify / Flag"


# ---------------- Example Run ----------------
if __name__ == "__main__":
    # Example suspicious user
    user = DeliveryUser(
        user_id=1,
        speed=120,             # unrealistic speed
        route_repeat=True,     # repeated routes
        active_hours=20,       # non-human activity
        mock_gps=True,         # fake GPS
        emulator=False,
        multiple_accounts=True
    )

    score = calculate_trust_score(user)
    action = decision_action(score)

    print("User ID:", user.user_id)
    print("Trust Score:", score)
    print("System Action:", action)
