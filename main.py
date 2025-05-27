def sort(width, height, length, mass):
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


# ✅ Test Cases
assert sort(100, 100, 100, 10) == "SPECIAL"    # Bulky due to volume (1,000,000)
assert sort(150, 50, 20, 10) == "SPECIAL"      # Bulky due to dimension
assert sort(50, 50, 50, 21) == "SPECIAL"       # Heavy only
assert sort(200, 200, 200, 25) == "REJECTED"   # Both heavy and bulky
assert sort(10, 10, 10, 5) == "STANDARD"       # Neither
assert sort(149, 149, 149, 19) == "STANDARD"   # Just under thresholds
assert sort(150, 150, 150, 19.99) == "SPECIAL" # Bulky, not heavy
assert sort(149, 149, 149, 20) == "SPECIAL"    # Heavy, not bulky
